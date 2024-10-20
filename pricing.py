from abc import ABC, abstractmethod
import datetime

class PriceStrategy(ABC):
    """Abstract base class for rental pricing, implemented as a singleton for each subclass."""
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(PriceStrategy, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class NewReleasePrice(PriceStrategy):
    """Pricing rules for New Release movies."""
    def get_rental_points(self, days):
        """New release rentals earn 1 point for each day rented."""
        return 1 * days

    def get_price(self, days):
        return 3 * days


class RegularPrice(PriceStrategy):
    """Pricing rules for Regular movies."""
    def get_rental_points(self, days):
        """Only get 1 point per rental."""
        return 1

    def get_price(self, days):
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount


class ChildrensPrice(PriceStrategy):
    """Pricing rules for Children's movies."""
    def get_rental_points(self, days):
        """Children's movies only get 1 point per rental."""
        return 1

    def get_price(self, days):
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount


def price_strategy_for_movie(movie) -> PriceStrategy:
    """Determine the price strategy for a given movie."""
    current_year = datetime.datetime.now().year
    if movie.year == current_year:
        return NewReleasePrice()
    elif any(genre.lower() == "children" for genre in movie.genre):
        return ChildrensPrice()
    else:
        return RegularPrice()
