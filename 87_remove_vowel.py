str = input("Enter the characters: ")
rem_vowel_count = 0
result = ""

for char in str:
    if char.lower() in 'aeiou': 
        rem_vowel_count += 1
    else:
        result += char  
        
if rem_vowel_count == 0:
    print("No vowels found")
else:
    print(f"String after removing vowels: {result}")
    print(f"Number of vowels removed: {rem_vowel_count}")
