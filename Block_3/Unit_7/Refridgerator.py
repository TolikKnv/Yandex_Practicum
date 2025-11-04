import datetime
from decimal import Decimal

goods = {}


def add(items, title, amount, expiration_date=None):
    if expiration_date != None:
        expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d")
        expiration_date = datetime.datetime.date(expiration_date)
    if title not in items:
        items[title] = [{"amount": amount, "expiration_date": expiration_date}]
    else:
        items[title].append({"amount": amount, "expiration_date": expiration_date})


def add_by_note(items, note):
    note = list(note.split())
    title = []
    amount = Decimal('0')
    expiration_data = None
    for word in note:
        if all([item in "0123456789." for item in word]):
            amount = Decimal(word)
        elif all([item in "-0123456789" for item in word]):
            expiration_data = word
        else:
            title.append(word)
    title = " ".join(title)
    add(items, title, amount, expiration_data)


def find(items, needle):
    name_list = []
    item_keys = list(items.keys())
    for item in item_keys:
        if needle.lower() in item.lower():
            name_list.append(item)
    return name_list


def amount(items, needle):
    sum = Decimal("0")
    need_list = find(items, needle)
    for i in need_list:
        for item in items[i]:
            sum += item["amount"]
    return sum

