from time import sleep


def repeat_decorator(
    call_count=None, start_sleep_time=None, factor=None, border_sleep_time=None
):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Кол-во запусков = {call_count}\nНачало работы")
            t = start_sleep_time
            for i in range(1, call_count + 1):
                sleep(t)
                if t < border_sleep_time:
                    t = start_sleep_time * factor**i
                else:
                    t = border_sleep_time
                print(
                    f"Запуск номер {i}. Ожидание: {t} секунд. Результат декорируемой функций = {func(*args, **kwargs)}."
                )
            print("Конец работы")

        return wrapper

    return decorator


@repeat_decorator(call_count=3, start_sleep_time=1, factor=2, border_sleep_time=10)
def multiplier(n):
    return n * 2


if __name__ == "__main__":
    multiplier(2)
