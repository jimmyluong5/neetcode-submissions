class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                #calculate the profit and then calculate max profit
                profit = prices[right]-prices[left]
                max_profit=max(max_profit, profit)
                
            else:
                #move the left ptr to the right pointer because thats the new low point.
                left = right
            #move the right ptr
            right+=1
        return max_profit
            