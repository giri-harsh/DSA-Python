# n to 1 
def out ( n ):
    if n == 0 :
        return
    print(n)
    return out(n-1)
n = 5
out (n)