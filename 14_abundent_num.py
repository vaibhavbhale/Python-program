'''A Number that is smaller than the sum of all it's factors except the number itself is known as an Abundant number.

Example
Input : Number = 12
Output : Yes, It's an Abundant Number
Explanation : The Factors for the number 12 are, 1, 2, 3, 4 and 6. We don't want to include the number itself.
Now the sum of the factors except the number itself is :
1 + 2 + 3 + 4 + 6 = 16
as the number 16>12 , the number itself.
It's an abundant number.'''

num=int(input("Enter the number:"))
sum=0

for i in range(2,num):
 if num % i== 0:
    sum+=i

if sum>num:
    print(num,"the number is abundent number")
else:
    print(num,"the number is not abundenty number")