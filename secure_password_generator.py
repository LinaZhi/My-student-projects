from random import *

chars = ''

q_count = int(input('Количество паролей для генерации: '))
q_length = int(input('Длинa одного пароля: '))

q_digit = input('Включать ли цифры? (Да/Нет) ')
q_WORD = input('Включать ли прописные буквы? (Да/Нет) ')
q_word = input('Включать ли строчные буквы? (Да/Нет) ')
q_symbol = input('Включать ли символы? (Да/Нет) ')


def Secure_Password_Generator(password):
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!# $%&*+-=?@^_.'
    count = q_length
    while count > 0:
        if q_digit.lower() == 'да':
            password += choice(digits)
            count -= 1
            if count == 0:
                break
        if q_WORD.lower() == 'да':
            password += choice(lowercase_letters)
            count -= 1
            if count == 0:
                break
        if q_word.lower() == 'да':
            password += choice(uppercase_letters)
            count -= 1
            if count == 0:
                break
        if q_symbol.lower() == 'да':
            password += choice(punctuation)
            count -= 1
    return password


def Secure_Password_Generator_without(password):
    digits = '23456789'
    lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
    punctuation = '!# $%&*+-=?@^_.'
    count = q_length
    while count > 0:
        if q_digit.lower() == 'да':
            password += choice(digits)
            count -= 1
            if count == 0:
                break
        if q_WORD.lower() == 'да':
            password += choice(lowercase_letters)
            count -= 1
            if count == 0:
                break
        if q_word.lower() == 'да':
            password += choice(uppercase_letters)
            count -= 1
            if count == 0:
                break
        if q_symbol.lower() == 'да':
            password += choice(punctuation)
            count -= 1
    return password


flag = True
while True:
    q_ambigious = input('Исключать ли неоднозначные символы (il1Lo0O)? (Да/Нет) ')
    if q_ambigious == 'да':
        for j in range(q_count):
            print(Secure_Password_Generator_without(chars))
        flag = False
        break
    elif q_ambigious == 'нет':
        for j in range(q_count):
            print(Secure_Password_Generator(chars))
        flag = False
        break
    else:
        print('Да или нет?')
        continue
