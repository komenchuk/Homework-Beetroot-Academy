# Task 2
from tkinter import *
import random

# Наименование товаров
product_1 = "Milk"
product_2 = "Apple"
product_3 = "Bread"
product_4 = "Chees"
product_5 = "Rise"
product_6 = "Potato"
product_7 = "Strawberry"
product_8 = "Meat"
product_9 = "Honey"
product_10 = "Candy"

# Вывод товаров (каждый отдельно)
print(product_1)
print(product_2)
print(product_3)
print(product_4)
print(product_5)
print(product_6)
print(product_7)
print(product_8)
print(product_9)
print(product_10)

# Вывод товаров (вместе)
product_basket = (product_1, product_2, product_3, product_4, product_5, product_6, product_7, product_8, product_9, product_10)
print(product_basket, sep=", ")

# Персоны
user_1 = "Oleh"
user_2 = "Vadim"
user_3 = "Alex"
user_4 = "Andrew"
user_5 = "Sergey"

user_group = (user_1, user_2, user_3, user_4, user_5)

# Создание списка
product_list = list(product_basket)
print(product_list)

user_list = list(user_group)

# Проверка на уникальность списка продуктов и групы персон
set_product_list = set(product_list)
if len(product_list) == len(set_product_list):
    print("All elements are unique.")
else:
    print("There are the same.")

set_user_list = set(user_list)
if len(user_list) == len(user_list):
  print("All users are unique.")
else:
  print("There are identical names.")

# Количество товаров
quantity_product_1 = random.randint(1, 20)
quantity_product_2 = random.randint(1, 20)
quantity_product_3 = random.randint(1, 20)
quantity_product_4 = random.randint(1, 20)
quantity_product_5 = random.randint(1, 20)
quantity_product_6 = random.randint(1, 20)
quantity_product_7 = random.randint(1, 20)
quantity_product_8 = random.randint(1, 20)
quantity_product_9 = random.randint(1, 20)
quantity_product_10 = random.randint(1, 20)

quantity_product_basket = (quantity_product_1, quantity_product_2, quantity_product_3, quantity_product_4, quantity_product_5, quantity_product_6, quantity_product_7, quantity_product_8, quantity_product_9, quantity_product_10)
quantity_product_list = list(quantity_product_basket)
print(quantity_product_list)

# Цена товаров
price_product_1 = 30
price_product_2 = 24
price_product_3 = 20
price_product_4 = 80
price_product_5 = 35
price_product_6 = 12
price_product_7 = 20
price_product_8 = 45
price_product_9 = 100
price_product_10 = 65

price_product_basket = (price_product_1, price_product_2, price_product_3, price_product_4, price_product_5, price_product_6, price_product_7, price_product_8, price_product_9, price_product_10)
price_product_list = list(price_product_basket)
print(price_product_list)

# Вывод товаров, их количества и цены
print(product_list, quantity_product_list, price_product_list)

# Стоимость товаров
cost_product_1 = int(quantity_product_1 * price_product_1)
cost_product_2 = int(quantity_product_2 * price_product_2)
cost_product_3 = int(quantity_product_3 * price_product_3)
cost_product_4 = int(quantity_product_4 * price_product_4)
cost_product_5 = int(quantity_product_5 * price_product_5)
cost_product_6 = int(quantity_product_6 * price_product_6)
cost_product_7 = int(quantity_product_7 * price_product_7)
cost_product_8 = int(quantity_product_8 * price_product_8)
cost_product_9 = int(quantity_product_9 * price_product_9)
cost_product_10 = int(quantity_product_10 * price_product_10)

# Кошельки персон
wallet_user_1 = random.randint(1, 550)
wallet_user_2 = random.randint(1, 550)
wallet_user_3 = random.randint(1, 550)
wallet_user_4 = random.randint(1, 550)
wallet_user_5 = random.randint(1, 550)

# Выбор покупки (сделать чтобы покупатель чз инпут выбирал товары которые хочет (с существующих в базе) и в каком хочет количестве)
class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        btns = [
            "Milk", "Apple",
            "Rise", "Potato",
            "Honey", "Candy",
            "Bread", "Chees",
            "Strawberry", "Meat",
            "C"
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "Milk":
            self.formula = str((eval(self.formula)) + price_product_1)
        elif operation == "Apple":
            self.formula = str((eval(self.formula)) + price_product_2)
        elif operation == "Rise":
            self.formula = str((eval(self.formula)) + price_product_3)
        elif operation == "Potato":
            self.formula = str((eval(self.formula)) + price_product_4)
        elif operation == "Honey":
            self.formula = str((eval(self.formula)) + price_product_5)
        elif operation == "Candy":
            self.formula = str((eval(self.formula)) + price_product_6)
        elif operation == "Bread":
            self.formula = str((eval(self.formula)) + price_product_7)
        elif operation == "Chees":
            self.formula = str((eval(self.formula)) + price_product_8)
        elif operation == "Strawberry":
            self.formula = str((eval(self.formula)) + price_product_9)
        elif operation == "Meat":
            self.formula = str((eval(self.formula)) + price_product_10)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x550+200+200")
    root.title("Shopping Menu")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()

# Сдача
change_user_1 = wallet_user_1 - cost_product_1

# Покупки
if wallet_user_1 == 0:
    print(f"You don't have enough money! You only have: {wallet_user_1}")
elif wallet_user_1 < price_product_1:
    print(f"You don't have enough money! You only have: {wallet_user_1}")
elif wallet_user_1 == price_product_1:
    print("Thank you for your purchase!")
elif wallet_user_1 > price_product_1:
    print(f"Thanks for the purchase, take your remaining money!: {change_user_1}.")