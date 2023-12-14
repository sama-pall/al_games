# Шифр Цезаря

SYMBOLS = 'АБВГДЕЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеежзийклмнопрстуфхцчшщъыьэюя'
MAX_KEY_SIZE = len(SYMBOLS)

def get_mode():
    while True:
        print('Вы хотите зашифровать или расшифровать или взломать текст?')
        mode = input().lower()
        if mode in ['зашифровать', 'з', 'расшифровать', 'р', 'взломать', "в"]:
            return mode
        else:
            print('Введите "зашифровать" или "з" для зашифровки или "расшифровать" или "р" для расшифровки или "в" для взлома.')

def get_message():
    return input('Введите текст: ')

def get_key():
    key = 0
    while True:
        print('Введите ключ шифрования (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if key >= 1 and key <= MAX_KEY_SIZE:
            return key


def get_translated_message(mode, message, key):
    if mode[0] == 'р':
        key = -key
    translated = ''

    for symbol in message:
        symbol_index = SYMBOLS.find(symbol)
        if symbol_index == -1:  ## Символ не найден в SYMBOLS.
            # Просто добавить этот символ без изменений
            translated += symbol 
        else:
            # Зашифровать или расшифровать
            symbol_index += key

            if symbol_index >= len(SYMBOLS):
                symbol_index -= len(SYMBOLS)
            elif symbol_index < 0:
                symbol_index += len(SYMBOLS)

            translated += SYMBOLS[symbol_index]
    return translated

mode = get_mode()
message = get_message()
if mode[0] != 'в':
    key = get_key()
print('Преобразованный текст:')
if mode[0] != 'в':
    print(get_translated_message(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, get_translated_message('расшифровать', message, key))
        
