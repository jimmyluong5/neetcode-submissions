class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since its sorted, kinda hints binary search?
        left = 0 
        right = len(numbers)-1

        #literally just two sum but with binary search
        #we also calculate diff which is target - numbers[i]
        #we are adding the indices not the value
        while left<=right:
            if target > numbers[left]+numbers[right]:
                left +=1
            elif target < numbers[left]+numbers[right]:
                right -=1
            else:
                return [left+1, right+1]
        return [left+1, right+1]
        