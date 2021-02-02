#   lab 5.2
# 	Write a program to generate Fibonacci series of N terms.


n=int(input("Enter the number to fibonacci series :"))
t1,t2=0,1
print('\n',t1,'\n',t2)
for i in range(t2,n-1):
    t3=t2+t1
    print('\n',t3)
    t1,t2=t2,t3