#   lab 10.3

#	Write a custom exception which is raised if
#   user entered login credentials remain invalid.



class login(Exception):pass
try:
    name=input("Username : ")
    word=input("Password : ")
    x="username"
    y="password"
    if name==x and word==y:
        print("successful login")
    else:
        raise login("Username or Password is worng")
except login as e:
    print(e)