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

e = [e1, e2]

# 初期確率
prior_prob = [0.4, 0.3, 0.3]

N = [[1, 1, 2], [1, 2, 2], [2, 1, 2], [2, 2, 2], [1, 1, 1]] 
V_d = [[[0.0, 0.0, 0.0], ""] for _ in range(5)]

for t in range(5):
    for a in range(3):
        if t == 4:
            if a == 2:
                continue
            
            V_d[t][0][a] += prior_prob[0] * e[a][0][0] + prior_prob[1] * e[a][1][0] +  prior_prob[2] * e[a][2][0]
            V_d[t][0][a] *= max(V_d[2 * a][0])
 
            tmp = 0
            tmp = prior_prob[0] * e[a][0][1] + prior_prob[1] * e[a][1][1] +  prior_prob[2] * e[a][2][1]
            tmp *= max(V_d[2 * a + 1][0])
            
            V_d[t][0][a] += tmp
            V_d[t][0][a] = round(V_d[t][0][a], 3)
            
            continue
        
        E, O, T = N[t][0], N[t][1], N[t][2]
        V_d[t][0][a] = prior_prob[a] * e[E - 1][a][O - 1]
        
        tmp = 0
        tmp += prior_prob[0] * e[E - 1][0][O - 1] + prior_prob[1] * e[E - 1][1][O - 1] +  prior_prob[2] * e[E - 1][2][O - 1]
        V_d[t][0][a] /= tmp
        
        V_d[t][0][a] = round(V_d[t][0][a], 3)
        
    max_value = sorted(V_d[t][0], reverse=True)[0]
    for k in range(3):
        if max_value == V_d[t][0][k]:
            max_index = k
    
    V_d[t][1] = max_index + 1

for vd in V_d:
    print(vd)
