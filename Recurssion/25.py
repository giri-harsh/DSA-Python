# factorial
# 5! = 5*4*3*2*1
# fact = fact(n-1)*fact(n-2)


def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
n = 5
ans = fact(n)
print(ans)
    


