#moedas spoj
v = [20, 30, 60]
n = len(v)
t = 120

dp = {0:0}


def menor_troco():
    for i in range(1,t+1):
        dp[i] = 100000
    
    for i in range(1,t+1):
        for k in range(0,n):
            if i-v[k] >= 0:
                dp[i] = min(dp[i-v[k]]+1, dp[i])
    
    return dp[t]

print(menor_troco())
