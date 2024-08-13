from random import randint,choice


lottery_ticket=[1,3,4,56,7,89,0,12,31,2,'d','a','c','e','o']
winning_numbers=[31, 'c', 4, 12]

active=True
num=0
while active:
    my_ticket=[]
    item=choice(lottery_ticket)
    my_ticket.append(item)
    item=choice(lottery_ticket)
    my_ticket.append(item)
    item=choice(lottery_ticket)
    my_ticket.append(item)
    item=choice(lottery_ticket)
    my_ticket.append(item)
    num+=1
    print(f'第 {num} 次 买彩票 {my_ticket}')
    if my_ticket[0]==winning_numbers[0] and my_ticket[1]==winning_numbers[1] and my_ticket[2]==winning_numbers[2] and my_ticket[3]==winning_numbers[3]:
        active=False

print(f'中奖了,买了 {num} 次彩票')