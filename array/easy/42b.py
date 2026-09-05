# right Rotate the Array by One
# Input:
#  nums = [1, 2, 3, 4, 5]  
# Output:
#  [5, 1 ,2, 3, 4] 

l = [1, 2, 3, 4, 5]  
n = len(l)-1
temp = l[n]
l2 = []
l2.append(temp)
for i in range(n):
    l2.append(l[i])

print(l2)
