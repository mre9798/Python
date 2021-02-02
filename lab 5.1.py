# lab5.1
#  Write python program to find factorial of a number.

n=int(input("Enter the number for factorial:"))
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial :",fact)