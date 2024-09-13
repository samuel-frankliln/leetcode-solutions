class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hash_map= {}
        for i,n in enumerate(nums):
            if n in hash_map:
                hash_map[n].append(i)
            else:
                hash_map[n]=[i]

        for element, indices in hash_map.items():
            for i in range(1,len(indices)):
                if(abs(indices[i]- indices[i-1])<=k):
                    return True
        return False  