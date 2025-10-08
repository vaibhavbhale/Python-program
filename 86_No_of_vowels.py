str=input("Enter the characters:")
count=0

for i in str:
    if i== 'a' or i== 'e' or i == 'i' or i == 'o' or i== 'u' or i == 'A' or i== 'E' or i == 'I' or i == 'O' or i == 'U':
       count +=1

if count == 0:
    print('No vowels found')
else:
    print(f"Total vowels are :{count}")