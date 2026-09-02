n = [5,3,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

for i in m:
    count = 0
    for j in n:
        if i ==j:
            count +=1
    print(count) 