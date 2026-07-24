class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pos = 0
        a = set(nums)
        a = sorted(a)
        for i in range(1,len(a)+2):
            if i not in a:
                pos = i
                break
        return pos
        