import hashlib
import os
from decorator import decorator_param_logger


@decorator_param_logger("hw2.log")
def MyGenerator(file_name):
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path) as f:
        for line in f:
            hash = hashlib.md5(line.encode('utf-8')).hexdigest()
            yield hash


def main():
    generator = MyGenerator("test.txt")
    for item in generator:
        print(item)


if __name__ == '__main__':
    main()
