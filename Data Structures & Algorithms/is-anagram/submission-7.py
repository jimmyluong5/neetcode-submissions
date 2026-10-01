class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if the lengths are not the same return False
        if len(s) != len(t):
            return False
        
        #create the hashmaps
        map1 = {}
        map2 = {}

        for char in s:
            if char in map1:
                #increase the frequency
                map1[char] +=1
            else:
                #add it to the hashmap
                map1[char] = 1
        
        for char in t:
            if char in map2:
                #increase the frequency
                map2[char] +=1
            else:
                #add it to the hashmap
                map2[char] = 1

        #now that the hashmaps are populated just check over them
      
        for char in s:
            if char not in map2 or map1[char] != map2[char]:
                return False
        return True
        
        