# sum of first n natural number 
def out (n,):
    if n ==0:
        return 0
    
    return n + out(n-1)

n = 5
sum = out(n)
print(sum)

    