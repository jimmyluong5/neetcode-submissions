class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <=right:
            k= (left+right)//2
            time = 0
            for p in piles:
                time += math.ceil( float(p)/float(k))
            
            if time <= h:
                #set the result to k which is the middle number
                res = k
                #move the right ptr
                right = k-1
            else:
                left = k+1
        return res