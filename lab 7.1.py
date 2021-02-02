#   lab 7.1

#	Write a program to search an item in a given list and
#   display the number of occurrences of the given item.


n_list=[1,27,31,47,34,5,89,6,98,34,23]
x=int(input("Enter the item to search : "))
t=i=0
while i<len(n_list):
    if x==n_list[i]:
        t+=1
    i+=1
print(x," is occur ",t," times")