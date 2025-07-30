''' A number whose square ends with the same number is known as an Automorphic number.
Let's try and understand it even better using an example ,

Example
Input : number = 5
Output : It's an Automorphic number.
Explanation : Number = 5
Square of number = 25
as the square of the number ends with the number itself, It's an Automorphic number.'''

number = int(input("Enter the number: "))
numsq = number * number  

if str(numsq).endswith(str(number)):
    print(f"The number {number} is automorphic")
else:
    print(f"The number {number} is not automorphic")
