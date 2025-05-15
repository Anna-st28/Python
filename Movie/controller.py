from Movie.model import Film
from Movie.view import FilmView


class FilmController:
    def __init__(self):
        self.films = []
        self.view = FilmView()

    def add_film(self, title, genre, director, year, duration, studio, actors):
        film = Film(title, genre, director, year, duration, studio, actors)
        self.films.append(film)

    def get_film(self, title):
        for film in self.films:
            if film.title == title:
                return film
        return None

    def remove_film(self, title):
        self.films = [film for film in self.films if film.title != title]

    def run(self):
        while True:
            print("\nДействия с фильмами:")
            print("1 - добавление фильма")
            print("2 - каталог фильмов")
            print("3 - просмотр определенного фильма")
            print("4 - удаление фильма")
            print("q - выход из программы")

            choice = input("Выберите вариант действия: ")

            if choice == '1':
                title = input("Название: ")
                genre = input("Жанр: ")
                director = input("Режиссер: ")
                year = int(input("Год выпуска: "))
                duration = int(input("Длительность: "))
                studio = input("Студия: ")
                actors = input("Актеры: ")
                self.add_film(title, genre, director, year, duration, studio, actors)
            elif choice == '2':
                self.view.display_catalog(self.films)
            elif choice == '3':
                title = input("Введите название фильма: ")
                film = self.get_film(title)
                if film:
                    display_film(film)
                else:
                    print("Фильм не найден.")
            elif choice == '4':
                title = input("Введите название фильма для удаления: ")
                self.remove_film(title)
            elif choice == 'q':
                break
            else:
                print("Неверный ввод.")
