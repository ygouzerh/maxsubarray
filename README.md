# MAXSUBARRAY


## Description

Test for fun of different handmade algorithms for the maximum subarray problem.


The subarray problem is a complex problem where, taking an array of integers,
you need to return the subarray constituted of the contiguous values with the higher sum.


It is a fun and complex problem with multiple solutions, so this project aims to
test some of them (with avoiding Kadane's algorithm of course, because it is too easy).


[More details: https://en.wikipedia.org/wiki/Maximum_subarray_problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem)

## Participate

You are welcomed to participate ! 


You simply need to add your strategy in the project, create a folder with the following architecture: 

.
* strategy_name/
    * src/
        strategy.py
        ...
        \__init__.py
    * tests/
        tester.py
        ...
        \__init__.py
    \__init__.py

## Requirements

Python 3.6

pip

(virtualenv) 

## Installation

1. Clone the directory
2. Creating a virtualenv ([and install if it is not already done](https://virtualenv.pypa.io/en/stable/installation/)) : `python3 -m virtualenv venv`
3. Activate the virtualenv : `source venv/bin/activate`
4. Import externals modules : `pip install -r requirements.txt`


You could run the tests then on any strategies : `pytest strategy_name/tests/tester.py`

## How to test

Test framework used : **pytest**


The folder [core/test](core/tests/) provides testers in order to check
each strategy.


They are inspired by the Strategy Design Pattern,
so they could work on any strategies which have an execute function,
which take a sample array in entry and return an array.


To use the strategy, you need to create a file which will import
the classes that you want to used, and to declare a **fixture**
which return an instance of the strategy that you want to used.

[See an example](cutinthree/tests/tester.py)
