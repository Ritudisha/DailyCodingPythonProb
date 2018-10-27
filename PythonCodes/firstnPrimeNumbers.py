import math
# Write your code here
n = input()
result = ""
for c in range(2,int(n)):
    flag = 0
    for i in range(2,math.ceil(int(c)/2) +1):
        if(int(c)%i == 0):
            flag = 1
            break
    if(flag == 0):
        result = result + " " + str(c)
        
print(result)
        