#Калькулятор площади
length = int(input("Введите длинну: "))
width = int(input("Введите ширину: "))
print(f"{length * width}")
#Конвертер температур
t = int(input("Введите число "))
print(f" температура по фаренгейту  = {(t * 9/5) + 32}")
print(f" температура по Цельсия = {round((t - 32)*5/9)} ")

#Калькулятор возраста
age = int(input("Введите Ваш год рождения: "))
print(f"Вам {2026 - age} лет")

#Проверка на четность
num = int(input("Введите число: "))
print("ДА") if num % 2 == 0 else print("Нет")

#Определение високосного года
year = int(input("Введите год: "))
print(f"{year} это високосный") if (year % 4 == 0 and year % 400 == 0) else print(f"{year} это не високосный")

#Калькулятор оценок
num = int(input("Введите число: "))
if num >= 0 and num <= 59:
    print("F")
if  num >= 60 and num <= 69:
    print("D")
if num >= 70 and num <= 79:
    print("C")
if num >= 80 and num <= 89:
    print("B")
if num >= 90 and num <= 100:
    print("A")


#Таблица умножения
num = int(input("Введите число: "))
count =  1
for i in range(1,11):
    print(f"{count} * {num} = {num * i}")
    count +=1
# Сумма чисел
count = int(input("Введите количество чисел: "))
s = 0
for i in range(count):
    num = int(input("Введите число: "))
    s += num
print(f"Сумма чисел = {s}, среднее арифметическое = {s/count}")
#Факториал
num = int(input())
f = 1
for i in range(1,num+1):
    f *= i
print(f)
#Числа Фибоначчи
num = int(input("Введите число: "))
f = [0,1]
if num <= 2:
    print(*f[0:num])
else:
    for i in range(2,num):
        chislo = f[i-1] + f[i-2]
        f.append(chislo)
    print(*f)
#Поиск максимума и минимума
import random
lst = []
for i in range(10):
    number = random.randint(1,100000)
    lst.append(number)
print(max(lst))
print(min(lst))
# Реверс списка
lst[::1]
# Удаление дубликатов
lst = [1,1,2,3,4,5,5,6,6]
print(set(lst))
#Подсчет символов
stroka = input("Введи строку: ").lower()
sogl ="бвгджзйклмнпрстфхцчшщ"
gl = "аеёиоуыэюя"
count_sogl = 0
count_gl = 0
for i in stroka:
    if i in sogl:
        count_sogl += 1
    if i in gl:
        count_gl +=1
print(f"кол-во согласных букв {count_sogl}, кол-во гласных букв {count_gl}")
#палиндром
word = input("Введите слово: ")
print("Да, палиндром") if word == word[::-1] else print("Нет")
#анаграммы
word1 = input("Введите слово №1: ").lower()
word2 = input("Введите слово №2: ").lower()
count = 0
if len(word1) == len(word2):
    for i in word1:
        if i in word2:
            count +=1
print("Да") if count == len(word1) else print("Нет")
#Простые числа
def num(number):
    count = 0
    for i in range(1,number+1):
        if number % i == 0:
            count +=1
    return "ДА" if count == 2 else "нет"
print(num(int(input())))
#калькулятор с функциями
def summa(*args):
    return sum(args)
summa()
def difference(a,b):
    return a - b
difference()
def division(a,b):
    return round(a/b,2)
division()
def multiplication(a,b):
    return a*b
multiplication()
#Генератор паролей
import random
password = ["б","в","г","д","ж","з","й","к","л","м","н","п","р","с","т","ф","х","ц","ч","ш","щ",1,2,3,4,5,6,7,8,9,0]
n = int(input("Введите длину пароля: "))
new_password = random.choices(password, k = n)
print(*new_password,sep="")
#Телефонная книга
phoneNumber = {}
phoneNumber["иван"] = 12
phoneNumber["света"] = 114
def addNum(name,number):
    phoneNumber[name] = number
    return phoneNumber

menu = int(input("Введите номер меню: "))
if menu == 1:
    name = input("Введите имя пользователя: ").lower()
    number = input("Введите телефонный номер: ")
    addNum(name,number)
if menu == 2:
    name = input("Введите имя контакта: ").lower()
    print(phoneNumber[name])
if menu == 3:
    name = input("Введите имя контакта для его удаления: ")
    del phoneNumber[name]
    print(phoneNumber)
if menu == 4:
    print(phoneNumber)
#подсчет частоты слов
slova = input("Введите слова: ").split()
d = dict()
for i in slova:
	if i in d:
		d[i] +=1
	else:
		d[i] = 1
print(d)
class Sports_equipment:

        def __init__(self,ball,racket,paddle):
              self.ball = ball
              self.racket = racket
              self.paddle = paddle

        def addSports_equipment(self,ball_count,racket_count,paddle_count):
            self.ball += ball_count
            self.racket += racket_count
            self.paddle += paddle_count
            return f" Кол-во спортивного инвентаря: мячи {self.ball}, ракетки {self.racket}, ракетки для настольного тенниса {self.racket}"
        
        def delSports_equipment(self,ball_count,racket_count,paddle_count):
            self.ball -= ball_count
            self.racket -= racket_count
            self.paddle -=paddle_count
            return f" Кол-во спортивного инвентаря: мячи {self.ball}, ракетки {self.racket}, ракетки для настольного тенниса {self.racket}"
              
        
    
sport1 = Sports_equipment(11,1,2)
print(sport1.addSports_equipment(22,23,24))
print(sport1.addSports_equipment(1,1,1))
print(sport1.delSports_equipment(10,12,21))





