# xxxxxxxxx
#  xxxxxxx
#   xxxxx
#    xxx
#     x

n = 5


for i in range(n):
    
    for k in range(i):
        print(" ", end="")
    
    for j in range((n-i)*2-1, 0, -1):
        print("x", end="")
        
    print()
