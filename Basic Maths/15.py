n = 11111
rev = []
normal = []
while n >0:
    a = n%10
    rev.append(a)
    n = n//10

normal = rev.copy()
normal.reverse()
flag = True
for i in range(len(rev)):
    if rev[i] != normal[i]:
        flag = False
if flag == True:
    print("yes")
else :
    print("No")


