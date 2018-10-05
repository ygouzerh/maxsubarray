"""
Description : Provide a ready-to-used tester for naturals
Need to use a fixture to pass the strategy used.
Author : Yohan GOUZERH
Creation : 05 October 2018
"""

from random import randint

class TestNaturals():
    """
        Tester to check the
        execution of a strategy on samples
        consituted by naturals.
    """
    @staticmethod
    def verify_naturals(strategy, sample):
        """
            Execute the strategy and verify the
            result.
            For naturals, we just have to return the
            same array.
        """
        assert strategy.execute(sample) == sample

    def test_naturals_one(self, strategy):
        """
            Test with
            an array of one natural number
        """
        self.verify_naturals(strategy, [42])

    def test_naturals_three(self, strategy):
        """
            Test with
            an array of three integer
        """
        self.verify_naturals(strategy, [10, 20, 30])

    def test_naturals_random_simple(self, strategy):
        """
            Test with
            a random simple array
        """
        self.verify_naturals(strategy, [randint(0, 100) for _ in range(10)])

    def test_naturals_random_complex(self, strategy):
        """
            Test with
            a random complex array
            in order to test performance
        """
        self.verify_naturals(strategy, [randint(0, 100000) for _ in range(10000)])
