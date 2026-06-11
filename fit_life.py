# Проект FitLife - MVP версия 1.0
# импортируем таймер для задержки перед выводом. Исключительно для красоты
from time import sleep
from random import randint as random

# Функции выводит уведомления пользователю о необходимости ввода данных
# в поля, без которых все поломается на этапе расчета ИМТ и, соответственно
# при расчете нормы потребления воды


def warn_name(user_name):
    """проверяет ввод и запрашивает имя пользователя"""
    if not user_name:
        choice = input('Не хотите указывать имя? 1 - укажу | 0 - нет ')
        if choice == '1':
            return input('Пожалуйста, укажите Ваше имя: ')
        else:
            print('Мы Вас поняли, таинственный незнакомец :)')
            return 'Таинственный незнакомец'
    return user_name


def warn_age(user_age):
    """проверяет ввод и запрашивает возраст пользователя"""
    if not user_age:
        choice_age = input('Не хотите указывать возраст? 1 - укажу | 0 - нет')
        if choice_age == '1':
            return input('Пожалуйста, укажите Ваш возраст: ')
        else:
            user_age = random(5, 100)
            print(f'Ваш случайный возраст {user_age} лет!')
    return user_age


def warn_height(height):
    """проверяет ввод и запрашивает высоту пользователя"""
    while True:
        if not height:
            height = input(
                'Вы не указали Ваш рост! Без него '
                'рассчитать ИМТ не получится. Пожалуйста, введите Ваш рост '
                '(в метрах): '
            )
        try:
            float(height.replace(',', '.'))
            return height
        except ValueError:
            height = input('Пожалуйста, укажите рост (цифрами): ')


def warn_weight(weight):
    """проверяет ввод и запрашивает вес пользователя"""
    while True:
        if not weight:
            weight = input(
                'Вы не указали Ваш вес! Без него '
                'рассчитать ИМТ не получится. Пожалуйста, введите Ваш вес '
                '(в кг.): '
            )
        try:
            float(weight.replace(',', '.'))
            return weight
        except ValueError:
            weight = input('Пожалуйста, укажите вес (цифрами): ')
    


def warn_water(water_usage):
    """проверяет и запрашивает потребление воды человеком"""
    global weight  # используем глобальную переменную
    
    while True:
        choice = input('Не хотите указывать сколько воды пьете? 1 - да | 0 - нет: ')
        
        if choice == '0':
            water_norm = round((weight * 30) / 1000, 1)
            print(f'Вам нужно минимум {water_norm} литра воды в день.')
            return str(water_norm)
        
        if choice == '1':
            water_usage = input('Сколько воды в день Вы пьете (в литрах)? ')
            if not water_usage:
                print('Вы не ввели значение.')
                continue
            try:
                float(water_usage.replace(',', '.'))
                return water_usage
            except ValueError:
                print('Используйте цифры (например, 1.5)')
                continue


# расчет ИМТ
def bmi(height, weight):
    """рассчитывает ИМТ человека на основе полученных данных"""
    return round((weight / height ** 2), 1)


# функция дает рекомендации по объему потребляемой воды в сутки в зависимости
# от параметров пользователя.
def water_recommend(user_age, water_usage, weight):
    """дает рекомендацию пользователю по количеству воды в день"""
    age = int(user_age)
    water_consump = (weight * 30) / 1000
    if age < 18:
        norm = 1.0
    else:
        norm = 1.5
    if water_usage < norm:
        print(f'Вы пьете мало воды! Вам нужно минимум {water_consump} литра.')
        return water_consump
    else:
        print('Вы пьете достаточно воды, так держать!')
        return None
   


def print_results():
    """оформляет результат"""
    print('=' * 40)
    print(
        f'Добрый день, {user_name}! Ваш возраст - {user_age}.',
        end='\n\n',
    )
    bmi_result = bmi(height, weight)
    print(f'Ваш ИМТ составляет {bmi_result}.')
    water_recommend(user_age, water_usage, weight)
    print(f'Расчет окончен, {user_name}, будьте здоровы!')
    print('=' * 40)


user_name = input('Добрый день! Как Вас зовут?: ')
user_age = input('Сколько Вам лет?: ')
weight = input('Введите, пожалуйста, Ваш вес (в кг.): ')
height = input('Введите Ваш рост (в метрах): ')
try:
    water_usage = input('Сколько воды в день Вы пьете (в л.)? ')
except EOFError:
    water_usage = '0'


user_name = warn_name(user_name)
user_age = int(warn_age(user_age))
height = float(warn_height(height).replace(',', '.'))
weight = float(warn_weight(weight).replace(',', '.'))
water_usage = float(warn_water(water_usage).replace(',', '.'))


print('Все данные получены! Производим расчет.')
# задержка тут для красоты, так все отобразится не сразу
sleep(0.8)


print_results()
