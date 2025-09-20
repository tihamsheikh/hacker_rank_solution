# n = input()
# ls = list(map(int, input().split()))

# tmp = None
# ls.sort()
# num = ls[-1]

# for i in range(len(ls)-1, 0, -1):
#     # print(i, ls[i])
#     if ls[i] < num:
#         print(ls[i])
#         tmp = True
#         break
#     if i == len(ls)-1 and tmp:
#         print(ls[0]) 

ls = [6]
if len(ls) == 1: print(ls[0])
process = {*ls}
process = sorted(process)
print(process[-1])
size = len(process)

i = 1
for item in process:
    if i == size-1:
        print(item)
        break
    i += 1

    
    
