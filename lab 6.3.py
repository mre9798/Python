#   lab 6.3

#	Find GCD of 2 numbers.


n = int(input("Enter first number : "))
m = int(input("Enter second number : "))
if m>n:
    small = n
else:
    small = m
for i in range(1,small+1):
    if m%i==0 and n%i==0:
        gcd=i
print('GCD of %d, %d is %d'%(n,m,gcd))