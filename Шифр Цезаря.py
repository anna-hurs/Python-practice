#На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными. Гарантируется, что между различными словами присутствует один пробел.

#Формат входных данных 
#На вход программе подается строка текста на английском языке.

#Формат выходных данных
#Программа должна вывести зашифрованный текст в соответствии с условием задачи.

#Примечание. Символы, не являющиеся английскими буквами, не изменяются.

def is_valid_int(num):
    while True:
        if num.isdigit() or (num[0] == '-' and num[1:].isdigit()):
            return int(num)
        else:
            num = input('Ввести можно только одно положительное или отрицательное число: ')
    
def is_valid_str(text):
    while text == '' or text.isspace():
        text = input("Введите хоть какой-нибудь текст! ")
    return text
    
def coder_decoder(text, k):
    alpha_en = [chr(i) for i in range(97, 123)] 
    text_Caesar = ''
    
    for i in text:
        if i.isalpha():
            k = len(i)
            text_Caesar += ' '
        else:
            new = ''
            for p in range(len(i)):
                if i[p].isalpha():
                    new += i[p]
            k = len(new)
            text_Caesar += ' '
            
        for j in range(len(i)):
            if i[j].isalpha() and i[j].lower() in alpha_en:
                if i[j].islower():
                    text_Caesar += alpha_en[(alpha_en.index(i[j]) + k) % 26]
                elif i[j].isupper():
                    text_Caesar += alpha_en[(alpha_en.index(i[j].lower()) + k) % 26].upper()
            else:
                text_Caesar += i[j]
        
            
    return text_Caesar[1:]

def start():
    
    text = is_valid_str(input()).split()
    k = 0
    print(coder_decoder(text, k))

start()
