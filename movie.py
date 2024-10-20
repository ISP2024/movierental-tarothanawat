from dataclasses import dataclass, field
from typing import Collection
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


@dataclass(frozen=True)
class Movie:
    """A movie available for rent. Immutable."""
    title: str
    year: int
    genre: Collection[str] = field(default_factory=list)

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_genre(self):
        return self.genre

    def is_genre(self, string: str) -> bool:
        #  any: check if something exists in a collection.
        return any(g.lower() == string.lower().strip() for g in self.genre)

    def __str__(self):
        return f"{self.title} ({self.year})"


class MovieCatalog:
    """Singleton class to manage a catalog of movies."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls._instance.movies = cls._instance._load_movies()
        return cls._instance

    def _load_movies(self):
        """Load movies from the CSV file into Movie objects."""
        movies = []
        try:
            with open('movies.csv', 'r') as file:
                next(file)
                for line_number, line in enumerate(file, start=2):  #
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    parts = line.split(',')
                    if len(parts) < 4:
                        logging.error(f"Line {line_number}: Unrecognized format '{line}'")
                        continue

                    try:
                        movie_id = parts[0]
                        title = parts[1]
                        year = int(parts[2])
                        genres = parts[3].split('|')
                        movies.append(Movie(title, year, genres))
                    except (ValueError, IndexError) as e:
                        logging.error(f"Line {line_number}: Unrecognized format '{line}'")
                        continue
        except FileNotFoundError:
            print("Movies file not found.")
        except Exception as e:
            print(f"Error loading movies: {e}")

        return movies

    def get_movie(self, title: str, year: int = None) -> Movie:
        """Return the first matching Movie by title and optional year."""
        for movie in self.movies:
            if movie.title.lower() == title.lower() and (year is None or movie.year == year):
                return movie
        return None


