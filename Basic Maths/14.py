n = int(input())
lastdig = []
while n>0:
    a = n%10
    lastdig.append(a)
    n= n//10
print(lastdig)
                        

     