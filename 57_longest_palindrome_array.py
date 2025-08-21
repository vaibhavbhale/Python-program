arr=list(map(int, input("Enter the elements :").split()))
pal=[]

for num in arr:
    if str(num) == str(num)[::-1]:
        pal.append(num) 
if pal:
 longest_palindrome= max(pal)
 print("longest_palindrome is",longest_palindrome)
else:
   print("Palindrome not found")