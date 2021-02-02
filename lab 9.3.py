#   lab 9.3

#	Write a recursive function to find the sum of digits of a given number.



def sum(n,s=0):
    if n==0:
        return 0
    else:
        s+=n%10
        n=n//10
        return(s+sum(n))
x=int(input("Enter the a number : "))
print("Sum : ",sum(x))