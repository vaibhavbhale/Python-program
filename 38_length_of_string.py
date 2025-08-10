def string_len(len):
    if len == "":
        return 0
    return 1 + string_len(len[1:])

str = input("Enter the string:")
print("Length of string:",string_len(str))