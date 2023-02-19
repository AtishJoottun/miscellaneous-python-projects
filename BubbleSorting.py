import random

index = int(10)
list = [0] * index

n = index - 1
for i in range(index):
    list[i] = random.randint(1,100)

print('Unsorted')
print(list)
print('')
for j in range(index):
    for k in range(n):

        if list[k] > list[k + 1]:
            
            temp = list[k]
            list[k] = list[k + 1]
            list[k+1] = temp

    n = n - 1

print('Sorted')
print(list)

