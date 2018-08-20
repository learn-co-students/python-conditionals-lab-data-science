import unittest2 as unittest
from ipynb.fs.full.index import *

class TestFunctionsConditions(unittest.TestCase):
    def test_better_restaurant_func(self):
        self.assertEqual(better_restaurant(frontier_restaurant, fork_fig), fork_fig)
        self.assertEqual(better_restaurant(fork_fig, frontier_restaurant), fork_fig)

    def test_cheaper_restaurant_func(self):
        self.assertEqual(cheaper_restaurant(frontier_restaurant, fork_fig), frontier_restaurant)
        self.assertEqual(cheaper_restaurant(fork_fig, frontier_restaurant), frontier_restaurant)

    def test_open_restaurants_func(self):
        self.assertItemsEqual(open_restaurants([fork_fig, frontier_restaurant]), [fork_fig])
