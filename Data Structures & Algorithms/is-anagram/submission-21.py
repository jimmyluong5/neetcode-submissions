class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slen=len(s)
        tlen=len(t)

        #if the lengths aren't the same then they cannot be anagrams
        if slen != tlen:
            return False
        #hashmap for each string
        map1 = {}
        map2 = {}

        for char1 in s:
            if char1 in map1:
                #increase freq
                map1[char1]+=1
            #else add it to the map
            else:map1[char1]=1
        
        for char2 in t:
            if char2 in map2:
                map2[char2]+=1
            else:map2[char2]=1
        

        #then compare the frequency at the end

        return map1 == map2