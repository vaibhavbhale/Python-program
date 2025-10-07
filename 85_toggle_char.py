s = input("Enter a string: ")

toggled = ""
for ch in s:
    if ch.islower():
      toggled += ch.upper()
    elif ch.isupper():
        toggled += ch.lower()
    else:
        toggled += ch  

print("Toggled string:", toggled)
