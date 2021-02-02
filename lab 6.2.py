#   lab 6.2

#	Write a program to generate all factors of a given number.


n=int(input("Enter the number: "))
for i in range(1,n+1):
    if n%i==0:
        print(i)