class CipherMaster:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def process_text(self, text, shift, is_encrypt):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        text = list(text.lower())
        if is_encrypt:
            delta = shift
        else:
            delta = (-1)*shift
        for i in range(len(text)):
            if text[i] not in self.alphabet:
                continue
            else:
                text[i] = self.alphabet[
                    (self.alphabet.index(text[i]) + delta) % len(self.alphabet)
                ]


        return "".join(text)


# Проверка:
cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))