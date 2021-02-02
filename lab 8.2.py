#   lab 8.2

#	Write lambda functions:
#   (a)	 To find largest of 2 numbers
#   (b)	 To check the input number is divisible by 5
#   (c)	 To remove all strings with length < 5 from a list of strings
#   (d)	 To increment a list of integers by 10% if the number
#        is greater than 1000 else by 5%.



l=lambda a,b:max(a,b)
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
print("Largest number is",l(a,b))

result=lambda a:"number can divide by 5" if a%5==0 else "number is not divide by 5"
a=int(input("Enter any number  : "))
print(result(a))

str=["python","is","a","simple","program",]
str1=list(filter(lambda a:len(a)>5,str))
print(str1)

num=[200,500,1500,2000,120]
num1=list(map(lambda x:x+x*0.1 if x>1000 else x+x*.05,num))
print(num1)