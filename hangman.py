from random import *
import emoji

word_list = '''муравей бабуин барсук медведь бобр верблюд кошка моллюск кобра пума койот ворона олень собака осел 
утка орел хорек лиса лягушка коза гусь ястреб ящерица лама моль обезьяна лось мышь мул тритон выдра сова панда попугай 
голубь питон кролик баран крыса носорог лосось акула змея паук аист лебедь тигр жаба форель индейка черепаха ласка 
кит волк вомбат зебра'''.split()


def get_word():
    random_word = choice(word_list).upper()
    return random_word


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def valid_input(text):
    if len(text) == 0:
        return False
    for i in text:
        if i not in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
            return False
    return True


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов!')
    print('Тема - животный мир')
    print(display_hangman(tries))
    print(word_completion)

    while tries > 0:
        user_input = input('Введите букву или слово целиком: ').upper()
        while valid_input(user_input) != True:
            user_input = input('Ввод может принять только русские буквы: ').upper()
        if len(user_input) == 1:
            if user_input in word:
                ind = -1
                for i in word:
                    ind += 1
                    if i == user_input:
                        word_completion = word_completion[:ind] + user_input + word_completion[ind + 1:]
                print(word_completion)
                if '_' not in word_completion:
                    print(emoji.emojize('Поздравляем, вы угадали слово! Вы победили! :thumbs_up:'))
                    break
            elif user_input in guessed_words:
                print('Вы уже называли такую букву')
            else:
                tries -= 1
                guessed_words.append(user_input)
                print(display_hangman(tries))
                print(word_completion)
                print('Уже названные буквы: ', *guessed_words)
                print('Уже названные слова: ', *guessed_letters)
        else:
            if user_input == word:
                print(emoji.emojize('Поздравляем, вы угадали слово! Вы победили! :thumbs_up:'))
                break
            elif user_input in guessed_letters:
                print('Вы уже называли такое слово')
            else:
                tries -= 1
                guessed_letters.append(user_input)
                print(display_hangman(tries))
                print(word_completion)
                print('Уже названные буквы: ', *guessed_words)
                print('Уже названные слова: ', *guessed_letters)
    if tries == 0:
        print(emoji.emojize('Вы проиграли :cookie:'))
        print('Правильное слово -', word)


play(get_word())