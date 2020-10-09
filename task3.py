import random, math

myNumber = math.floor(random.random()*100)
flag = True
print(myNumber)

while flag:
    print('I made up a number from 1 to 100, can you guess it?')
    number = input("enter number: ")
    if number.isdigit():
        dNumber = int(number)
        if dNumber in range(1, 101):
            if dNumber < myNumber: print('my number is bigger')
            elif dNumber > myNumber: print('my number is smaller')
            else: 
                flag = False
                print('Congratulations! You guess the number!')
        else: print('Number should be greater than 0 and less than 101')
    else: print('Number should be integer')