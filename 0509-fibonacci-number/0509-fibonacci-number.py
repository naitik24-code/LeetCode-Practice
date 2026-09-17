class Solution(object):
    def fib(self, n):
        prev=0
        curr=1
        for i in range(n):
            next_num=prev+curr
            prev=curr
            curr=next_num
        return prev
        