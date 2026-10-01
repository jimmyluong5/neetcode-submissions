class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        #create res string 
        res = " " *(n+m)

        #just turn the result into array
        res = list(res)
        word1 = list(word1)
        word2 = list(word2)
        #then just add each character from each string to the result string one by one
        i=0
        j=0
        k=0
        while i < n and j < m:
            res[k] = word1[i]
            k+=1
            i+=1

            res[k] = word2[j]
            k+=1
            j+=1

        
        #if we run out of length on one of the word2 string
        #just add the rest of word1 to res
        while i < n and j == m:
            res[k] = word1[i]
            k+=1
            i+=1
        while j < m and i == n:
            res[k]=word2[j]
            j+=1
            k+=1
        
        #turn the result back into a string
        res = "".join(res)
        return res