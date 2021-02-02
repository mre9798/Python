#   lab 9.2

#	Write a recursive function to find nth term in the Fibonacci series.


def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
x=int(input("Enter the number : "))
print(x,"th term of Fibonacci series : ",fibo(x))