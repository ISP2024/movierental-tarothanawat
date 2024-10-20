# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, MovieCatalog
from rental import Rental
from customer import Customer


def make_movies():
    """Some sample movies."""
    movies = [
        ['Civil War', 2024],
        ['Barbie', None],
        ['Poor Things', None],
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    catalog = MovieCatalog()
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(catalog.get_movie(movie[0], movie[1]), days))
        days = (days + 2) % 5 + 1
    print(customer.statement())

