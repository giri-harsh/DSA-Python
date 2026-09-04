    # Find Second Smallest and Second Largest Element in an array


# 43

# Problem Statement:
#  Given an array, find the second smallest and second largest element
#  in the array. Print ‘-1’ in the event that either of them doesn’t exis


l = [1,2,3,4,5]
largest = 0
for i in l:
    if i>largest:
        largest = i
# print(largest)
largest2 = 0
for i in l :
    if i >largest2 and i <largest:
        largest2 = i
print(largest2)

