import sys
#print (sys.argv[2])
k = int(sys.argv[1])
arr = map(int, sys.argv[2].split(','))
arrLen = len(arr)
flag = 0
#print(arrLen, arr)
temp = 0

sortedArr = sorted(arr)
#print(sortedArr)
j = arrLen - 1
i = 0
while i<j:
    temp = sortedArr[i] + sortedArr[j]
    if(temp == k):        
        flag = 1
        break
        
    elif(temp < k):
        i = i + 1
    else:
        j = j - 1
    #print(temp)

if(flag == 1): 
    print('True')
else:
    print('False')