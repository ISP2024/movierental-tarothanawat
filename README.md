## Movie Rental Refactoring
[![Autograding Tests](https://github.com/ISP2024/movierental-tarothanawat/actions/workflows/python-publish.yml/badge.svg)](https://github.com/ISP2024/movierental-tarothanawat/actions/workflows/python-publish.yml)

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rational

# 2.1 What refactoring signs (code smells) suggest this refactoring?
Ans: Feature Envy in Couplers.Because movie class should only have methods that is related to movie, PriceStrategy and get_price should be moved to Rental instead.


# 2.2 What design principle suggests this refactoring? Why?
Ans: SRP aka. Single Responsibility Principle suggests this refactoring. Because a class should define only one thing, 
Movie class should only have things that are related to movies such as title, release date, genre.

# 5.2 Describe where you implement this method and the reasons for your choice. Include one or more of these design principles to justify your design and how it applies:

**Low Coupling**: I placed price_strategy_for_movie function outside of any class (in the pricing.py module) minimizing the coupling between Rental and PriceStrategy
**High Cohesion**: price_strategy_for_movie function is related to PriceStrategy class, so I put them together in the same module which is good for maintainability.
**SRP**: now Movie and Rental class doesn't associate themselves with calculating the price. It gets done in pricing.py module
**Information Expert**: The class Movie has year and genre attributes which is necessary for determining the price strategy.
**Other**: If we decided to create a new price strategy we can easily implement it in the pricing.py module without having to change any code in Movie or Rental.
