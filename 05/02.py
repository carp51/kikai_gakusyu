x = [0, 1, 1, 1]

w = [
    [1, 1, 2, 1, 1, 2, 2, 1],
    [2, 1, 1, 1, 2, 1, 1, 5]
]

def f_m(l):
    return l ** 2


def f_o(l):
    return l + 10


l1_M = sum([w[0][i] * x[i] for i in range(len(x))]) + w[0][4]
l2_M = sum([w[1][i] * x[i] for i in range(len(x))]) + w[1][4]

o1_M = f_m(l1_M)
o2_M = f_m(l2_M)

o = [o1_M, o2_M]

l1_O = sum([w[0][i] * o[i - 5] for i in range(5, 7)]) + w[0][7]
l2_O = sum([w[1][i] * o[i - 5] for i in range(5, 7)]) + w[1][7]

Y1 = f_o(l1_O)
Y2 = f_o(l2_O)

print(f'(O1_M, O2_M, Y1, Y2) = {o1_M, o2_M, Y1, Y2}')