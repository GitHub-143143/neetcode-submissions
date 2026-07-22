import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        low = 0
        high = len(c)-1
        ans  = True
        while low<=high:
            if c[low] != c[high]:
                ans = False
            low+=1
            high-=1
        return ans



        