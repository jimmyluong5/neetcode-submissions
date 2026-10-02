class Solution:
    def isValid(self, s: str) -> bool:
        #create a stack
        stack = []

        #if the string is odd then return False
        #because these brackets need pairs, so even length of string.
        if len(s) %2 != 0:
            return False
        #append every character in the string to the stack
        #if the open bracket equals the top of the stack then we pop it from the stack and move on, then if the stack is empty then we can know our result
        for char in s:
            
            #check if the bracket is a open bracket then only store that
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            
            else:
                #it must be a closing bracket
                #we need to first check if the stack is empty if it is then we return false
                if len(stack) == 0:
                    return False
                
                #if not empty then we need to pair the character we currently on and check the top of the stack
                if char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    #the top of stack didn't match return False
                    return False
            #check if the length of the stack is empty if it is return true else return false
        return len(stack) == 0
            

           