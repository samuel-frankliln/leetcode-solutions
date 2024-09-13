class Solution:
    def isHappy(self, n: int) -> bool:
        memory = []

        while n != 1:
            if n in memory:
                return False
            memory.append(n)
            n = self.sumSquareDigits(n)

        return True

    def sumSquareDigits(self, num: int) -> int:
        square_num = 0
        while num != 0:
            temp = num % 10
            square_num += temp ** 2
            num = num // 10
        return square_num
