class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left+1
        maxProfit = 0
        while right < len(prices):
            
            if prices[left]<prices[right]:
                #calculate the profit
                profit = prices[right]-prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                #prices[right] is smaller, move the left pointer to the right pointer, and move the right pointer forward after
                left = right
            right +=1
        return maxProfit 