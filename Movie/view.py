def display_film(film):
    print(f"Название: {film.title}")
    print(f"Жанр: {film.genre}")
    print(f"Режиссер: {film.director}")
    print(f"Год выпуска: {film.year}")
    print(f"Длительность: {film.duration}")
    print(f"Студия: {film.studio}")
    print(f"Актеры: {film.actors}")


class FilmView:

    def display_catalog(self, films):
        for film in films:
            print(f"- {film.title} ({film.year})")
