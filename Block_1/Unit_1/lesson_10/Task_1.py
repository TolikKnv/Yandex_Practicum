bash = 31
c_and_c_plus_plus = 29
c_sharp = 11
html_css = 36
java = 19
javascript = 37
sql = 34


def analyze_skills(q, w, e, r, t, y, u):
    # Среди всех переменных найдите минимальное и максимальное значение.
    # Напечатайте фразы, описанные в задании (две строки).
    mi = min(q, w, e, r, t, y, u)
    ma = max(q, w, e, r, t, y, u)
    print(f"Доля питонистов, у которых есть наименее популярный навык (в %): {mi}")
    print(f"Доля питонистов, у которых есть наиболее популярный навык (в %): {ma}")


# Не удаляйте вызов функции.
analyze_skills(bash, c_and_c_plus_plus, c_sharp, html_css, java, javascript, sql)
