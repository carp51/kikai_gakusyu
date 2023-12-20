# 入力層
input_layer = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1]
]

# フィルタ
filter1 = [
    [1, 2, 2],
    [2, 2, 1],
    [1, 2, 2]
]

B1_F = 2

# 畳み込み演算
def convolution(input_layer, filter):
    filter_size = len(filter)
    result_size = len(input_layer) - filter_size + 1
    result = [[B1_F] * result_size for _ in range(result_size)]

    for i in range(result_size):
        for j in range(result_size):
            result[i][j] += sum(input_layer[i+k][j+l] * filter[k][l] for k in range(filter_size) for l in range(filter_size))

    return result

# 結果の表示
output = convolution(input_layer, filter1)
print("畳み込み結果:")
for row in output:
    print(row)

# 入力値 I_{1,2,2}^F の計算
I_1_2_2_F = output[0][2]
print("入力値 I_{1,2,2}^F:", I_1_2_2_F)
