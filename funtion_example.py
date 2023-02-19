##Function
def difference(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    sub = num1 - num2
    return sub

##main program

num1 = input('Enter number 1: ')
num2 = input('Enter number 2: ')
sub = difference(num1,num2)
print('the difference is: ', sub)
