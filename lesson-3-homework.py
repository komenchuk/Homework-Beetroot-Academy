# Task 1
s = 'komenchukoleh'
h = s[:2] + s[11:]
print(h)

a = 'my'
print((a[:] + a[:]))

x = 'x'
print(x[1:])

# Task 2


# Task 3
import random

gamer_attempt = 0

s = int(random.uniform(1, 10))
while gamer_attempt < 6:

    print('Как ты думаешь, какое число?')
    point = int(input('Я думаю, что это число: '))

    gamer_attempt = gamer_attempt + 1

    if point < s:
        print('Число больше!')

    if point > s:
        print('Число меньше!')

    if point == s:
        break

if point == s:
    gamer_attempt = str(gamer_attempt)
    print('Ты угадал число')

if point != s:
    s = str(s)
    print('Жаль, попытки закончились')

# Task 4
user_Name = 'oleh'
user_InputName = input('Здравствуйте, введите Ваше имя для идентификации: ')
s = user_InputName.lower()
if s == user_Name:
    print("Вход в систему выполнен!")
else:
    print('Неверно введеное имя')