# Remove Duplicates
l = [1,1,2,2,2,3,3]
s = set()
for i in l :
    s.add(i)

l2 = []
for i in s:
    l2.append(i)
# print(l2)
n1 = len(l)
n2 = len(l2)
n3 = n1-n2
l3 = ["_"]*n3
# print(l3)
l2.extend(l3)
print(l2)
