import random
Index = int(10)
List = [0] * Index

for i in range(Index):
    List[i] = random.randint(0,99)

print(List)

SearchItem = input("Enter search data: ")

for i in range(Index):
    if SearchItem == List[i]:
        DataIndex = i
        Found = True
    else:
        Found = False

print(List)

if Found == True:
    print("Data was found at index: " ,DataIndex)
else:
    print("Data was not found")
