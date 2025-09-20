
string = """HackerRank.com presents "Pythonist 2"."""
new_string = ""

for i in string:
    unicode = ord(i)
    # if (unicode >= 65 and unicode <= 90) or (unicode >= 97 and unicode <= 122):
    #     print(i)

    if (unicode >= 65 and unicode <= 90):
        new_string += chr(unicode+32)
    elif (unicode >= 97 and unicode <= 122):
        new_string += chr(unicode-32)
    else:
        new_string += i

print(new_string)
