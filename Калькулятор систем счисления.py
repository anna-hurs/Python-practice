#BOH*
#На вход программе подается натуральное число в десятичной системе счисления. Напишите программу, которая переводит его в двоичную, восьмеричную и шестнадцатеричную системы счисления.

#Формат входных данных 
#На вход программе подается натуральное число.

#Формат выходных данных
#Программа должна вывести текст в соответствии с условием задачи.
# * BOH = Binary, Octal, Hex.

n = int(input())

binary = bin(n)
octal = oct(n)
hex1 = hex(n)

print(binary[2:])
print(octal[2:])
print(hex1[2:].upper())
