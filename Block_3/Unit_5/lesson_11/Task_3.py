def is_palindrome(str):
    # Ваш код здесь
    str = str.lower()
    str = str.replace(' ', '')
    return str == str[::-1]


# Должно быть напечатано True:
print(is_palindrome('А роза упала на лапу Азора'))
# Должно быть напечатано False:
print(is_palindrome('Не палиндром'))