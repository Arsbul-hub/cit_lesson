def get_max_number(a, b, c): # a - аргумент функции (переменная в которую передаются данные)
    # Алгоритм нахождения максимума
    numbers = a
    max_number = 0
    for n in numbers:
        if n > max_number:
            max_number = n

    print(max_number)

get_max_number(1, 2, 3) # вызов (запуск) функции
