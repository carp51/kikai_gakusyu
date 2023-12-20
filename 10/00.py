# パラメータの設定
S = 2  # 状態数
A = 2  # 行動数
E = 2  # イベント数
T = 2  # 期間長

# 初期確率
prior_prob = [0.5, 0.5]

# 遷移確率
theta_probs = [
    [0.6, 0.4], 
    [0.2, 0.8],
    [0.5, 0.5], 
    [0.8, 0.2]
]

# 利得
reward = [100, 10]

# イベント生起確率
event_prob = [
    [0.8, 0.2],
    [0.2, 0.8]
]

def pr(N, N1):
    ans = 0
    s, a1, e, a2 = N1[0], N[0], N[1], N1[1]
    
    ans = pr_4(s, a1, e, a2)
    
    return ans
    
def pr_4(s, a1, e, a2):
    tmp = pr_3(1, a1, e) * theta_probs[(a2 - 1) + 0][s - 1] + pr_3(2, a1, e) * theta_probs[(a2 - 1) + 2][s - 1]
    return pr_3(1, a1, e) * theta_probs[(a2 - 1) + 0][s - 1] + pr_3(2, a1, e) * theta_probs[(a2 - 1) + 2][s - 1]

def pr_3(s, a1, e):
    ans = pr_2(s, a1) *  event_prob[s - 1][e - 1]
    tmp = [pr_2(s, a1), event_prob[s - 1][e - 1]]
    ans /= pr_2(1, a1) * event_prob[0][e - 1] + pr_2(2, a1) * event_prob[1][e - 1]
    
    return ans

def pr_2(s, a1):
    tmp = prior_prob[0] * theta_probs[(a1 - 1) + 0][s - 1] + prior_prob[1] * theta_probs[(a1 - 1) + 2][s - 1]

    return prior_prob[0] * theta_probs[(a1 - 1) + 0][s - 1] + prior_prob[1] * theta_probs[(a1 - 1) + 2][s - 1]

N = [[1, 1, 2], [1, 2, 2], [2, 1, 2], [2, 2, 2], [1, 1, 1]] 
V_d = [[[0.0, 0.0], ""] for _ in range(5)]

print(pr(N[2], [2, 2]))
for t in range(5):
    for a in range(2):
        if t == 4:
            V_d[t][0][a] += pr_2(1, a + 1) * event_prob[0][0] + pr_2(2, a + 1) * event_prob[0][1]
            V_d[t][0][a] *= reward[0] + max(V_d[2 * a][0])
            awww = [pr_2(1, a + 1), event_prob[0][0], pr_2(2, a + 1), event_prob[0][1]]
            b = max(V_d[2 * a][0])
            tmp = 0
            tmp = pr_2(1, a + 1) * event_prob[1][0] + pr_2(2, a + 1) * event_prob[1][1]
            tmp *= reward[1] + max(V_d[2 * a + 1][0])
            
            
            V_d[t][0][a] += tmp
            continue
        
        
        V_d[t][0][a] = pr(N[t], [1, a + 1]) * event_prob[0][0] + pr(N[t], [2, a + 1]) * event_prob[0][1]
        V_d[t][0][a] *= reward[0]
        
        tmp = 0
        tmp = pr(N[t], [1, a + 1]) * event_prob[1][0] + pr(N[t], [2, a + 1]) * event_prob[1][1]
        # a = [pr(N[t], [1, 1]), event_prob[1][0], pr(N[t], [2, 1]), event_prob[1][1]]
        tmp *= reward[1]
        V_d[t][0][a] += tmp
        
        if V_d[t][0][0] >= V_d[t][0][1]:
            V_d[t][1] = "a1"
        else:
            V_d[t][1] = "a2"
        tmp = 0
        
if V_d[t][0][0] >= V_d[t][0][1]:
    V_d[t][1] = "a1"
else:
    V_d[t][1] = "a2"
        
for vd in V_d:
    print(vd)