# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

#0 we got the right answer, so the else statement
#-1 higher so the number must be lower so right = mid-1
#1 lower so the number must be higher so left = mid+1

class Solution:
    def guessNumber(self, n: int) -> int:
        #binary search
        #instead of using an array, we use the api given as guess(mid)
        #we don't get to see anything from guess, if guess(mid) > pick then our number is lower.
        left = 1
        right = n

        while left <= right:
            mid = left + (right-left)//2
            if guess(mid) == -1: #then our guess is too high
                right = mid-1
            elif guess(mid) == 1: #our guess is too low
                left = mid+1
            else: #then guess(mid) == 0 we found the correct number
                return mid
            
        


            

