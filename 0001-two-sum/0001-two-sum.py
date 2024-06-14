
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_with_indices = [(num, i) for i, num in enumerate(nums)]
        
        num_with_indices.sort()
        
        l, r = 0, len(num_with_indices) - 1
        
        while l < r:
            current_sum = num_with_indices[l][0] + num_with_indices[r][0]
            if current_sum == target:
                # Return the original indices
                return [num_with_indices[l][1], num_with_indices[r][1]]
            elif current_sum < target:
                l += 1
            else:
                r -= 1
                
        return []