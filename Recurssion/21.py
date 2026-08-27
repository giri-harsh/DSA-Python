# Print 1 to N using recursion
def count(n,a):
    if n == 0 :
        return
    
    print(a)
    return count(n-1,a+1)
n = 5
a = 0
count(n,a)
