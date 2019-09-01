from scipy import optimize
import numpy as np


# 代码文档： https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html

# c = [2, 3, -5]

# A = [[-2, 5, -1], [1, 3, 1]]

# b = [-10, 12]

# Aeq = [[1, 1, 1]]  # Caution! Aeq is a matrix

# beq = [7]

# res = optimize.linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq,
#                        bounds=[(0, None), (0, None), (0, None)])


# 例 1  某机床厂生产甲、乙两种机床，每台销售后的利润分别为 4000 元与 3000 元。
# linprog 默认是求最小值，求最大值要把 c 反号
c = np.array([4, 3])
A = [[2, 1], [1, 1]]
b = [10, 8]

res = optimize.linprog(-c, A_ub=A, b_ub=b, bounds=[(0, None), (0, 7)])

print(res)
