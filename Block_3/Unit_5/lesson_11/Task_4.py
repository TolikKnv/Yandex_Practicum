def pay_bills(month, bills):
    if month % 3 == 0:
        return bills[1:-1]
    else:
        list_ = [bills[0], bills[-1]]
        return list_


# Вызов функции:
print(pay_bills(5, ["Интернет", "Коммуналка", "Телефон", "Страховка"]))
