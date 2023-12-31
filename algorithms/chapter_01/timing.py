import time


def get_time(algorithm):
    start_time = time.time()
    print(f"Наибольшее значение: {algorithm}")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения алгоритма: {execution_time} секунд")

