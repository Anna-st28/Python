class FilmView:
    def print_menu(self):
        print("==== Редактирование данных каталога фильмов ====")
        print("Действия с фильмами:")
        print("1 - добавление фильма")
        print("2 - каталог фильмов")
        print("3 - просмотр определенного фильма")
        print("4 - удаление фильма")
        print("q - выход из программы")

    def print_film_details(self, film):
        print("Название: ", film.title)
        print("Жанр: ", film.genre)
        print("Режиссер: ", film.director)
        print("Год выпуска: ", film.year)
        print("Длительность: ", film.duration)
        print("Студия: ", film.studio)
        print("Актеры: ", film.actors)
