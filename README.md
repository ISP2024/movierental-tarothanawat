## Movie Rental Refactoring

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

