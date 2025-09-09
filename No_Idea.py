# first try if the duplicates in the list is accepted
# then if it is not make the list a set and 
# switch array searching in set to set searching in array

# inputs
n_m = input()     # not_important_input
arr = list(map(int, input().split()))   # array 
a = set(map(int, input().split()))  # Set A
b = set(map(int, input().split()))  # Set B

# 1st version
# def matched(a: list, arr: list):
#     count = 0
#     for i in a:
#         # print("1st: ", i)
#         if i in arr:
#             # print("2nd: ", i)
#             count += 1
#     return count

# happy_point = matched(a, arr)
# sad_point = matched(b, arr)

# print(happy_point-sad_point)

# 2nd version
def get_hash(a):
    dict_arr = {}
    for i in a:
        if i not in dict_arr:
            dict_arr[i] = 1
        else:
            dict_arr[i] += 1

    return dict_arr

def get_point(dict_a , dict_arr):
    mood = 0
    for key in dict_a:
        if key in dict_arr:
            # print(key, dict_arr[key])
            mood += dict_arr[key]
    return mood

dict_arr = get_hash(arr)


happy = get_point(a, dict_arr)
sad = get_point(b, dict_arr)

print(happy - sad)