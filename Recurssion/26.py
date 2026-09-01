# rev an array
def rev(n,i):
    if i <0:
        return
    print(n[i])
    return rev(n,i-1)

n = [1,2,3,4,5]
i = len(n)-1
# print(i)
rev(n,i)