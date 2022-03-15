class Solution:
    def checkRecord(self, s: str) -> bool:
        a=("LLL")
        if s.count("A")>=2 or a in s:
            return False
        return True
