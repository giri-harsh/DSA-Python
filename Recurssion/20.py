def repeat(n,a):
    if n == 0:
        return
    print(a," ")

    return repeat(n-1,a)

a = "harsh"
n = 5
repeat(n,a)