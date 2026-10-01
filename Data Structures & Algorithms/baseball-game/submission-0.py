class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #create an empty stack
        stack = []

        #if we have a C, we need to pop it out of our stack, if we have D we just double whatever we appended to our stack

        #in the code we can check if its a operation or not, it is isn't then its an integer
        #we need to loop through the operations string
        for op in operations:
            if op == "+":
                #we need to add the two previous values in our stack
                
                #we can get the last value by doing stack[-1] or len(stack)-2
                #and 2nd last value by doing stack[-2] or len(stack)-2
                stack.append(stack[-1] + stack[-2]) #then we append these to the end/top of the stack  
            elif op == "D":
                #double the previous score which is the top of the stack
                stack.append(2*stack[-1])
            elif op == "C":
                stack.pop() 
            else: #its an integer here
            #here we just need to sum up all the elements then return it
        #there are guaranteed to be operations so nothing here
                #after then our op is an integer but you must convert the string to integer
                stack.append(int(op))
        return sum(stack) #return the sum in the stack.
