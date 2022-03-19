class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs[0])
        n = len(strs)
        strs.sort()
        if not strs:
            return ""
        for index,item in enumerate(strs[0]):
            for i in range(1,n):
                if item != strs[i][index]:
                    return strs[0][:index]
        return strs[0]
