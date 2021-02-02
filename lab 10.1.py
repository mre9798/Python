#  lab 10.1

#  Write a program to demonstrate ZeroDivisionError and ValueError



try:
    x=int(input("Enter a number : "))
    y=0
    print(x,'/',y,'=',x/y)
except(ZeroDivisionError,ValueError)as e:
    print(e)
else:
    print('division successful')