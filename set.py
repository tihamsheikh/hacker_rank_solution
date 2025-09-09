# # s = set("hello")
# # print(s.symmetric_difference("owl"))

# # print(s.symmetric_difference(set(['o', 'w', 'l'])))

# # print(s.symmetric_difference(['o', 'w', 'l']))

# # print(s.symmetric_difference(enumerate(['o', 'w', 'l'])))

# # print(s.symmetric_difference({"owl":1}))

# # print(s ^ set("owl"))

# # r1 = [1, 2, 3, 4 ,5, 6, 7, 8, 9]
# # r2 = [10, 1, 2, 3, 11, 21, 55, 6, 8]



# def getting_number(string):
#     count = ""
#     list = []

#     for i in string:
#         if i == " ":
#             # print(count)
#             list.append(count.strip())
#             count = ''
#         count += i
#     list.append(count.strip())

#     return list

# blank = input()
# english = input()
# english = getting_number(english)
# blank = input()
# french = input()
# french = getting_number(french)

# # print(f"{english} : {french}")
# # print(f"{set(english)} : {set(french)}")
# # print(set(english).symmetric_difference(french))
# print(len(set(english).symmetric_difference(french)))



# #--------------------------------------------------------------
# def getting_number(string):
#     count = ""
#     list = []

#     for i in string:
#         if i == " ":
#             converted = count.strip()
#             list.append(int(converted))
#             count = ''
#         count += i
#     converted = count.strip()
#     list.append(int(converted))

#     return list

# arr = input()
# values = input()

# list = set(getting_number(values))
# output = sum(list)/len(list)
# # print(list)


# print(round(output, 3))

#------------------------------------------------



