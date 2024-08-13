from random import randint,choice


lottery_ticket=[1,3,4,56,7,89,0,12,31,2,'d','a','c','e','o']

winning_numbers=[]
num=0
while num<4:
    item=choice(lottery_ticket)
    winning_numbers.append(item)
    num+=1

print(f'中奖号码是 {winning_numbers}')