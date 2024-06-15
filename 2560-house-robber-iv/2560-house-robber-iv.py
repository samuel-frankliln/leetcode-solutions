class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def isPossible(maxh):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= maxh:
                    count += 1
                    i += 1
                i += 1
            if count >= k:
                return True
            return False

        low = min(nums)
        high = max(nums)
        res = high
        while low <= high:
            mid = (low + high) // 2
            if isPossible(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res