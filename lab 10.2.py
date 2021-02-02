#   lab 10.2

#	Write a program that accepts an integer from user and
#   raises ValueError with argument ‘Abnormal Condition’,
#   if the reading is not within 90 – 120.



try:
    x=int(input("Enter a integer value :"))
    if x<90 or x>120:
        raise ValueError("Abnormal Condition")
    print('Number is between 90 and 120')
except Exception as e:
    print(e)