#   lab 8.1

#	Write a function to get a new string from a given
#   string by adding ‘Is’ to the beginning of the input string.
#   If the given string already begins with ‘Is’, return the 
#   input string unchanged.



def string(s):
    if s[:2]=="is":
        return s
    else:
        return "is "+s
    
sin=input("Enter the string : ")
sin=sin.lower()
string(sin)