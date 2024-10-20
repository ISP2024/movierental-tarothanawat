from dataclasses import dataclass, field
from typing import Collection


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
