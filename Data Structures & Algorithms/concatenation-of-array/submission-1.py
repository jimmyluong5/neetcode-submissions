class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #create an array ans of length 2n
        n = len(nums)

        ans = [0] * (2*n) #create the ans array

        #then just append the first part then the i+n
        i = 0
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n]=nums[i]
        return ans

        #after just add the other 
