import random
num = random.randrange(1, 101)
print('Добро пожаловать в числовую угадайку')
def is_valid(text):
#Функция проверки корректности введенных данных
    return text.isdigit() and 1 <= int(text) <=100
def osnovnoy_sikl():
    flag = False
    while flag == False:
    #Основной цикл программы
        number = input('Введите число от 1 до 100 (включительно):')
        if is_valid(number):
            flag = True
            number = int(number)
            if number < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                flag = False
            elif number > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
                flag = False
            elif number == num:
                flag = True
                print('Вы угадали, поздравляем!')
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        else:
            flag = False
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
osnovnoy_sikl()
