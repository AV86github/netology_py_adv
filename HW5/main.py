import re
import os
from pprint import pprint
from functools import reduce
import csv
from collections import defaultdict


class App():
    """
        1. Parse FIO to 1,2,3 fields
        2. Format phone +7(999)999-99-99 доб.9999
        3. Deduplicate
    """

    def __init__(self, book_path):
        self.book_path = book_path
        self.result_path = os.path.join(os.getcwd(), "phonebook.csv")
        # unformatted re
        # self.phone_re = re.compile(r"(\+7|8)\s*\(?(\d{3})\)?[\s-]*(\d{3})[^\d]?(\d{2})[^\d]?(\d{2})")
        # formatted re
        self.phone_re = re.compile(r"(\+7|8)(\d{3})(\d{3})(\d{2})(\d{2})")
        self.add_re = re.compile(r"(доб)(\d*)")

    def run(self):
        with open(self.book_path, encoding='utf-8', newline='') as f:
            rows = csv.reader(f, delimiter=",")
            contacts_list = list(rows)
        contacts_list = list(map(self.format_list, contacts_list))
        contacts_list = self.dedup(contacts_list)
        pprint(contacts_list)
        with open(self.result_path, "w", encoding='utf-8', newline='') as f:
            datawriter = csv.writer(f, delimiter=',')
            # Вместо contacts_list подставьте свой список
            datawriter.writerows(contacts_list)

    def dedup(self, contacts_list):
        # deduplication.
        # Key = contacts_list[item][0:2]
        res = defaultdict(list)
        for item in contacts_list:
            res[tuple(item[0:2])].append(item[2:])
            if len(res[tuple(item[0:2])]) > 1:
                res[tuple(item[0:2])] = [self.dedup_item(res[tuple(item[0:2])])]
        # dict to list
        contacts_list = []
        print(res)
        print("===========")
        for k, v in res.items():
            # print(v)
            contacts_list.append(list(k) + v[0])
        return contacts_list

    def dedup_item(self, items):
        # 2 or more arrays to one - for duplicated row
        res = []
        for item in list(zip(*items)):
            res.append(reduce(self.reduce_func, item))
        return res

    def reduce_func(self, prev_val, next_val):
        return prev_val if prev_val else next_val

    def format_list(self, raw):
        # parse FIO
        fio = " ".join(raw[0:3]).split()
        while len(fio) < 3:
            fio.append("")
        raw[0:3] = fio
        # format phone raw[5]
        phone = re.sub(r"[\s\-\(\)\.]", "", raw[5])
        if self.phone_re.search(phone):
            phone = self.phone_re.sub(r"+7(\2)\3-\4-\5", phone)
        if self.add_re.search(phone):
            phone = self.add_re.sub(r" \1. \2", phone)
        raw[5] = phone
        return raw


def main():
    BOOK_PATH = os.path.join(os.getcwd(), "phonebook_raw.csv")
    app = App(BOOK_PATH)
    app.run()


if __name__ == '__main__':
    main()
