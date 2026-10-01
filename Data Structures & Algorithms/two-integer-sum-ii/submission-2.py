class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointers with binary search twist
        left = 0
        right = len(numbers)-1
        while left<=right:
            if target>numbers[left]+numbers[right]:
                #move the right pointer down
                left +=1
            elif target<numbers[left]+numbers[right]:
                right-=1
            else:
                return [left+1, right+1]

        return [left+1, right+1]
