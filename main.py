import matplotlib.pyplot as plt
import matplotlib
import numpy as np
# 设置全局字体
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
matplotlib.use('TkAgg')  # 使用适当的后端（TkAgg 只是一个例子）
plt.rcParams['font.size'] = 12


def draw(data_num, data_money):
    print(data_money)
    # 生成柱状图
    # plt.figure(figsize=(8, 6))  # 宽度为10英寸，高度为10英寸
    plt.bar(data_num, data_money, color='blue')
    # 添加标签和标题
    plt.xlabel('号码')
    plt.ylabel('累计金额')
    plt.title('号码累计金额分布(总金额：{}元)'.format(sum(data_money)))
    x_ticks = [i for i in range(1, 50)]
    x_tick_labels = [str(i) for i in range(1, 50)]
    plt.xticks(ticks=x_ticks, labels=x_tick_labels)
    for i, value in enumerate(data_money):
        plt.text(i+1, value, str(value), ha='center', va='bottom')
    # plt.show()
    plt.savefig('./result.png', dpi=840)


if __name__ == '__main__':
    data_num = [i for i in range(1, 50)]
    data_money = [0 for i in range(49)]
    while 1:
        s = input()
        try:
            num, money = s.strip().split()
            num = int(num)
            money = int(money)
            data_money[num] += money
        except:
            if s.strip() == 'show':
                draw(data_num=data_num, data_money=data_money)


