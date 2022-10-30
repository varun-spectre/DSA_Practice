def lengthOfLIS(nums):
    n = len(nums)
    dp = [1]*(n)
    
    for i in range(n):
        max_ = 1
        for j in range(i-1, -1, -1):
            if nums[j] < nums[i]:
                # print("here")
                # print(dp[j],  max_)
                max_ = max(dp[j]+1, max_)
                
        dp[i] = max_
    return max(dp)