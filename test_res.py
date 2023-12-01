import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # 使用适当的后端（TkAgg 只是一个例子）
from matplotlib.font_manager import FontProperties
# 选择合适的字体，例如SimHei或其他中文字体
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
# 设置全局字体
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
import  numpy as np

import matplotlib.pyplot as plt
import numpy as np

# 示例数据
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [20, 45, 30, 60]

# 绘制柱状图
plt.bar(categories, values, color='skyblue')

# 在每个柱子上显示数字
for i, value in enumerate(values):
    plt.text(i, value + 1, str(value), ha='center', va='bottom')

# 添加标签和标题
plt.xlabel('类别')
plt.ylabel('值')
plt.title('柱状图示例')

# 显示图表
plt.show()