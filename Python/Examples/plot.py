import matplotlib.pyplot as plt
import numpy as np

# https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

# eg.1
# 绘制 (1,1) ... (4,4) 相连线段
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some number')
# plt.show()

# # eg.2
# # 绘制(1,2) (1,4)相连线段
# plt.plot([1, 1], [2, 4])
# # 可调整坐标轴范围
# plt.axis([0.5, 1.5, 1, 5])
# plt.show()

# # eg.3
# # 散点图
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()


# # eg.4
# # 使用numpy的array对象
# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)  # 创建区间 [0,5] 且每个区间长度0.2

# # red dashes, blue squares and green triangles 绘制不同颜色的图像
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')  # ** 在python中表示指数运算 t^n
# plt.show()


# eg.5
# 不同类型的散点图效果
# np.arange(50) 从1到49 间隔为1
# randint(0,50,50) 从0到50 50个随机整数

# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}

# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()


# eg.6
# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)

# # the histogram of the data
# n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# plt.show()

# # eg.7 分组图
# names = ['group_a', 'group_b', 'group_c']
# values = [1, 10, 100]

# plt.figure(figsize=(9, 3))

# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()


# eg.8 绘制函数

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.show()
