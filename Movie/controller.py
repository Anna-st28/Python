class FilmController:
    def __init__(self):
        self.films = []

    def add_film(self, film):
        self.films.append(film)

    def get_all_films(self):
        return self.films

    def get_film_by_title(self, title):
        for film in self.films:
            if film.title.lower() == title.lower():
                return film
        return None

    def delete_film_by_title(self, title):
        for film in self.films:
            if film.title.lower() == title.lower():
                self.films.remove(film)
                return True
        return False

