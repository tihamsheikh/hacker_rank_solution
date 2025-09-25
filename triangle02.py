
n = 5

# *****
# ****
# ***
# **
# *

for i in range(n):
    for j in range(n, i, -1):
        print("*", end="")

    print()

# 01234
# 0123
# 012
# 01
# 0

for i in range(n):
    for j in range(n-i):
        print(j, end="")
    
    print()


