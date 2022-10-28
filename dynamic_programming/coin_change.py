def coinChange(coins, amount: int):
    if amount == 0:
        return 0
    n_cols = amount+1
    n_rows = len(coins) + 1
    dp = [[2**64]*(amount+1) for i in range(len(coins)+1)]

    for i in range(n_rows):
        dp[i][0] = 0

    for i in range(1, n_rows):
        for j in range(1, amount+1):
            if j < coins[i-1]:
                dp[i][j] =  dp[i-1][j]
            else:
                take = 1 + dp[i][j-coins[i-1]]
                leave = dp[i-1][j]
                dp[i][j] = min(take, leave)
                

    return -1 if dp[n_rows-1][n_cols-1]==2**64 else dp[n_rows-1][n_cols-1]