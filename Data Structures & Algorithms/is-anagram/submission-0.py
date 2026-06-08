class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
'''        
        for x in s:
            if x not in t:
                return False
            elif len(s) != len(t):
                return False
        return True
'''
        