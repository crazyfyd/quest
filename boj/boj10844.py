n = int(input())
dp = [[0 for col in range(11)] for row in range(101)]
for k in range(1,10):
    dp[1][k] = 1
for i in range(2,n+1):
    for j in range(0,10):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n])%1000000000)