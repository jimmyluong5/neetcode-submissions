class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #so we only care about the first string
        #also create a empty result string
        result = ""
    
        for i in range(len(strs[0])):
            #then we only care about the characters from our array we create s
            for s in strs:
                #if our iterator goes out of bounds then it will result in ending the prefix only regardless of the size of our string
                if i == len(s) or s[i] != strs[0][i]:
                    return result
                #else we just add the string to our result
            result = result + s[i]
        return result