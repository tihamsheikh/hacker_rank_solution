#     x
#    xxx
#   xxxxx
#  xxxxxxx
# xxxxxxxxx
# xxxxxxxxx
#  xxxxxxx
#   xxxxx
#    xxx
#     x

# to note
# if i want to take 10 as a input and print 10 column (means use 1 main loop), then i rekcon, that i should n/2 in a if. 
# That contains second part and the 1st part is outside the if.

# another note
# i could just divide the n/2 and use only this. In this case both of the loops are in use. Like n = n/2 

n = int(input("The size of your diamond: "))

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



