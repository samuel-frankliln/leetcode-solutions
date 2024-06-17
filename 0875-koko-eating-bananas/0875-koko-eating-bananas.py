class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1  # Minimum possible eating speed is 1
        r = max(piles)  # Maximum possible eating speed is the largest pile

        while l <= r:
            mid = (l + r) // 2
            if self.isPossible(mid, piles, h):
                r = mid - 1  # Try to find a smaller feasible eating speed
            else:
                l = mid + 1  # Increase the eating speed

        return l  # `l` is the smallest feasible eating speed

    def isPossible(self, k: int, piles: List[int], h: int) -> bool:
        total_hours = 0
        for n in piles:
            total_hours += math.ceil(n / k)
        return total_hours <= h