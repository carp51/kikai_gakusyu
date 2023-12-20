e1 = [
    [0.2, 0.8],
    [0.8, 0.2],
    [0.6, 0.4]
]

e2 = [
    [0.2, 0.8],
    [0.8, 0.2],
    [0.9, 0.1]
]

# 事前確率
prior_prob = [0.05, 0.8, 0.15]

pr_2 = [0.0, 0.0, 0.0]

for i in range(3):
    pr_2[i] += prior_prob[i] * e1[i][0] * e2[i][1]
    tmp = 0.0
    for j in range(3):
        tmp += prior_prob[j] * e1[j][0] * e2[j][1]
        
    pr_2[i] /= tmp
    
print(pr_2)

max_value = sorted(pr_2, reverse=True)[0]
for k in range(3):
    if max_value == pr_2[k]:
        max_index = k

print(max_index + 1)
    