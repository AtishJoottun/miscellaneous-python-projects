Palindrome = input('Enter a palindrome: ')
c = len(Palindrome) - 2
a = len(Palindrome) - 1
b =True
x = int(0)

while b == True or (c<0 and (a>len(Palindrome)-1)):
        if Palindrome[a+1] == Palindrome[c - 1]:
            b = True
            c -= 1
            a +=1
        else:
            b = False


if b == True:
    print(Palindrome, " is a palindrome.")
else:
    print(Palindrome, " is not a palindrome")
