def combinationSum4(nums, target):
    dp = {0:1} // "base case"
    for i in range(1, target+1):
        dp[i] = 0 // "we will start with zero and update the final value in the below loop"
        for j in nums:
            dp[i] += dp.get(i-j, 0) // "if we get negative values, we will return 0"
        print(dp[i])
    return dp[target] // "return dp[target] is nothing but sum(target - nums[0] , target - nums[2], ..., target - nums[n-1])"