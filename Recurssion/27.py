
# check for palindrome



ar1 = []
n = 123321
def check (n):
    if n <=0:
        return 0
    a = n%10
    ar1.append(a)
    return check(n//10) 



flag = True
def comp (ar1,ar2,i,flag):
    if i == len(ar1):
        return flag
    if ar1[i] != ar2[i]:
        flag = False
        return flag
    return comp(ar1,ar2,i+1,flag)    


check(n)
ar2 = ar1.copy()
ar2.reverse()
flag = comp(ar1,ar2,0,flag)
if flag == True:
    print("Yes")
else :
    print("No")