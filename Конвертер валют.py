# Добрый день! Программа составлена Хурс Анной, почта: ania.khurs@yandex.ru
# подключаем через API актуальные данные по стоимости одной валюты по отношению к доллару
import requests


def get_online_currencies():
    host = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_NBSrzSBi5SH2Tmp8vIBuHDLyaFPmZ0PbRYI5lKOc&currencies=USD%2CEUR%2CGBP%2CRUB%2CJPY%2CBGN%2CCZK%2CDKK%2CHUF%2CPLN%2CRON%2CSEK%2CCHF%2CISK%2CNOK%2CHRK%2CTRY%2CAUD%2CBRL%2CCAD%2CCNY%2CHKD%2CIDR%2CILS%2CINR%2CKRW%2CMXN%2CMYR%2CNZD%2CPHP%2CSGD%2CTHB%2CZAR"

    response = requests.get(host)

    return response.json().get("data")


CURRENCIES = get_online_currencies()


# шапка программы (приветствие и правила прользования)
def greeting_and_description():
    print("Добро пожаловать в конвертор валют!")
    print(
        """
Данная программа поможет вам конвертировать вашу валюту в желаемую.
- выбор исходной валюты;
- ввод количества этой валюты;
- выбор валюты конвертации.
"""
    )
    count = 1
    for key in CURRENCIES.keys():
        print(f"{count} -> {key}")
        count += 1

    print()


# функции на запрос данных у пользователя
def is_current_currency():
    current_currency = input(
        "Введите имеющуюся валюту (вводите наименование валюты в том же формате, как прописано в описании): "
    )
    while current_currency.upper() not in list(CURRENCIES.keys()):
        print("Такого наименования нет в списке валют программы, попробуйте еще раз.")
        current_currency = input(
            "Введите имеющуюся валюту (вводите наименование валюты в том же формате, как прописано в описании): "
        )
    return current_currency.upper()


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_current_amount():
    while True:
        current_amount = input(
            "Введите имеющуюся сумму, которую хотите конвертировать (форма принимает только числовые значения): "
        )
        if isfloat(current_amount):
            return float(current_amount)
        else:
            print(
                "Похоже введенное значение не является цифрой, в случае десятичной дроби проверьте, чтобы стояла точка. Попробуйте ввести значение еще раз."
            )


def is_conversion_currency():
    conversion_currency = input(
        "Выберите валюту для конвертации (вводите наименование валюты в том же формате, как прописано в описании): "
    )
    while conversion_currency.upper() not in list(CURRENCIES.keys()):
        print("Похоже в наименовании ошибка, попробуйте еще раз.")
        conversion_currency = input(
            "Выберите валюту для конвертации (вводите наименование валюты в том же формате, как прописано в описании): "
        )
    return conversion_currency.upper()


# выводим результат
def conversion_result():
    # result = CURRENCIES[current_currency] / CURRENCIES[conversion_currency] * current_amount
    result = (
        current_amount / CURRENCIES[current_currency] * CURRENCIES[conversion_currency]
    )
    print(f"ИТОГО: {round(result, 2)} {conversion_currency}")


# старт программы
greeting_and_description()
while True:
    current_currency = is_current_currency()
    current_amount = is_current_amount()
    conversion_currency = is_conversion_currency()
    conversion_result()
    while True:
        answer = str(
            input(
                'Если вы хотите продолжить конфертировать валюту, напишите "y", в ином случае напишите "n": '
            )
        )
        if answer in ("y", "n"):
            break
        print("Недопустимое значение, попробуйте еще раз.")
    if answer == "y":
        continue
    else:
        print("Благодарим за выбор нашей программы! Ждем Вас снова.")
        break
