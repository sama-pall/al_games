# Это игра по угадыванию чисел.
import random


def ending(num):
    '''
    формирует окончание в зависимости от числа попыток
    '''
    if num + 1 == 1:
        return 'y'
    elif num + 1 > 4:
        return 'ок'
    else:
        return 'и'


def gender(name):
    '''
    формирует окончание глагола в зависимости от пола
    '''
    if name.endswith('а') or name.endswith('я'):
        return 'ась'
    return 'ся'


guessesTaken = 0

myName = input('Привет! Как тебя зовут(полное имя)? ')

number = random.randint(1, 20)
print('Что ж, ' + myName + ', я загадал число от 1 до 20.')

for guessesTaken in range(6):
    print('Попробуй угадать.')
    guess = int(input())

    if guess < number:
        print("Твое число слишком маленькое.")
    elif guess > number:
        print("Твое число слишком большое.")
    else:
        break

if guess == number:
    print(f'Отлично, {myName}! Ты справил' + gender(myName) + f' за {guessesTaken + 1} попытк' + ending(
        guessesTaken) + '!')
elif guess != number:
    print(f'Увы. Я загадала чилсло {number}.')
