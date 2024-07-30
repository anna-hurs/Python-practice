import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous_symbols = 'il1Lo0O'
chars = ''

def check_yes_no(answer):
    while True:
        if answer.lower() == 'да':
            return True
        elif answer.lower() == 'нет':
            return False
        else:
            answer = input('Ответ неправильный, повторите: да/нет -->')

def check_digits(answer):
    while True:
        if answer.isdigit() == True:
            return answer
        else:
            answer = input('Ответ неправильный, повторите ввод числа: -->')

count_of_passwords = check_digits(input('Какое количество паролей вы хотите сгенерировать? -->').strip())
length = check_digits(input('Укажите, пожалуйста, длину одного пароля: -->').strip())
count_of_passwords = int(count_of_passwords)
length = int(length)
digits_of_passwords = check_yes_no(input(f'Включать ли цифры: "{digits}" ? (да / нет) -->').strip())
upper_of_passwords = check_yes_no(input(f'Включать ли прописные буквы "{uppercase_letters}"? (да / нет) -->').strip())
lower_of_passwords = check_yes_no(input(f'Включать ли строчные буквы "{lowercase_letters}"? (да / нет) -->').strip())
punctuation_of_passwords = check_yes_no(input(f'Включать ли символы "{punctuation}"? (да / нет) -->').strip())
ambiguous_symbols_of_passwords = check_yes_no(input(f'Исключить ли неоднозначные символы "{ambiguous_symbols}"? (да / нет) -->').strip())

if digits_of_passwords:
    chars += digits
if upper_of_passwords:
    chars += uppercase_letters
if lower_of_passwords:
    chars += lowercase_letters
if punctuation_of_passwords:
    chars += punctuation
if ambiguous_symbols_of_passwords:
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password

for _ in range(count_of_passwords):
    print(generate_password(length, chars), sep='\n')
