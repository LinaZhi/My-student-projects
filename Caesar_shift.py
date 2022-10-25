# eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
# eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
# rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

text = input('Введите текст: ')


def val_dir(s):
    if s in 'з' or s in 'р':
        return True
    return False


def val_lang(s):
    if s in 'р' or s in 'а':
        return True
    return False


def val_key(n):
    if str(n).isdigit():
        return True
    return False


print("Нужно зашифровать или расшифровать текст?")
direction = input('"з" - зашифровать, "р" - расшифровать: ').lower()
while val_dir(direction) != True:
    direction = input('Выберете "з" или "р": ').lower()
print("На каком языке текст?")
language = input('"р" - русский, "а" - английский: ').lower()
while val_lang(language) != True:
    language = input('Выберете "р" или "а": ').lower()
key = int(input('Величина сдвига вправо: '))
while val_key(key) != True:
    key = int(input('Укажите одну цифру: '))


# зашифровка
def eng_encryption():
    for i in text:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            if ord(i) + key > 122:
                print(chr((ord(i) - (26 - key))), end='')
            else:
                print(chr(ord(i) + key), end='')
        elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if ord(i) + key > 90:
                print(chr((ord(i) - (26 - key))), end='')
            else:
                print(chr(ord(i) + key), end='')
        else:
            print(i, end='')


def rus_encryption():
    for i in text:
        if i in "абвгдежзийклмнопрстуфхцчшщъыьэюя":
            if ord(i) + key > 1103:
                print(chr((ord(i) - (32 - key))), end='')
            else:
                print(chr(ord(i) + key), end='')
        elif i in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
            if ord(i) + key > 1071:
                print(chr((ord(i) - (32 - key))), end='')
            else:
                print(chr(ord(i) + key), end='')
        else:
            print(i, end='')


# расшифровка
def eng_decryption():
    for i in text:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            if ord(i) - key < 97:
                print(chr((ord(i) + (26 - key))), end='')
            else:
                print(chr(ord(i) - key), end='')
        elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if ord(i) - key < 65:
                print(chr((ord(i) + (26 - key))), end='')
            else:
                print(chr(ord(i) - key), end='')
        else:
            print(i, end='')


def rus_decryption():
    for i in text:
        if i in "абвгдежзийклмнопрстуфхцчшщъыьэюя":
            if ord(i) - key < 1072:
                print(chr((ord(i) + (32 - key))), end='')
            else:
                print(chr(ord(i) - key), end='')
        elif i in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
            if ord(i) - key < 1040:
                print(chr((ord(i) + (32 - key))), end='')
            else:
                print(chr(ord(i) - key), end='')
        else:
            print(i, end='')


if direction == "з":
    if language == "а":
        eng_encryption()
    else:
        rus_encryption()
elif direction == "р":
    if language == "а":
        eng_decryption()
    else:
        rus_decryption()

# Перебрать все варианты
# text = "Hawnj pk swhg xabkna ukq nqj."
# for k in range(25):
#     eng_decryption(k)
#     print()