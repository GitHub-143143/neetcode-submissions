class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ""
        plus = []
        for i in digits:
            a+=''.join(str(i))
        b = int(a)+1
        for i in str(b):
            plus.append(int(i))
        return plus
                