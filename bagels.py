import random

NUM_DIGITS = 3
MAX_GUESS = 10


def get_secret_num():
    # Возвращает строку уникальных случайных цифр, длина которой составляет NUM_DIGITS.
    numbers = list(range(10))
    random.shuffle(numbers)
    s_num = ''
    for i in range(NUM_DIGITS):
        s_num += str(numbers[i])
    return s_num


def get_clues(g_uess, s_num):
    # Возвращает строку с подсказками пользователю "Тепло", "Горячо" и "Холодно"
    if g_uess == s_num:
        return 'Вы угадали!'

    clues = []
    for i in range(len(g_uess)):
        if g_uess[i] == s_num[i]:
            clues.append('Горячо')
        elif g_uess[i] in s_num:
            clues.append('Тепло')
    if len(clues) == 0:
        return 'Холодно'

#    clues.sort()
    return ' '.join(clues)


def is_only_digits(num):
    # Возвращает значение True, если num - строка, состоящая только из цифр. В противном случае возвращает False.
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True


print('Я загадаю %s-х значное число, которое вы должны отгадать.' % NUM_DIGITS)
print('Я дам несколько подсказок...')
print('Когда я говорю:\tЭто означает:')
print(' Холодно\tНи одна цифра не отгадана.')
print(' Тепло\tОдна цифра отгадана, но не отгадана ее позиция.')
print(' Горячо\tОдна цифра и ее позиция отгаданы.')

while True:
    secret_num = get_secret_num()
    print('Итак, я загадал число. У вас есть %s попыток, чтобы отгадать его.' % MAX_GUESS)
    guesses_taken = 1
    while guesses_taken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not is_only_digits(guess):
            print('Попытка №%s: ' % guesses_taken)
            guess = input()
        
        print(get_clues(guess, secret_num))
        guesses_taken += 1

        if guess == secret_num:
            break
        if guesses_taken > MAX_GUESS:
            print('Попыток больше не осталось. Я загадал число %s.' % secret_num)

    print('Хотите сыграть еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break
