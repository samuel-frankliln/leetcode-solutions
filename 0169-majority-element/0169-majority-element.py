class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        majority_count = len(nums) // 2
        for key, value in count.items():
            if value > majority_count:
                return key
            
        