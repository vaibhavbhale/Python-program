'''A perfect square is a positive integer that is obtained by multiplying an integer by itself. 
In simple words, we can say that perfect squares are numbers that are the products of integers by themselves'''

from math import sqrt

num=int(input("Enter the number:"))
if num>=0:
  sqroot=int(sqrt(num))
  sqroot*sqroot
  if sqroot*sqroot == num:
      print(f"The number {num} is a perfect square number ")
  else:
    print(f"The number {num} is  not a perfect square number ")
    
else:
    print(f"The number {num} is  not a perfect square number ")