#   lab 8.3

#	Write lambda functions, each to find area 
#   of square, rectangle and triangle.


square=lambda a:a*a
rectangle=lambda l,b:l*b
triangle=lambda w,h:(w*h)/2
a=int(input("Enter the side of square : "))
print("Area of square : ",square(a))
l=int(input("\n  Enter the length of rectangle :"))
b=int(input("Enter the breath of rectangle : "))
print("Area",rectangle(l,b))
w=int(input("\nEnter the base of triangle : "))
h=int(input("Enter the height of triangle : "))
print("Area of triangle : ",triangle(w,h))