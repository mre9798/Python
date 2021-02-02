#   lab 7.2

#	Write a program to print all even numbers
#   from a given list in the given order until
#   you reach number 237 or end of the list.



n=[123,234,145,7,34,237,43,67]
i=0
while i<len(n):
    if n[i]==237:
        print(n[i])
        break
    else:
        if n[i]%2:
            print(n[i],end=' ')
    i+=1