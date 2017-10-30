n = int(input())
setList = list(map(int, input().split()))
setList.insert(0,0)
dp = [0]*(n+1)
for i in range(1,n+1):
    dp[i] = 0
    for j in range(1,i+1):
        dp[i] = int(max(dp[i], dp[i-j]+setList[j]))
print(dp[n])