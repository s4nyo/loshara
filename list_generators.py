numbers = [1, 2, 3, 4, 5, 6, 7, 8, 100]
result =[]
for number in numbers:
    if number > 5 and number < 50:
        result.append(number)
print(result)


result = filter(lambda number:number > 5 and number < 50, numbers)
print(list(result))


result1 = [number for number in numbers if number > 5 and number < 50]
print(result1)


names = ['leo', 'max', 'kate', 'mag']
NAMES = []
for i in names:
    NAMES.append(i.upper())
print(NAMES)


names = ['leo', 'max', 'kate', 'mag']
MAMES = []
for i in names:
    if i[0] == 'm':
        MAMES.append(i)
print(MAMES)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 100]
niggers =[]
for number in numbers:
    if number > 5:
       niggers.append(1)
    else:
        niggers.append(0)
print(niggers)


kvadrat = {i:i**2 for i in range(1,10)}
print(kvadrat)