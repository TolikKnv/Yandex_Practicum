from typing import Optional


class User:
    def __init__(
            self,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            username: Optional[str] = None,
    ):
        if not first_name and not last_name and not username:
            raise ValueError('Необходимо указать параметры пользователя')

        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    # Опишите метод класса with_name.
    @classmethod
    def with_name(cls, first, last):
        return User(first_name=first, last_name=last)

    # Опишите метод класса with_username.
    @classmethod
    def with_username(cls, nickname):
        if User.is_username_allowed(nickname):
            return User(username=nickname)
        else:
            raise ValueError('Некорректное имя пользователя')


    # Опишите статический метод класса is_username_allowed.
    @staticmethod
    def is_username_allowed(username: str):
        if username[:5]=='admin':
            return False
        else:
            return True

    # Опишите метод-свойство full_name.
    @property
    def full_name(self):
        if self.first_name is not None and self.last_name is not None:
            return f'{self.first_name} {self.last_name}'
        else:
            return f'@{self.username}'


stas = User.with_name('Стас', 'Басов')
print(stas.full_name)

# Попробуем создать пользователя с "запрещённым" именем.
ne_stas = User.with_username('admin_nestas_anonymous')