def input_number():
    num1=input('please input a number')
    try:
        num1=int(num1)
        return num1
    except ValueError:
        print('you input a string, not a number')
        return None
    
num1=input_number()
while num1==None:
    num1=input_number()
num2=input_number()
while num2==None:
    num2=input_number()
print(num1+num2)