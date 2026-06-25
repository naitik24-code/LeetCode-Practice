class Solution(object):
    def topKFrequent(self, nums, k):
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        sorted_items=sorted(freq.items(), key=lambda x : x[1],reverse=True)
        answer=[]
        for i in range(k):
            answer.append(sorted_items[i][0])
        return answer
        