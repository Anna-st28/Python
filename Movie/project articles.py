from Movie.controller import FilmController
from Movie.model import Film
from Movie.view import FilmView

if __name__ == "__main__":
    controller = FilmController()
    view = FilmView()

    while True:
        view.print_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название фильма: ")
            genre = input("Введите жанр: ")
            director = input("Введите режиссера: ")
            year = input("Введите год выпуска: ")
            duration = input("Введите длительность: ")
            studio = input("Введите студию: ")
            actors = input("Введите актеров через запятую: ").split(", ")
            film = Film(title, genre, director, year, duration, studio, actors)
            controller.add_film(film)
            print("Фильм добавлен!")
        elif choice == "2":
            films = controller.get_all_films()
            for film in films:
                print(film.title)
        elif choice == "3":
            title = input("Введите название фильма: ")
            film = controller.get_film_by_title(title)
            if film:
                view.print_film_details(film)
            else:
                print("Фильм не найден.")
        elif choice == "4":
            title = input("Введите название фильма: ")
            if controller.delete_film_by_title(title):
                print("Фильм удален.")
            else:
                print("Фильм не найден.")
        elif choice == "q":
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")
