from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PyQt5.QtGui import QPixmap
import sys
from gaming_ui import Ui_MainWindow
import matplotlib.pyplot as plt
import matplotlib
import os
import pickle
import copy
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
matplotlib.use('TkAgg')  # 使用适当的后端（TkAgg 只是一个例子）
plt.rcParams['font.size'] = 9


def draw(data_num, data_money):
    print('drawing...')
    plt.clf()
    if sum(data_money) < 0.1:
        plt.savefig('./result.png')
        return
    plt.gcf().set_size_inches(11, 6)
    plt.bar(data_num, data_money, color='blue')
    # 添加标签和标题
    plt.xlabel('号码')
    plt.ylabel('累计金额')
    plt.title('号码累计金额分布(累计总金额：{:.2f}元)'.format(sum(data_money)))
    x_ticks = [i for i in range(1, 50)]
    x_tick_labels = [str(i) for i in range(1, 50)]
    plt.xticks(ticks=x_ticks, labels=x_tick_labels)
    for i, value in enumerate(data_money):
        plt.text(i+1, value, str(value), ha='center', va='bottom')
    plt.savefig('./result.png')


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, data_money, data_log, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.data_num = [i for i in range(1, 50)]
        self.data_money = data_money
        self.data_log = data_log
        self.textBrowser.setText(self.data_log)
        self.resize(1600, 1200)

    def click_buy_button(self):
        print('ok')
        num = self.lineEdit.text()
        money = self.lineEdit_2.text()
        if num == '' and money == '':
            self.data_log += '请输入号码和金额！\n'
        elif num == '':
            self.data_log += '请输入号码！\n'
        elif num == '':
            self.data_log += '请输入金额！\n'
        else:
            try:
                num = int(num)
                money = float(money)
                if 1 <= num <= 49:
                    self.data_money[num-1] += money
                    self.data_log += '选择号码：{}号，买入金额：{:.2f}元。\n'.format(num, money)
                else:
                    self.data_log += '输入号码有误，请重新输入!\n'
            except:
                self.data_log += '输入号码或者金额有误，请重新输入!\n'
        print(self.data_log)
        self.textBrowser.setText(self.data_log)
        self.save_data()

    def clear_history(self):
        self.data_money = [0 for i in range(1, 50)]
        self.data_log = '-------------- 买入记录 -------------\n'
        self.textBrowser.setText(self.data_log)
        self.save_data()
        self.show_dis_fig()

    def show_dis_fig(self):
        print(self.data_money)
        draw(data_num=self.data_num, data_money=self.data_money)
        scene = QGraphicsScene()
        pixmap = QPixmap('./result.png')
        scene.addPixmap(pixmap)
        self.graphicsView.setScene(scene)
        self.graphicsView.show()

    def save_data(self):
        with open('./data_money.pkl', 'wb') as f:
            pickle.dump(copy.deepcopy(self.data_money), f)
        with open('./data_log.pkl', 'wb') as f:
            pickle.dump(copy.deepcopy(self.data_log), f)

    def query_sum_money(self):
        num = self.lineEdit.text()
        if num == '':
            self.data_log += '请先输入选择号码！'
            self.textBrowser.setText(self.data_log)
            return
        num = int(num)
        if 1 <= num <= 49:
            self.lineEdit_3.setText('{:.2f}'.format(self.data_money[num-1]))
        else:
            self.data_log += '输入数字大于49或者小于1，请重新输入！'
            self.textBrowser.setText(self.data_log)


def main(data_num, data_log):
    app = QApplication(sys.argv)  # 创建应用程序对象
    MainWindow = MyMainWindow(data_num, data_log)  # 创建主窗口
    MainWindow.show()  # 显示主窗口
    sys.exit(app.exec_())  # 在主线程中退出


if __name__ == '__main__':
    if os.path.exists('./data_money.pkl'):
        with open('./data_money.pkl', 'rb') as f:
            data_money = pickle.load(f)
    else:
        data_money = [0 for i in range(49)]
    if os.path.exists('./data_log.pkl'):
        with open('./data_log.pkl', 'rb') as f:
            data_log = pickle.load(f)
    else:
        data_log = '-------------- 买入记录 -------------\n'
    main(data_money, data_log)
