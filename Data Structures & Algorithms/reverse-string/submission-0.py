class Solution:
    def reverseString(self, s: List[str]) -> None:
        #two ptr approach, place one ptr at index 0 and one ptr at
        #index len(s)-1 then just swap them.
        l = 0
        r = len(s)-1
        temp = s[0]
        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l +=1
            r -=1
        
        