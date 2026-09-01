# Print Fibonacci Series up to Nth term


# 9

# Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.


def fib(n):
    if n <=0 :
        return 0
    if n == 1:
        return 1
    
    return fib(n-1)+fib(n-2)

for i in range(6):
    print(fib(i))
    
