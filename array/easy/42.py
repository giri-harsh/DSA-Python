# Left Rotate the Array by One
# Input:
#  nums = [1, 2, 3, 4, 5]  
# Output:
#  [2, 3, 4, 5, 1] 



l = [1, 2, 3, 4, 5]  
temp = l[0]
n2 = []
for i in range(1,len(l)):
    n2.append(l[i])
n2.append(temp)
print(n2)
