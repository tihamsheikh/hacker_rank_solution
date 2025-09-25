from time import sleep

n = 0

while True:
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")


        for k in range((i*2)+1):

            print("x", end="")
            
        print()


    for i in range(n):
        
        for k in range(i):
            print(" ", end="")
        
        for j in range((n-i)*2-1, 0, -1):
            print("x", end="")
            
        print()

    print()
    sleep(1)

    n += 1