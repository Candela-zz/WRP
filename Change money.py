#Change money
import math
print('We have four type of coins 1,7,40 and 150 unit')
print('-------------------------------------------------------')
money=int(input('Input some change :'))
print('-------------------------------------------------------')
#find out amount of 150 unit coins
print(f'You recieved {math.floor(money/150)} coins of 150 unit')
b=money%150
#find out amount of 40 unit coins
print(f'You recieved {math.floor(b/40)} coins of 40 unit')
c=b%40
#find out amount of 7 unit coins
print(f'You recieved {math.floor(c/7)} coins of 7 unit')
#find out amount of 1 unit coins
print(f'You recieved {math.floor(c%7)} coins of 1 unit')