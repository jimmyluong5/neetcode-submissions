class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two ptrs, just see if the array values are equal and move up to r/2?
        #we need to remove all spaces and non alpha characters
        s = "".join(i for i in s if i.isalnum())

        #then turn the string to lower case or uppercase
        s = s.lower()

        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
                
            left +=1
            right -=1
        return True