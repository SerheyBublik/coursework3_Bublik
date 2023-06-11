import json


def convert_date(date):
    """

    :param date:
    :return:

    example 2019-12-07T06:17:14.634890 -> 07.12.2019
    """
    return '.'.join(date[:10].split('-')[::-1])


def masking_card(card_info):
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
    out = f"""{convert_date(operation['date'])} Перевод организации
     {masking_card(operation['from'])} -> {masking_card(operation['to'])}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}руб."""

    print(out)


def main():
    with open('data/operations.json', mode='r', encoding='utf8') as file:
        data = json.load(file)

    data = filter(lambda x: (x.get('state') == "EXECUTED" and x.get('from')), data)
    data = sorted(data, key=lambda x: x.get('date'), reverse=True)

    for operation in data[:5]:
        print(show_operation(operation))


main()