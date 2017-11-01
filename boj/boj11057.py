n = int(input())
dp = [[0 for col in range(11)] for row in range(10001)]
mod = 10007
for k in range(10):
    dp[1][k] = 1
if n > 1:
    for i in range(2,n+1):
        for j in range(10):
            mp = 0
            for m in range(j,10):
                mp = mp+dp[i-1][m]
            dp[i][j] = mp
print(sum(dp[n])%mod)