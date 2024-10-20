from dataclasses import dataclass, field
from typing import Collection
import csv
import pandas as pandas
import pandas as pd


@dataclass(frozen=True)
class Movie:
    """A movie available for rent. Immutable."""
    title: str
    year: int
    genre: Collection[str] = field(default_factory=list)

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
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(',')
                        title = parts[1]
                        year = int(parts[2])
                        genres = parts[3].split('|')
                        movies.append(Movie(title, year, genres))
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


