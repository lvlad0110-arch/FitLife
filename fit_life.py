# Проект FitLife - MVP версия 1.0
# импортируем таймер для задержки перед выводом. Исключительно для красоты
from time import sleep as zzz

# Функции выводит уведомления пользователю о необходимости ввода данных
# в поля, без которых все поломается на этапе расчета ИМТ и, соответственно
# при расчете нормы потребления воды


def warn_name(user_name):
    """проверяет ввод и запрашивает имя пользователя"""
    if user_name == '':
        choice = input('Не хотите указывать имя? 1 - укажу | 0 - нет ')
        if choice == '1':
            return input('Пожалуйста, укажите Ваше имя: ')
        else:
            print('Мы Вас поняли, таинственный незнакомец :)')
            return 'Таинственный незнакомец'
    return user_name


def warn_age(user_age):
    """проверяет ввод и запрашивает возраст пользователя"""
    if user_age == '' or not user_age.isdigit():
        return input(
            'Вы не указали свой возраст! Пожалуйста, '
            'укажите Ваш возраст: '
        )
    return user_age


def warn_height(height):
    """проверяет ввод и запрашивает высоту пользователя"""
    if height == '':
        return input(
            'Вы не указали Ваш рост! Без него рассчитать '
            'ИМТ не получится. Пожалуйста, введите Ваш рост (в метрах): '
        )
    return height


def warn_weight(weight):
    """проверяет ввод и запрашивает вес пользователя"""
    if weight == '':
        return input(
            'Вы не указали Ваш вес! Без него '
            'рассчитать ИМТ не получится. Пожалуйста, введите Ваш вес '
            '(в кг.): '
        )
    return weight


def warn_water(water_usage):
    """проверяет и запрашивает потребение воды человеком"""
    if water_usage == '':
        return input(
            'Вы не указали, сколько воды Вы пьете. Если '
            'не хотите указывать, пожалуйста, напишите "0". '
        )
    return water_usage


# расчет ИМТ
def bmi(height, weight):
    """рассчитывает ИМТ человека на основе полученных данных"""
    return round((weight / height ** 2), 1)


# функция дает рекомендации по объему потребляемой воды в сутки в зависимости
# от параметров пользователя.
def water_recommend(user_age, water_usage, weight):
    """дает рекомендацию пользователю по количеству воды в день"""
    if int(user_age) < 18 and water_usage < 1:
        water_consump = round(((weight * 30) / 1000), 1)
        print(
            'Вы пьете мало воды! Вам нужно минимум', water_consump,
            'литра.',
        )
        return water_consump
    elif int(user_age) >= 18 <= 59 and water_usage < 1.5:
        water_consump = (weight * 30) / 1000
        print(
            'Вы пьете мало воды! Вам нужно минимум', water_consump,
            'литра.',
        )
        return water_consump
    elif int(user_age) >= 60 and water_usage < 1.5:
        water_consump = (weight * 30) / 1000
        print(
            'Вы пьете мало воды! Вам нужно минимум',
            water_consump,
            'литра.',
        )
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
    if water_usage > 1.5:
        print('Вы пьете достаточно воды, так держать!')
    else:
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
user_age = int(warn_age(user_age).replace(',', '.'))
height = float(warn_height(height).replace(',', '.'))
weight = float(warn_weight(weight).replace(',', '.'))
water_usage = float(warn_water(water_usage).replace(',', '.'))


print('Все данные получены! Производим расчет.')
# zzz тут для красоты, так все отобразится не сразу
zzz(0.8)
print()


print_results()
