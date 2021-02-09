file1=filec=False
try:
    file1=open('eldhose.txt')
    filec=open('eldhose-c.txt','w')
    line=file1.read()
    while line:
        filec.write(line)
        file1=False
        file1=open('eldhose-c.txt')
        line=file1.readline()
    print(filec)
except IOError as er:
    print(er)
finally:
    if file1:
        file1.close()
    if filec:
        filec.close()
        