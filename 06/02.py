# 入力層
input_layer = [
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
]

# フィルタ
filter1 = [
    [2, 1, 2],
    [1, 2, 1],
    [2, 1, 2]
]

b1_F = 1

# 畳み込み演算
def convolution(input_layer, filter):
    filter_size = len(filter)
    result_size = len(input_layer) - filter_size + 1
    result = b1_F

    for i in range(1, result_size):
        for j in range(1, result_size):
            result += input_layer[i][j] * filter[i - 1][j - 1]

    return result

# 結果の表示
output = convolution(input_layer, filter1)

# 入力値 I_{1,2,2}^F の計算
I_1_2_2_F = output
print("入力値 I_{1,2,2}^F:", I_1_2_2_F)
