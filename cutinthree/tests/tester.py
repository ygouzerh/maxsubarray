"""
Description : Test the strategy proposed
in this module
Author : Yohan GOUZERH
Creation : 05 October 2018
"""
import os, sys, inspect
import pytest
# Add the root of the project
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, os.path.dirname(parent_dir))
from core.tests.naturals import TestNaturals
from cutinthree.src.strategy import CutInThree

@pytest.fixture
def strategy():
    """
        Used by the testeurs to execute the strategy
    """
    return CutInThree()
