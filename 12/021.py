pr_1 = [
    [0.6, 0.4],
    [0.2, 0.8],
    [0.5, 0.5],
    [0.5, 0.5]
]

pr_2 = [
    [0.8, 0.2],
    [0.5, 0.5],
    [0.2, 0.8],
    [0.4, 0.6]
]

pr = [pr_1, pr_2]
B = 0.8

# 遷移確率
pr_to = [[0.8, 0.2],
         [0.2, 0.8]]

r = [
    [100, 10],
    [50, 50],
    [100, 20],
    [60, 80]
]

N = [[1, 1, 2], [1, 2, 2], [2, 1, 2], [2, 2, 2], [1, 1, 1]] 
V_d = [[[0.0, 0.0], -1, ""] for _ in range(5)]

for t in range(5):
    for a in range(2):
        if t == 4:
            V_d[t][0][a] += pr_to[1][0] * V_d[0][1] + pr_to[1][1] * V_d[1][1]
            V_d[t][0][a] *= B
            V_d[t][0][a] += r[a][0]
            V_d[t][0][a] *= pr[1][a][0]
            
            tmp = pr_to[1][0] * V_d[2][1] + pr_to[1][1] * V_d[3][1]
            tmp *= B
            tmp += r[a][1]
            tmp *= pr[1][a][1]
            
            V_d[t][0][a] += tmp
            
            V_d[t][0][a] = round(V_d[t][0][a], 2)
            
            V_d[t][1] = max(V_d[t][0])
    
            if V_d[t][0][0] > V_d[t][0][1]:
                V_d[t][2] = "a1"
            else:
                V_d[t][2] = "a2"
            
            continue
        
        S, Th, T = N[t][0], N[t][1], N[t][2]
        V_d[t][0][a] = pr[t % 2][2 * (S - 1) + a][0] * r[2 * (t // 2) + a][0] + pr[t % 2][2 * (S - 1) + a][1] *  r[2 * (t // 2) + a][1]
        V_d[t][0][a] = round(V_d[t][0][a], 3)
        
    V_d[t][1] = max(V_d[t][0])
    
    if V_d[t][0][0] > V_d[t][0][1]:
        V_d[t][2] = "a1"
    else:
        V_d[t][2] = "a2"

for vd in V_d:
    print(vd)
