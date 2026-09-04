# array is sorted or no

l = [1,2,3,4,5]
flag = True
for i in range(len(l)-1):
    j = i+1
    if l[i] >l[j]:
        flag= False
        break

if flag == True:
    print("Sorted")
else :
    print("not sorted")