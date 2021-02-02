#    lab 6.4

#	Accept a list of integers from user. For all values above
#   100 store the string ‘Over’ in the specific position.


l=input("Enter list of  numbers : ")
l=[int(n) for n in l.split()]
j=0
for i in l:
    if i>100:
        l[j]='Over'
    j+=1
print(l)