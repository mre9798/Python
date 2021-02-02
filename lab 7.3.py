#   lab 7.3

#	Write a program to remove all odd indexed 
#   characters from a given string.



c="Paper"
c1=''
i=0
while i<len(c):
    if i%2:
        c1+=c[i]
    i+=1
print('Afer removing ',c1)