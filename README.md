# Lisp interpreter written in Python

## In general there are 2 main requirements for an language to be Turing-Complete:
- a form of conditional repetition or conditional branching
- a way to read and write some form of storage (e.g. variables, lists)

## In this implementation of Lisp interpreter in order to be Turing-Complete following functions were implemented:
- atom - checks whether or not the argument is an atom
- cons - creates a list out of given elements
- car - returns first element of list
- cdr - returns second element of list
- if - conditional if/else statement
- eq - tests equality of two elements
- quote - returns back given symbol

Selection of the function was based on John McCarthy and Paul Graham publicationson Lisp language

### REPL interpreter can be run from main.py file
