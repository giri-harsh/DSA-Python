# Find the highest/lowest frequency element


# 30

# Problem Statement: Problem Statement: Given an array of size N. Find the highest and lowest frequency element.



# Input: array[] = {10,5,10,15,10,5};
# Output: 10 15


l = [10,5,10,15,10,5]
freq = {}
for i in l :
    if i == freq[i]:
        freq[i] +=1
    else :
        freq[i] = 1
    h_freq = 0
    h_ele = 0
    l_freq = 0
    l_ele = 9999
    
