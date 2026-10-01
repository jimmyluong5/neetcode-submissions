class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #create the result string
        result = ""

        #we only care about the first string because if the first string and create a comparison string s

        #first we loop through the length of the first string
        for i in range(len(strs[0])):
            
            #then we create a string s then loop through the characters of the 0th index string and see if the characters don't match, if they don't then we return our result, else if they do match then we add the characters we have seen match to result using the string we made s[i]
            #also we also need to check an edge case, if the index is out of bounds, meaning that i is outside the len(s) then we cannot have a longer prefix.
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            
            #add the character to the result
            result = result + s[i]
        return result