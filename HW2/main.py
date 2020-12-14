import json
import os


class CountryIterator():

    def __init__(self, file_path):
        self.file_path = os.path.join(os.getcwd(), file_path)
        self.wiki = "https://en.wikipedia.org/wiki/"
        self.counter = -1

        with open(self.file_path) as f:
            self.countries_full = json.load(f)

        self.country_list = [x["name"]["common"] for x in self.countries_full]

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == len(self.country_list):
            raise StopIteration
        return f"{self.country_list[self.counter]}: {self.wiki}{self.country_list[self.counter]}"


def main():
    print("start")
    file_path = "countries.json"
    country = CountryIterator(file_path)
    for i in country:
        print(i)


if __name__ == '__main__':
    main()
