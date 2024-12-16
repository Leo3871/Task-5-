import time


def binary_search_recursive(func, interval, log_filename, tolerance=1e-5, start_time=None):
    if start_time is None:  # Если начальное время выполнения не указано (None),
        start_time = time.time()  # устанавливаем текущее время работы программы с помощью time.time()

    a, b = interval
    f_a, f_b = func(a), func(b)  # вычисляем значения функции func в этих точках

    with open(log_filename, "a") as log:
        log.write(f"Interval: [{a}, {b}], f(a)={f_a}, f(b)={f_b}\n")

    if f_a * f_b > 0:
        with open(log_filename, "a") as log:
            log.write("Корней нет, значения на концах одного знака.\n")
        return None

    mid = (a + b) / 2
    f_mid = func(mid)  # Считаем значение функции в точке mid (середине интервала)

    elapsed_time = time.time() - start_time

    with open(log_filename, "a") as log:
        log.write(f"Midpoint: {mid}, f(mid)={f_mid}, Time elapsed: {elapsed_time:.5f} sec\n")

    if abs(f_mid) < tolerance:
        with open(log_filename, "a") as log:
            log.write(f"Корень найден: {mid}, f(mid)={f_mid}, Сходимость достигнута!\n")
        return mid

    if f_a * f_mid < 0:  # Корень в левом отрезке
        return binary_search_recursive(func, [a, mid], log_filename, tolerance, start_time)
    else:
        return binary_search_recursive(func, [mid, b], log_filename, tolerance, start_time)


def example_func(x):
    return x ** 3 - 4 * x - 9


log_file = "binary_search_recursive_log.txt"

# Очищаем содержимое файла перед началом обработки
with open(log_file, "w") as file:
    pass

root = binary_search_recursive(example_func, [2, 3], log_file)
print(f"Найденный корень: {root}")