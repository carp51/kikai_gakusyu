# 状態数と行動数
num_states = 2
num_actions = 2
# 目標状態と期間長
target_state = 1
T = 3

# 状態遷移確率
transition_probs = [[0.5, 0.5], [0.3, 0.7], [0.9, 0.1], [0.5, 0.5]]
# 利得
rewards = [[1, 0], [1, 0], [1, 0], [1, 0]]

# DPテーブルの初期化
V = [[0] * (T + 1) for _ in range(num_states)]
policy = [[""] * (T + 1) for _ in range(num_states)]

# DPの再帰的な計算
for t in range(T - 1, -1, -1):
    for s in range(num_states):
        l = []
        for a in range(num_actions):
            tmp = 0
            for next_s in range(num_states):
                if t == T - 1:
                    tmp += transition_probs[s * num_actions + a][next_s] * (rewards[s * num_actions + a][next_s])
                else:
                    tmp += transition_probs[s * num_actions + a][next_s] * (V[next_s][t + 1])
                
            l.append(tmp)
            
        if l[0] >= l[1]:
            V[s][t] = l[0]
            policy[s][t] = "a1"
        else:
            V[s][t] = l[1]
            policy[s][t] = "a2"

print("最適な価値関数:")
for s in range(num_states):
    for t in range(1, T + 1):
        print(f"V(s{s + 1}, {t}) = {V[s][t - 1]}, d*(s{s + 1}, {t}) = {policy[s][t - 1]}")
