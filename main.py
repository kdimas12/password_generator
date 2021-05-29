import random
from string import digits, punctuation, ascii_letters


def password_gen(length, tanda_baca):
    symbols = ascii_letters + digits

    if tanda_baca == "y":
        symbols += punctuation

    return "".join(random.choice(symbols) for i in range(length))


length = int(input("How long do you wanna create? "))
tanda_baca = input("Do you wanna add punctuation?(y/n) ")

print(password_gen(length, tanda_baca))
print(ascii_letters + digits)