#   lab 9.1

#	Write a recursive function to find factorial of a number.


def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the nnumber : "))
print("Factorial is ",fact(n))