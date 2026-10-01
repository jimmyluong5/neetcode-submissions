class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        #create result string
        res =""

        #then we only look at the first string because the other strings depend on the first string
        for i in range(len(strs[0])):
            #then we care about the first string
            #strs[0] gives the first string
            #we need to compare the elements of a string we create and the elements in the first string
            for s in strs:
                #if our iterating variable is at the end of the string we created, then we don't
                #add anything to our result string so just return it
                #or if our string chars don't equal the first strings characters then return res as well.
                if i == len(s) or s[i] !=strs[0][i]:
                    return res
            #if its equal then we add the character to our result, s[] is like a buffer.
            res += s[i]
        return res

