from rental import Rental
from movie import Movie
import logging


class Customer:
    """A customer who rents movies.

    The customer object holds information about the
    movies rented for the current billing period,
    and can print a statement of his rentals.
    """

    def __init__(self, name: str):
        """Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        """Add a rental for this customer"""
        if rental not in self.rentals:
            self.rentals.append(rental)
    
    def get_name(self):
        """Get the customer's name."""
        return self.name
    
    def statement(self):
        """Create a statement of rentals for the current period.

        Print all the rentals in the current period, 
        along with total charges and frequent renter points.
        
        Returns:
            the statement as a String
        """
        frequent_renter_points = 0
        # the .format method substitutes actual values into the fmt string
        statement = f"Rental Report for {self.name}\n\n"
        header_fmt = "{:40s}  {:6s} {:6s}\n"
        statement += header_fmt.format("Movie Title", "  Days", " Price")
        rental_fmt = "{:40s}  {:6d} {:6.2f}\n"

        for rental in self.rentals:
            statement += rental_fmt.format(
                            rental.get_movie().get_title(),
                            rental.get_days_rented(),
                            rental.get_price())

        # footer: summary of charges
        frequent_renter_points = self.get_total_rental_points()
        total_amount = self.get_total_amount()
        statement += "\n"
        statement += "{:40s}  {:6s} {:6.2f}\n".format(
                       "Total Charges", "", total_amount)
        statement += "Frequent Renter Points earned: {}\n".format(frequent_renter_points)

        return statement

    def get_total_amount(self):
        """Calculate the total charge for the current rentals."""
        return sum(rental.get_price() for rental in self.rentals)

    def get_total_rental_points(self):
        """Calculate the total frequent rental points for all rentals."""
        return sum(rental.get_rental_points() for rental in self.rentals)

