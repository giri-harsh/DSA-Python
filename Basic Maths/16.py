a = 20
b = 15
gcd = 1
min  = 1
if (a>b):
    min = a
else :
    min = b
for i in range (1,min+1):
    if a % i == 0 and b % i ==0:
        gcd = i

print(gcd)