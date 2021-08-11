import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = "https://habr.com/ru/all/"

# ret = requests.get('https://2ip.ru/')
# print(ret.text)

# soup = BeautifulSoup(ret.text, 'html.parser')

# el = soup.find(id='d_clip_button')

# ip = el.text
# print(ip)


def main():
    ret = requests.get(URL)
    # print(ret.text)
    soup = BeautifulSoup(ret.text, "html.parser")

    art_list = soup.find("div", class_="tm-articles-list")
    articles = art_list.find_all("article", class_="tm-articles-list__item")
    for article in articles:
        if any((k in article.text for k in KEYWORDS)):
            title = article.find("a", class_="tm-article-snippet__title-link").text
            dt = article.find("span", class_="tm-article-snippet__datetime-published").text
            link = article.find("a", class_="tm-article-snippet__title-link").attrs.get("href")
            print(f"{dt} - {title} - {urljoin(URL, link)}")


if __name__ == '__main__':
    main()
