class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #if they aren't the same length then they aren't valid anagrams
        if len(s) != len(t):
            return False


        #we create hashmaps and track the frequency
        map1 = {}
        map2 = {}

        #we add the elements to each hashmap then see if map1==map2?
        for char in s:
            if char in map1:
                #increase the frequency
                map1[char] +=1
            else:
                #add it to the hashmap
                map1[char] = 1
        

        #for map2
        for char in t:
            if char in map2:
                map2[char]+=1
            else:
                map2[char]=1

        return map1==map2