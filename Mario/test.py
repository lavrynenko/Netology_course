while True:
    maximum = int(input('Введите число-максимум: '))
    quantity = int(input('Введите число, которое не больше введенного числа-максимума: '))
    if maximum < quantity:
        print('Введенное число должно быть МЕНЬШЕ или равно ',maximum ,' :) Повторите!: ')
    else:
        print('Ну наконец-то! :) ')
        break