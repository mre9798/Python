from rectangle import *
from circle import *
from dgraphic.sphere import *
from dgraphic.cuboid import *
rl=int(input("Enter the length of rectangle : "))
rb=int(input("Enter the breath : "))
print('\nArea of rectangle : ',rectarea(rl,rb))
print("Perimeter of rectangle : ",rectperimeter(rl,rb))
print('\n \n')
cr=int(input("Enter the radius of the circle : "))
print('\nArea of circle : ',cirarea(cr))
print("Perimeter of circle : ",cirperimeter(cr))
print('\n \n')
cl=int(input("Enter the length of cuboid : "))
cb=int(input("Enter the breath of cuboid : "))
ch=int(input("Enter the height of cuboid : "))
print('\nArea of cubiod :',cubarea(cl,cb,ch))
print("Perimeter of cubiod : ",cubperimeter(cl,cb,ch))
print('\n \n')
sr=int(input("Enter the radius of sphere : "))
print('\nArea of sphere : ',spherearea(sr))
print("Circumference of sphere : ",spherecircum(sr))