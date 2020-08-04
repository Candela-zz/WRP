print('Find amount of prime number : Press 1')
print('Check prime number : Press 2')
print('-------------------------------------------------------')

press =input('Press 1 or 2 :')
if press =='1':
	#Find amout of prime number
	number=int(input('Input the largest number : '))
	e=0
	if number>1 :
		for x in range (2,number+1) :
			count=0
			for y in range (1,x+1):
				if (x%y)==0 :
					count+=1
			if count==2 :
				print(x)
				e+=1
			if x == number :
				print(f'Amount of prime number are {e}')

	else :
		print('1 is not a prime number')
		print('Please input one more time')

	
if press =='2':
	#Check a prime number
	number=int(input('Input number that you want to check :'))
	for i in range (2,number):
		if(number%i)==0 :
			print('This number is not a prime number')
		else :
			print('This number is a prime number')



