from multiprocessing import Pool


def square(number):
    return number ** 2


# Функция для расчет квадратов чисел списка, которая использует многопроцессорность.
def compute_squares(numbers):
    with Pool() as p:
        squares = p.map(square, numbers)
        return squares


if __name__ == "__main__":
    # Список чисел, которые возводим в квадрат
    numbers = [95_555_555_555, 1, 2, 3, 10, 100, 200, 300, 500, 200]

    print(compute_squares(numbers))
