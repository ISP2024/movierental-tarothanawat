import unittest
from movie import Movie
from pricing import NewReleasePrice, RegularPrice, ChildrensPrice, price_strategy_for_movie


class PricingTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2024, ['Children', 'Action'])
        self.regular_movie = Movie("Air", 2000, 'Adult')
        self.children_movie = Movie("Frozen", 2018,['Children', 'Comedy'])
        self.childrens_movie = Movie("For Childrens", 2018, ['Childrens', 'Comedy'])

    def test_get_pricing_strategy(self):
        self.assertIsInstance(price_strategy_for_movie(self.new_movie), NewReleasePrice)
        self.assertIsInstance(price_strategy_for_movie(self.regular_movie), RegularPrice)
        self.assertIsInstance(price_strategy_for_movie(self.childrens_movie), ChildrensPrice)
        self.assertIsInstance(price_strategy_for_movie(self.children_movie), ChildrensPrice)

