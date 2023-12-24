PI = 3.14


def calculate_length_circle(radius):  # radius - аргумент функции, (переменная в которую передаются данные)
    circle_length = 2 * PI * radius
    print(circle_length)


def calculate_area_circle(radius):
    circle_area = PI * radius ** 2
    print(circle_area)


r = float(input())
calculate_length_circle(5)  # данные (любые)
calculate_area_circle(r)
