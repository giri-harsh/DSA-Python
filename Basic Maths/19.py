n = int(input())
flag = False
for i in range(2,(n//2)+1,1):
    if n%i==0:
        flag = True
        break
if flag == True:
    print("Not Prime")
else:
    print("Prime")