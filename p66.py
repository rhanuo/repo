class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:#如果列表为空
            return [1]#返回1
        digits[-1]+=1# 最末位加一
        for current_index in range(len(digits)-1,0,-1):# 从最末位开始循环到第二高位
            if digits[current_index]>=10:#如果当前位需要进位
                digits[current_index-1]+=digits[current_index]//10
                digits[current_index]%=10#进位到上一位
        if digits[0]>=10:#如果最高位需要进位
            digits.insert(0,digits[0]//10)#进位到最高位
            digits[1]%=10
        return digits
