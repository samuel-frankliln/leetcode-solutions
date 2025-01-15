class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero=0
        product =1
        
        for n in nums:
            if n==0:
                count_zero +=1
            else:
                product*=n
        
        output=[]

        for m in nums:
            if count_zero==0:
                output.append(product//m)
            elif count_zero==1:
                if m==0:
                    output.append(product)
                else:
                    output.append(0)
            elif count_zero==2:
                output.append(0)
        
        return output


        