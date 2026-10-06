class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #check if the len of needle and haystack ==0
        if len(haystack) == 0 or len(needle) == 0:
            return -1
        
        #create the pointers
        left = 0
        right = 0

        while right < len(haystack):
            #check if the length between the pointers equals to size of the needle, we finna do sliding window
            if right-left+1 == len(needle):
                #then we need to check if the word in the window is equal to the needle
                if haystack[left:right+1] == needle:
                    #return the left pointer
                    return left
                #if its not the needle we move the left pointer to initiate moving the window
                left+=1
            #if its not equal to the length of the needle then we need to increase our window size
            right+=1
        return -1

        