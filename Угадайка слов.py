import random
word_list = ['суббота', 'заяц', 'морковь', 'ворона', 'воробей', 'солнце', 'работа', 'аккорд', 'хоккей', 'маяк', 'фигура', 'йогурт', 'корова', 'собака', 'легенда', 'салют', 'корзина']
def get_word():
    return random.choice(word_list).upper()
#get_word()
def display_hangman(tries): # тут функция нормально не переносится, поэтому я ее запишу просто названием
    def again_game(answer):
        if answer == 'да':
             play(get_word())
        elif answer == 'нет':
        print('Спасибо за игру!')
        else:
        answer = input('Ответ не соответствует предложенным вариантам, напишите "да" или "нет"')
def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()
def check_yes_no(answer):
    if answer.isalpha():
        return answer
    else:
        answer = input('Похоже, что вы ввели не букву или слово, а что-то другое. Поопробуйте еще раз: ')
 
def play(word):
    word = get_word()
    word_completion = '_ ' * len(word) # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False # сигнальная метка
    guessed_letters = [] # список уже названных букв
    guessed_words = [] # список уже названных слов
    tries = 6 # количество попыток
 
print('Давайте играть в угадайку слов!')
#print(word)
print(display_hangman(tries))
print(word_completion)
print()
 
while True: #and tries != 0:
    word_input = check_yes_no(input('Введите букву или полностью слово, которое загадано: ').upper())
#print(word_input)
    if word_input in guessed_letters or word_input in guessed_words:
        print('Уже было')
        continue
    if len(word_input) > 1:
        if word_input == word:
            print(f'Поздравляем, вы угадали загаданное слово: {word}! Вы победили!')
            break
        else:
            guessed_words.append(word_input)
            tries -= 1
            print(f'Не верно, осталось попыток: {tries}')
print(display_hangman(tries))
print_word(word, guessed_letters)
if tries == 0:
    print(f'Загаданное слово: {word}. Кол-во попыток исчерпало себя, попробуй еще раз сыграть)')
    again_game(input('Хотите сыграть еще? Напишите "да" или "нет"'))
    break
continue
 
if word_input in word:
    guessed_letters.append(word_input)
for c in word:
    if c not in guessed_letters:
    print('Вы угадали букву, идем дальше')
    print_word(word, guessed_letters)
    guessed = False
    break
    guessed = True
if guessed:
    print_word(word, guessed_letters)
    print('Поздравляем, вы угадали слово! Вы победили!')
    again_game(input('Хотите сыграть еще? Напишите "да" или "нет"'))
    break
else:
    guessed_letters.append(word_input)
    tries -= 1
    print(f'Не верно, осталось попыток: {tries}')
    print(display_hangman(tries))
    print_word(word, guessed_letters)
if tries == 0:
    print(f'Загаданное слово: {word}. Кол-во попыток исчерпало себя, попробуй еще раз сыграть)')
    again_game(input('Хотите сыграть еще? Напишите "да" или "нет"'))
    break
 
play(get_word())
