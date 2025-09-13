operations = ["insert", "print", "remove", "append", "sort", "pop", "reverse"]

list = []

command_size = int(input())

for i in range(command_size):
    command = input().split()

    if command[0] == operations[0]: # insert
        value = int(command[-1])
        index = int(command[1])
        
        list.insert(index, value)
        # if index+1 > len(list):
        #     list.append(value)
        #     continue
        # list[index] = value

    elif command[0] == operations[1]: # print
        print(list)

    elif command[0] == operations[2]: # remove 
        value = int(command[-1])

        if list != []:
            list.remove(value)

    elif command[0] == operations[3]: # append
        value = int(command[-1])
        list.append(value)

    elif command[0] == operations[4]: # sort
        list.sort()

    elif command[0] == operations[6]: # reverse
        list = list[::-1]

    elif command[0] == operations[5]: # pop
        if list != []:
            list.pop()
    




