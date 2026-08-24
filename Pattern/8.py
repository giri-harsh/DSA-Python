# *********
#  *******
#   *****
#    ***
#     *
n = int(input())
for i in range(n):
    # space
    for j in range(0,i):
        print(" ",end='')
        # n1
    for j in range (n,i+1,-1):
        print("*",end='')
        # n2
    for j in range(n,i,-1):
        print("*",end='')
    print(" ")



# ******** 
#  ****** 
#   **** 
#    ** 