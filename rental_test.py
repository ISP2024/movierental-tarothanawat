import unittest
from rental import Rental
from movie import Movie
from pricing import NewReleasePrice, RegularPrice, ChildrensPrice, price_strategy_for_movie


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2024, ['Action', 'Fantasy'])
        self.regular_movie = Movie("Air", 2000, ['Action'])
        self.childrens_movie = Movie("Frozen", 2018, ['Children'])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        self.assertEqual("Air (2000)", str(self.regular_movie))
        self.assertIsInstance(price_strategy_for_movie(self.regular_movie), RegularPrice)

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)

        # added tests for other types of movies.
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_price(), 6.5)
        rental = Rental(self.regular_movie, 6)
        self.assertEqual(rental.get_price(), 8)

        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_price(), 4.5)

    def test_rental_points(self):
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.childrens_movie, 100)
        self.assertEqual(rental.get_rental_points(), 1)

        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 100)
        self.assertEqual(rental.get_rental_points(), 1)

        rental_new = Rental(self.new_movie, 5)
        self.assertEqual(rental_new.get_rental_points(), 5)
        rental_new = Rental(self.new_movie, 100)
        self.assertEqual(rental_new.get_rental_points(), 100)

