# 1/2/3/4/5
print (1, 2, 3, 4, 5, sep='/')
# First line
print ('First line', end=' ')
# Second line
print ('Second line', end='\n \n \n')
# Third line!!!
print ('Third line', end='!!!')
# Выводит справку по print
help(print)
a = 'Hello, '
# Выводит число элементов
print(len(a))
b = a + str(len(a))
# Выводит результат b
print(b)

"""def repeat(s, exclaim):
    result = s + s + s
    if exclaim:
        result = result + '!!!'
    return result

def main():
    print repeat('Yay', False)
    print repeat('Woo Hoo', True)"""

Oleh_Komenchuk = True
if Oleh_Komenchuk:
    print ("Be careful not to all off!")

# Буква O
print ("#"*9, end='\n \n')
print ("#\t\t#\n"*3)
print ("#"*9, end='\n \n \n')
# Буква H
print ("#\t\t#\n"*2, end='\n')
print ("#"*9, end='\n \n')
print ("#\t\t#\n"*2, end='\n')