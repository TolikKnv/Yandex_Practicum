class CipherMaster:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        original_text = list(original_text.lower())
        for i in range(len(original_text)):
            if original_text[i] not in self.alphabet:
                continue
            else:
                original_text[i] = self.alphabet[
                    (self.alphabet.index(original_text[i]) + shift) % len(self.alphabet)
                ]

        return "".join(original_text)

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        original_text = list(cipher_text.lower())
        for i in range(len(original_text)):
            if original_text[i] not in self.alphabet:
                continue
            else:
                original_text[i] = self.alphabet[
                    (self.alphabet.index(original_text[i]) - shift) % len(self.alphabet)
                ]

        return "".join(original_text)


cipher_master = CipherMaster()
print(
    cipher_master.cipher(
        original_text="Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь",
        shift=2,
    )
)
print(
    cipher_master.decipher(
        cipher_text="Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ", shift=4
    )
)
