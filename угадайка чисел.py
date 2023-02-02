import random



welcome_message = 'Добро пожаловать в числовую угадайку'
bye_message = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'



def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100

def input_nums():
    while True:
        n = input('Введите Ваше число от 1 до 100: ')
        if is_valid(n) == False:
            print('А может быть все-таки введем целое число от 1 до 100?')
        elif is_valid(n) == True:
            return int(n)

def compare_nums():
    num = random.randint(1, 100)
    counter_of_tries = 0
    while True:
        n = input_nums()
        counter_of_tries += 1
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif n == num:
            print('Вы угадали, поздравляем!')    
            break
    print('Число попыток:', counter_of_tries)
    print(bye_message)


def continue_game():
    print('Хотите сыграть ещё раз? (да/нет)')
    answer = input()
    while True:
        if answer in ('ДА', 'да'):
            return True
        elif answer in ('Нет', 'нет'):
            return False

def start_game():
    print(welcome_message)
    while True:
        compare_nums()
        if continue_game():
            continue
        else:
            break

start_game()

