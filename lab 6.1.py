#   lab 6.1

#	Generate the pattern
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *
#   * * * *
#   * * *
#   * *
#   *


n=1
for i in range(1,10):
    if i<=5:
        for j in range(i):
            print('*',end=' ')
    else:
        for j in range(i-n*2):
            print('*', end=' ')
        n+= 1
    print()