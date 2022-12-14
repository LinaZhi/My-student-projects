from random import *


def welcome():
    print('Добро пожаловать в числовую угадайку!')
    print('Сначала решим в каком диапозоне будем угадывать.')
    global x
    x = int(input('Задайте правую границу диапозона: '))
    print(f'Введите число от 1 до {x}: ')


def is_valid(s_num):
    return s_num.isdigit() and 1 <= int(s_num) <= x


def numerical_guessing_game():
    n = randint(1, x)
    counter = 0
    user_input = ''
    while user_input != n:
        user_input = input()
        if is_valid(user_input) != True:
            print(f'А может быть все-таки введем целое число от 1 до {x}?')
            continue
        else:
            user_input = int(user_input)
        if user_input < n:
            counter += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        elif user_input > n:
            counter += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        elif user_input == n:
            counter += 1
            print('Вы угадали, поздравляем!')
            print('Количество попыток:', counter)


def end_game():
    while True:
        print('Хотите сыграть еще раз? (Да/Нет)')
        answer = input()
        if answer.lower() == 'да':
            numerical_guessing_game()
        elif answer.lower() == 'нет':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        else:
            print('Простите, я не понял, хотите ещё поиграть?')


welcome()
numerical_guessing_game()
end_game()#   M y - s t u d e n t - p r o j e c t s  
 