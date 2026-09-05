# # Rotate array by K elements
# Input : nums = [1, 2, 3, 4, 5, 6, 7], k = 2, right
# Output : [3, 4, 5,6,7,1,2]

l = [1, 2, 3, 4, 5, 6, 7]
k = int(input("Enter K"))

temp = []
for i in range(k):
    temp.append(l[i])
print(temp)
n = len(l)
l2 = []
for i in range(k,n):
    l2.append(l[i])
l2.extend(temp)
print(l2)
