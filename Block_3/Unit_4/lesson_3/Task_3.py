# Пропишите нужные импорты.
from decimal import Decimal, getcontext


# Напишите код функции.
def get_monthly_payment(credit_sum, month, bank_percent):
    # Банк делит названную сумму на названное количество месяцев
    # и увеличивает ежемесячный платёж на оговоренный процент.
    getcontext().prec = 3
    sum_without_percent = Decimal(str(credit_sum)) / Decimal(str(month))
    percent = Decimal("1") + Decimal(str(bank_percent / 100))
    result = Decimal(str(sum_without_percent)) * Decimal(str(percent))
    # Функция должна вернуть сумму ежемесячного платежа по кредиту.
    return result


# Вызовите функцию get_monthly_payment()
# с указанными в задании аргументами
# и распечатайте нужное сообщение.
print(f"Ежемесячный платёж: {get_monthly_payment(54, 24, 9)} ВтК")
