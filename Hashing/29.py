n = [5,3,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
freq_dict = {}
for i in n:
    if i in freq_dict:
        freq_dict[i]+=1
    else :
        freq_dict[i] = 1
print(freq_dict)        

for i in m:
    if i in freq_dict:
        print(i, "->", freq_dict[i])
    else:
        print(i, "->", 0)

        

