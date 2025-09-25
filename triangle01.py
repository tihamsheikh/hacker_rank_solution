
n = int(input("Size of your pyramid: "))

for i in range(n):
    for j in range(i):
        print("*", end="")
    print("*")