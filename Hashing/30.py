l = [10, 5, 10, 15, 10, 5]

freq = {}

for i in l:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

h_freq = 0
h_ele = 0

l_freq = float('inf')
l_ele = 0

for i in freq:
    if freq[i] > h_freq:
        h_freq = freq[i]
        h_ele = i

    if freq[i] < l_freq:
        l_freq = freq[i]
        l_ele = i

print(h_ele)
print(l_ele)