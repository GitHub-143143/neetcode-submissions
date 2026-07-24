class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        a = sorted(a)
        maxi = 1
        count = 1
        for i in range(1,len(a)):
            if a[i] ==a[i-1]+1:
                count+=1
            else:
                count = 1
            maxi = max(maxi,count)
        if len(nums)==0: return 0
        return maxi
        