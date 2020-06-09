from random import randint

heads_count = 0
tails_count = 0

for i in range(100):

    i = randint(0,1)

    if(i == 0):
        tails_count+=1
    elif( i == 1):
        heads_count+=1

print('no of heads',heads_count,', probablity of getting Heads',heads_count/100)
print('no of tails',tails_count,', probablity of getting Tails',tails_count/100)
