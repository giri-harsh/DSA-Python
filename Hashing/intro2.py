n = [5,3,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash_list = []
hash_list=[0]*11
print(hash_list)

for i in n:
    hash_list[i] +=1
for i in m:
    if i < 1 or i >10:
        print("0")
    else :
        print(hash_list[i])

