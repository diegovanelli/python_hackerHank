import sys

class Solution:
    queuey = []
    
    def enqueueCharacter(self, s):
        self.queuey.append(s)

    def popCharacter(self):
        return self.queuey.pop()

    def dequeueCharacter(self):
        retorno = self.queuey[0]
        self.queuey.remove(retorno)
        return retorno

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    