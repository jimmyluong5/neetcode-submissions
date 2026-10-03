class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #keep track of duplicates using hashset
        map = set()

        left = 0
        right = 0
        res = 0
        while right < len(s):
            #need to check for duplicates
            while s[right] in map:
                #then we have a duplicate and need to shrink the window and         remove from it from the set, and move left pointer
                map.remove(s[left])
                left+=1
            #if not in map we add it to the hashset
            map.add(s[right])
            #determine the max length of a substring
            res = max(res, right-left+1)
            #move right pointer
            right+=1
        return res
