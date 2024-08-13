from random import randint
class Die:
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        print(f"Die{self.sides} {randint(1,self.sides)}")

die6=Die()
die10=Die(10)
die20=Die(20)

num=0
while num<10:
    die6.roll_die()
    die10.roll_die()
    die20.roll_die()
    num+=1
