import requests
from bs4 import BeautifulSoup


class Book:
    def __init__(self, title, author, link):
        self.title = title
        self.author = author
        self.link = link

    def __str__(self):
        return f"Название: {self.title}\nАвтор: {self.author}\nСсылка: {self.link}\n"


def parse_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    books = []
    for container in soup.find_all('div', class_='CollectionCard__content'):
        try:
            title = container.find('div', class_='CollectionCard__title').text.strip()
            author = container.find('div', class_='CollectionCard__authors').text.strip()
            link = 'https://www.litres.ru' + container.find('a', class_='CollectionCard__link')['href']
            book = Book(title, author, link)
            books.append(book)
        except AttributeError:
            print("Не удалось извлечь данные.")
    return books


def save_to_txt(books, filename='books.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        for book in books:
            f.write(str(book))


if __name__ == '__main__':
    url = 'https://www.litres.ru/collections/top-100-luchshih-proizvedeniy/'
    books = parse_books(url)
    save_to_txt(books)
