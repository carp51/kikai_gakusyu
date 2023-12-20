# NumPyをインポート
import numpy as np

# パラメータとデータの設定
S = 2
A = 2
T = 2
theta_probs = [0.5, 0.5]
N_s1 = [[[0 for _ in range(S)] for _ in range(A)] for _ in range(S)]
theta_probs_1 = [
    [0.6, 0.4], 
    [0.2, 0.8], 
    [0.2, 0.8], 
    [0.6, 0.4]
    ]
theta_probs_2 = [
    [0.8, 0.2], 
    [0.2, 0.8], 
    [0.4, 0.6], 
    [0.8, 0.2]
    ]
rewards = [
    [100, 60],
    [50, 100],
    [80, 100],
    [120, 80]
]

pr_1, pr_2 = 0.5, 0.5
def pr(N, flag):
    ans = 0
    
    if flag == 1:
        t, s1, a, s2 = 1, N[1], N[2], N[3]
        # 0.5は問題によって変わるよ
        ans += pr_1 * theta_probs_1[2 * (s1 - 1) + a - 1][s2 - 1]
        ans /= (pr_1 * theta_probs_1[2 * (s1 - 1) + a - 1][s2 - 1] + pr_2 * theta_probs_2[2 * (s1 - 1) + a - 1][s2 - 1])
    else:
        t, s1, a, s2 = 2, N[1], N[2], N[3]
        ans += pr_2 * theta_probs_2[2 * (s1 - 1) + a - 1][s2 - 1]
        ans /= (pr_1 * theta_probs_1[2 * (s1 - 1) + a - 1][s2 - 1] + pr_2 * theta_probs_2[2 * (s1 - 1) + a - 1][s2 - 1])
    
    return ans

N = [[1, 2, 1, 1], [2, 2, 1, 2], [1, 2, 2, 1], [2, 2, 2, 2], [2, 2, 2, 2]] 

V_d = [[[0.0, 0.0], ""] for _ in range(5)]

for t in range(5):
    for a in range(2):
        if t == 4:
            V_d[t][0][a] += pr_1 * theta_probs_1[2 * (N[t][3] - 1) + a][0] + pr_2 * theta_probs_2[2 * (N[t][3] - 1) + a][0]
            V_d[t][0][a] *= max(V_d[(2 * (a))][0])
            tmp = 0
            tmp = pr_1 * theta_probs_1[2 * (N[t][3] - 1) + a][1] + pr_2 * theta_probs_2[2 * (N[t][3] - 1) + a][1]
            tmp *= max(V_d[(2 * a) + 1][0])
            
            V_d[t][0][a] += tmp
            continue
        
        V_d[t][0][a] = pr(N[t], 1) * theta_probs_1[2 * (N[t][3] - 1) + a][0] + pr(N[t], 2) * theta_probs_2[2 * (N[t][3] - 1) + a][0]
        V_d[t][0][a] *= rewards[2 * (N[t][3] - 1) + a][0]
        tmp = 0
        tmp = pr(N[t], 1) * theta_probs_1[2 * (N[t][3] - 1) + a][1] + pr(N[t], 2) * theta_probs_2[2 * (N[t][3] - 1) + a][1]
        tmp *= rewards[2 * (N[t][3] - 1) + a][1]
        V_d[t][0][a] += tmp
        
    if V_d[t][0][0] >= V_d[t][0][1]:
        V_d[t][1] = "a1"
    else:
        V_d[t][1] = "a2"
        
for vd in V_d:
    print(vd)
