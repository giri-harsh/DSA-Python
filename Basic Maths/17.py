n = int(input())
m = n
digit = []
count = 0
while n >0:
    a = n%10
    count = count +1
    # digit.append(a)
    n = n//10
print(count)
while m >0:
    a = m%10
    a = a**count
    digit.append(a)
    m = m//10
print(sum(digit))

