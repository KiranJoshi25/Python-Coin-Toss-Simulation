from random import randint

i = int(input('enter how many times coin to be tossed'))
count1 = 0
count2 = 0

for res in range(i):
	res = randint(0,1)

	if res == 1:

		count1 = count1 +1
	else:
	
		count2 = count2 +1
print('No of heads')
print(count1)

print('No of tails')
print(count2)

count1 = (count1/i)*100
count2 = (count2/i)*100

print('probablity of getting head')
print(count1)

print('probablity of getting tails')
print(count2)
