# Task 1
name = input('Как Вас зовут? --> ')
day = input('Какой сегодня день недели? --> ')
print("Good day, " + name + "! " + day + " is a perfect day to learn some Python.")

# Task 2
nameUser = input('Как Вас зовут? --> ')
surnameUser = input('Укажите Вашу фамилию. --> ' )
day = input('Какой сегодня день недели? --> ')
print("Good day, " + nameUser + ' ' + surnameUser + "! " + day + " is a perfect day to learn some Python.")

# Task 3
print('Эта программа использует введенные Вами данные для вычесления ИМТ (индекса массы тела)')
weightUser = float(input("Какой у Вас вес тела в кг? --> "))
heightUser = float(input("Какой у Вас рост в м? --> "))
bmi = round(weightUser / (heightUser * heightUser), 2)
print('Ваш ИМТ (индекс массы тела) составляет: ', bmi)
