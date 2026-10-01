class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #we only look at the first string

        #create result string
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                #if the string is in the list of strs
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += s[i]
        return res


