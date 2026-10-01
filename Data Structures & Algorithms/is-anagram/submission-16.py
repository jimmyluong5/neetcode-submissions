class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       #make two hashmaps and put each character in it then compare the two at the end
       #check edge case where if they are not the same length then not an anagram.

        
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}


        for char in s:
            if char in s_map:
                #increase the freq
                s_map[char] +=1
            #else add it to the map
            else:
                s_map[char] = 1
        
        for char in t:
            if char in t_map:
                t_map[char] +=1
            else:t_map[char] =1
        
        return s_map == t_map