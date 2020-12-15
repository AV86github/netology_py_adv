from datetime import datetime
import os


def decorator_logger(func):
    print("Invoked: decorator_logger")
    log_name = "log.txt"

    def wrapper(*args, **kwargs):
        print(f"Before call: {func.__name__}")
        mode = "a" if os.path.exists(log_name) else "w"
        print(mode)
        with open(log_name, mode) as f:
            f.write(f"{datetime.now()}: BEFORE. {func.__name__}  {args}, {kwargs}\n")
            result = func(*args, **kwargs)
            f.write(f"{datetime.now()}: AFTER. {func.__name__}  result: {result}\n")
        return result
        print(f"After call: {func.__name__}")
    return wrapper


def decorator_param_logger(log_name):
    print("Invoked: decorator_param_logger")

    def outer(func):
        print("Invoked: outer")

        def wrapper(*args, **kwargs):
            print(f"Before call: {func.__name__}")
            mode = "a" if os.path.exists(log_name) else "w"
            print(mode)
            with open(log_name, mode) as f:
                f.write(f"{datetime.now()}: BEFORE. {func.__name__}  {args}, {kwargs}\n")
                result = func(*args, **kwargs)
                f.write(f"{datetime.now()}: AFTER. {func.__name__}  result: {result}\n")
            return result
            print(f"After call: {func.__name__}")
        return wrapper
    return outer


@decorator_param_logger("new_log.txt")
def callable_func(arg1, arg2):
    print("inside: callable_func")
    return arg1 + arg2


def main():
    print("Start")
    res = callable_func(1, 3)
    print(f"main: {res}")


if __name__ == '__main__':
    main()
