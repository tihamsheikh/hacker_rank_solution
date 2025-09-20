x = 1+1
y = 1+1
z = 1+1
n = 2

main_list = []

for i in range(x):
    print(f"i is {i}")
    for j in range(y):
        print(f"j is {j}")
        for k in range(z):
            print(f"k is {k}")
            if i+j+k == n:
                print("it was inside")
                continue
            print("got out")
            main_list.append([i,j,k])


print(main_list)


