import time


def binary_search_iterative(func, interval, log_filename, tolerance=1e-5):
    start_time = time.time()  # начальное время выполнения кода
    a, b = interval  # Присваивает начальные границы интервала a, b
    f_a, f_b = func(a), func(b)  # вычисляет значения функции func в этих точках (f_a и f_b).

    with open(log_filename, "w") as log:
        log.write(f"Начальный интервал: [{a}, {b}], f(a)={f_a}, f(b)={f_b}\n")

    if f_a * f_b > 0:
        with open(log_filename, "a") as log:
            log.write("Корней нет, значения функции на концах интервала одного знака.\n")
        return None

    while abs(b - a) > tolerance:
        mid = (a + b) / 2  # Вычисляет середину интервала mid
        f_mid = func(mid)  # значение функции func в этой точке f_mid.
        elapsed_time = time.time() - start_time  # Вычисляет время, затраченное на выполнение алгоритма

        with open(log_filename, "a") as log:
            log.write(f"Interval: [{a}, {b}], Midpoint: {mid}, f(mid)={f_mid}, Elapsed: {elapsed_time:.5f} sec\n")

        if abs(f_mid) < tolerance:  # Если значение в середине достаточно близко к нулю
            with open(log_filename, "a") as log:
                log.write(f"Корень найден: {mid}, f(mid)={f_mid}, Сходимость достигнута!\n")
            return mid

        if func(a) * f_mid < 0:  # Если корень в левом подотрезке
            b = mid
        else:  # Если корень в правом подотрезке
            a = mid

    return (a + b) / 2


# Пример задания функции
def example_func(x):
    return x ** 3 - 4 * x - 9  # Пример функции: x^3 - 4x - 9


# Определяем границы интервала [a, b]
interval = [2, 3]  # Значения выбраны так, что example_func(2) * example_func(3) < 0

# Имя файла для логирования
log_file = "binary_search_iterative_log.txt"

# Выполняем подсчёт корня
root = binary_search_iterative(example_func, interval, log_file)

# Выводим результат
if root is not None:

    print(f"Найденный корень: {root:.5f}")
else:
    print("На заданном интервале корней нет.")