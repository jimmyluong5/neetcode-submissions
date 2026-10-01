class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0 #in word1
        p2 = 0 #in word2
        p = 0 #in res

        n1 = len(word1)
        n2 = len(word2)

        res = " " * (n1+n2) #empty string then just append to this result string
        res = list(res)
        word1=list(word1)
        word2=list(word2)

        #we want to iterate through the array comparing to the length of the arrays
        
       
        while p1<n1 and p2<n2:
            res[p] = word1[p1]
            p+=1
            p1+=1

            res[p] = word2[p2]
            p2+=1
            p+=1
             
            #terminates when p1 or p2 hits n1, n2 respectively.
        if p1 == n1 and p2<n2:
            while p2<n2:
                res[p]=word2[p2]
                p2+=1
                p+=1    
        if p2 == n2 and p1<n1:
            while p1<n1:
                res[p] = word1[p1]
                p1+=1
                p+=1
                            
        res = "".join(res)
        return res

        
        
        
        
