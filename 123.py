

def test_chech(weight):
    while True:
        if not weight:
            weight = input(
                'Вы не указали Ваш вес! Пожалуйста, введите Ваш вес (в кг.): '
            )
        try:
            float(weight.replace(',', '.'))
            return weight
        except ValueError:
            weight = input(
                'Вес должен быть числом (например, 70.5). Пожалуйста, введите вес: '
            )


weight = input('Введите вес')

weight_fl = float(test_chech(weight).replace(',', '.'))

print(weight_fl)
