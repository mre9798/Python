try:
    file=open('appendfile.txt','a')
    line=input("Enter a line of text : ")
    while line:
        file.write(line+"\n")
        line=input("Enter next line of text : ")
    file.close()
except IOError as er:
    print(er)