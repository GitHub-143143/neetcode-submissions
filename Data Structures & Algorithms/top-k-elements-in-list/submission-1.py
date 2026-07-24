class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
    
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        s = sorted(h.items(), key=lambda x:x[1],reverse=True)
        top = [i[0] for i in s[:k]]
        return top

        