e1 = [
    [0.8, 0.2],
    [0.2, 0.8],
    [0.5, 0.5]
]

e2 = [
    [0.5, 0.5],
    [0.8, 0.2],
    [0.2, 0.8]
]

# 初期確率
prior_prob = [0.4, 0.3, 0.3]

pr_2 = [0.0, 0.0, 0.0]

for i in range(3):
    pr_2[i] += prior_prob[i] * e1[i][0] * e2[i][1]
    tmp = 0.0
    for j in range(3):
        tmp += prior_prob[j] * e1[j][0] * e2[j][1]
        
    pr_2[i] /= tmp
    
print(pr_2)


    