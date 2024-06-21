class Solution:
    def rob(self, nums: List[int]) -> int:
        def letsRob(nums):
            if len(nums)==0: return 0

            dp=[]
            dp.append(0)
            dp.append(nums[0])

            for i in range(1,len(nums)):
                dp.append(max(dp[i],dp[i-1]+nums[i]))

            return dp[len(nums)]
        return max(nums[0],letsRob(nums[1:]),letsRob(nums[:-1]) )
        