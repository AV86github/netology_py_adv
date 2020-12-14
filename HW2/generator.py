import hashlib
import os


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
