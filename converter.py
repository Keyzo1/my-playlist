# Файл converter.py
# Автор Хулхачиев Эркен Валерьевич
# Вариант 2 Стандартный конвертер v2

def convertor():
    print('Конвертор:')
    print('Доступные системы: dec, bin, hex')
    system = input('Из какой системы счисления переводим: ')
    number = input('Введите число: ')
    if system == 'dec':
        dec = int(number)
        print(f'BIN: {bin(dec)[2:]}')
        print(f'HEX: {hex(dec)[2:]}')
    elif system == 'bin':
        dec = int(number, 2)
        print(f'DEC: {dec}')
        print(f'HEX: {hex(dec)[2:]}')
    elif system == 'hex':
        dec = int(number, 16)
        print(f'DEC: {dec}')
        print(f'BIN: {bin(dec)[2:]}')
    else:
        print('Ошибка! Используйте только: dec, bin, hex')
convertor()