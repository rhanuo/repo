class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if (1 not in digits) and (2 not in digits) and (3 not in digits) and (4 not in digits) and (5 not in digits) 
        and (6 not in digits) and (7 not in digits) and (8 not in digits) and (0 not in digits):
            return [1]+[0]*(len(digits))
        else:
            if digits[-1]!=9:
                digits[-1]+=1
                return digits
            elif digits[-1]==9:
                for i in range(len(digits)-1,-1,-1):
                    if digits[i]!=9:
                        digits[i]+=1
                        for j in range(i+1,len(digits)):
                            if digits[j]==9:
                                digits[j]=0
                                continue
                        return digits
