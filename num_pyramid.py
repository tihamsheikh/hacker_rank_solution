#    1
#   121
#  12321
# 1234321


n = int(input("Size of your num pyra: "))+1

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")


    for k in range(1, i):
        print(k, end="")

    for m in range(i, 0, -1):
        print(m, end="")
        
        
        

    print()



    