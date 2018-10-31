'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import math
# Write your code here
n = input()
a = n.split(' ')
result = ""

def checkPrimeNumber(c):
    flag = 0
    if(c==2):
        return True
    if(c%2 == 0 or c == 1):
        return False
        
    for i in range(3,int(math.sqrt(c))+1,2):  
        if(int(c)%i == 0):
            return False
    
    return True
    

for c in range(int(a[0]),int(a[1]) + 1):
    x=c
    if(checkPrimeNumber(c)):
        sum1 = 0
        while x != 0:
            c0 = int(x%10)
            x = int(x/10)
            sum1 = sum1 + c0
        
        if(checkPrimeNumber(sum1)):
            result = result + ' ' + str(c)

print(result)