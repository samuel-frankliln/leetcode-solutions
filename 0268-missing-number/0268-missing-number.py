class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=0
        for i in nums:
            total+=i


        n= len(nums)
        total_actual = (n)*(n+1)//2 
        return total_actual - total
        