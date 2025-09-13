operations = ["discard", "remove", "pop"]

sizeof_set = input()

user_set = set(map(int, input().split()))
# print(user_set)

command_len = int(input())

for i in range(command_len):
    command = input().split()

    if command[0] == operations[0]:   # discard
        user_set.discard(int(command[-1]))

    elif command[0] == operations[1]: # remove
        if int(command[-1]) in user_set:
            user_set.remove(int(command[-1]))

    else: # pop
        user_set.pop()
        
print(sum(user_set)) # sum the set


