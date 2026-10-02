class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #create a stack 
        st = []

        #loop through the stack
        for op in operations:
            #if the character is equal to +
            #we just add the previous values together and append to the stack
            if op == '+':
                st.append(st[-1]+st[-2])
            elif op == 'D':
                #double the previous value
                st.append(2*st[-1])
            elif op == 'C':
                st.pop() #just pop the previous value
            else:
                #we just append the value to the stack, but it must be an integer
                st.append(int(op))
            
        return sum(st) #returns the sum of the stack

        