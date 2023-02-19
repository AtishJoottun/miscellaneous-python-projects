import random

index = int(10)
array = [0] * index
n = int(index - 1)

#Start of procedure
def generateNumber():
    for i in range(index):
        array[i] = random.randint(1,100)
#End Of Procedure

#Start of procedure
def sort():
    global n
    for i in range(index - 1):
        for j in range(n):

            if  array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[ j + 1] = temp

        n = n - 1
#End Of Procedure

###########main program###############
generateNumber()
print(array)
sort()
print(array)
