# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, NewReleasePrice, RegularPrice, ChildrensPrice
from rental import Rental
from customer import Customer

def make_movies():
    """Some sample movies."""
    movies = [
        Movie("Air", NewReleasePrice()),
        Movie("Oppenheimer", RegularPrice()),
        Movie("Frozen", ChildrensPrice()),
        Movie("Bitconned", NewReleasePrice()),
        Movie("Particle Fever", RegularPrice())
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days = (days + 2) % 5 + 1
    print(customer.statement())
