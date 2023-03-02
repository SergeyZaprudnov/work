import requests
import datetime


def load_json():
    data = requests.get(
        'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14'
        '-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677859516841'
        '&signature=YQtAJMU5SU7Wr8KqsECbdnY4x85Ck_Z-9KDS4AEDF8k&downloadName=operations.json')
    data_word = data.json()
    return data_word


def state_executed():
    executed_data = load_json()
    list_executed = []
    for i in executed_data:
        if not i:
            continue
        else:
            if i['state'] == "EXECUTED":
                list_executed.append(i)
    return list_executed


def sort_by_date():
    executed_operations = state_executed()
    sorting = sorted(executed_operations, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
                     reverse=True)
    return sorting


def last_five():
    sorting_list = sort_by_date()
    return sorting_list[:5]


def disguise_card(transactions):
    for i in transactions:
        if 'перевод' in i['description'].lower():
            if 'счет' in i['from'].lower():
                i['from'] = i['from'][:(len(i['from']) - 4) - 10] + '*' * 6 + i['from'][(len(i['from']) - 4):]
            i['from'] = i['from'][:(len(i['from']) - 4) - 6] + '*' * 6 + i['from'][(len(i['from']) - 4):]
        i['to'] = i['to'][:(len(i['to']) - 4) - 16] + '*' * 2 + i['to'][(len(i['to']) - 4):]
    return transactions


def date_format_change(transactions):
    disguise_card(transactions)
    for i in transactions:
        i['date'] = (datetime.datetime.strptime(i['date'], "%Y-%m-%dT%H:%M:%S.%f")).strftime("%d.%m.%Y")
    return transactions


def output(transactions):
    for i in transactions:
        if 'Открытие вклада' in i['description']:
            print(f"{i['date']} {i['description']}\n"
                  f"{i['to']}\n"
                  f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
            print()
        elif 'Перевод со счета на счет' or 'Перевод организации' or 'Перевод с карты на карту' in i['description']:
            print(f"{i['date']} {i['description']}\n"
                  f"{i['from']} -> {i['to']}\n"
                  f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
            print()


def main():
    output(last_five())
