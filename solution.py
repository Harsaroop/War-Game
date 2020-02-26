import random

def get_guess():
    return list(input('Make a guess of the three digit number: '))

def number_generator():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return (digits[:3])

def clues_generator(x,y):

    if y==x:
        return 'Code Cracked'

    clues = []

    for ind,num in enumerate(y):
        if num == x[ind]:
            clues.append('Match')
        elif num in x:
            clues.append('Close')

    if clues == []:
        return ['Nope']
    else:
        return clues

print('Welcome to the code breaker game!')

x = number_generator()

clues_report = []

while clues_report != 'Code Cracked':
    y = get_guess()

    clues_report = clues_generator(x,y)
    print('Here is the result of your guess : ')
    for clue in clues_report:
        print(clue)
