import json
from json import JSONDecodeError

PATH = 'data/operations.json'


def convert_date(date):
    """
    Дата перевода представлена в формате ДД.ММ.ГГГГ
    example 2019-12-07T06:17:14.634890 -> 07.12.2019
    """
    return '.'.join(date[:10].split('-')[::-1])


def masking_card(card_info):
    """
    - Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
- Номер счета замаскирован и не отображается целиком в формате  **XXXX
(видны только последние 4 цифры номера счета).
    """
    card_info = card_info.split()
    number = card_info[-1]
    if len(number) == 16:
        hide_number = number[:4] + " " + number[5:6] + "** **** " + number[-4:]
    elif len(number) == 20:
        hide_number = "**" + number[-4:]
    else:
        hide_number = "the number is not correct"

    return f'{" ".join(card_info[:-1])} {hide_number}'


def show_operation(operation):
    """
    выводит  операци в формате:
    <дата перевода> <описание перевода>
<откуда> -> <куда>
<сумма перевода> <валюта>
# Пример вывода для одной операции:
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
    """
    out = f"""{convert_date(operation['date'])} Перевод организации
     {masking_card(operation['from'])} -> {masking_card(operation['to'])}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}.
"""

    print(out)


def main():
    """
    Открывает файл, выбирает "EXECUTED" операции, сортирует по дате, выбирает 5 последних
    :return: show_operation(operation)
    """
    try:
        with open(PATH, mode='r', encoding='utf8') as file:
            data = json.load(file)

            data = filter(lambda x: (x.get('state') == "EXECUTED" and x.get('from')), data)
            data = sorted(data, key=lambda x: x.get('date'), reverse=True)

            for operation in data[:5]:
                print(show_operation(operation))
    except FileNotFoundError:
        print("Файл не открывается")
    except JSONDecodeError:
        print("Файл не удается преобразовать")


#

if __name__ == '__main__':
    main()
