value = int(input())
dp = [None]*(value+1)
dp[1] = 0
if value > 1 : dp[2] = 1
if value > 2 : dp[3] = 1
def makeOne(n):
    for i in range(4,n+1):
        dp[i] = dp[i-1]+1
        if i % 3 == 0:
            if dp[i//3]+1 < dp[i]:
                dp[i] = dp[i//3]+1
        if i % 2 == 0:
            if dp[i//2]+1 < dp[i]:
                dp[i] = dp[i//2]+1
    return
makeOne(value)
print(dp[value])
