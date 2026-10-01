class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #this is just two pointers and binary search
        left = 0
        right=len(numbers)-1

        while left<=right:
            #calculate mid
            mid = left+(right-left)//2
            sum = numbers[left]+numbers[right]
            if target>sum:
                #move the left pointer up
                left+=1
            elif target<sum:
                #move right ptr
                right-=1
            else:
                return [left+1, right+1]
        return [left+1, right+1]