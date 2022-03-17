class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = s + t
        for i in c:
            if c.count(i)%2!=0:
                return i
