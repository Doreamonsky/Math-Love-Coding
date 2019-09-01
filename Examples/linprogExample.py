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

# Linear programming solves problems of the following form:
# Ax<=b
# Aeq * x = beq
# lb<=x<=ub bounds 来限制范围

# 例 1  某机床厂生产甲、乙两种机床，每台销售后的利润分别为 4000 元与 3000 元。
# linprog 默认是求最小值，求最大值要把 c 反号
c = np.array([4, 3])
A = [[2, 1], [1, 1]]
b = [10, 8]

res = optimize.linprog(-c, A_ub=A, b_ub=b, bounds=[(0, None), (0, 7)])

print(res)


# 例2  运输问题（产销平衡）
# 某商品有m个产地，n个销地。各产地的产量分别是A1，A2......Am，各销地的需求量分别是B1，B2......Bn。若商品从i产地运输到j销地其单位运价为Cij，请问该如何调运才能使总运费最省？

c = [3, 11, 3, 10, 1, 9, 2, 8, 7, 4, 10, 5]

Aeq = [
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
]

beq = [7, 4, 9, 3, 6, 5, 6]

res = optimize.linprog(
    c,
    A_eq=Aeq,
    b_eq=beq,
    bounds=[
        (0, None),
        (0, None),
        (0, None),
        (0, None),
        (0, None),
        (0, None),
        (0, None),
        (0, None),
        (0, None),
        (0, None),
        (0, None),
        (0, None)
    ]
)

print(res)
