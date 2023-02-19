import random as rand

list_ = 'QWERTYUIOPASDFGHJKLZXCVBNM' + '1234567890' + '!@#$%^&*()'+ 'qwertyuiopasdfghjklzxcvbnm' + '[]{}:;<,>>?/~`|\''
list_1 =list(list_)
password = []
length = int(input('Enter the lenght of the character: '))

while length <=8:
    print('Lenght must be greater than 8!')
    length = int(input('Re-enter the length of the character: '))

for i in range(length):
    password.append(rand.choice(list_1))

return_password = ''.join(password)

def get_passwd():
    return return_password


print(get_passwd())
