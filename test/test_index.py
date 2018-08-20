import pytest
from ipynb.fs.full.index import open_restuarants, cheapest_restaurant, most_reviewed, highest_rated, fork_fig_rating_relevance, frontier_restaurant_rating_relevance

def test_open_restaurants():
    assert type(open_restaurants) == type([])
    assert open_restaurants == [fork_fig]

def test_cheapest_restaurant():
    assert type(cheapest_restaurant) == type({})
    assert cheapest_restaurant == frontier_restaurant

def test_most_reviewed():
    assert type(most_reviewed) == type({})
    assert most_reviewed == frontier_restaurant

def test_highest_rated():
    assert type(highest_rated) == type({})
    assert highest_rated == fork_fig

def test_rating_relevance():
    assert fork_fig_rating_relevance == False
    assert frontier_restaurant_rating_relevance == True
