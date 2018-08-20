
# Conditionals in Python Lab

## Introduction

Alright, now that we have seen how to use condtionals, let's put them to use. We'll use some data from restaurants on yelp to decide where we want to eat and we'll use conditionals to help us do that.

## Objectives
* Use conditionals to assert if an element passes a certain condition
* Combine conditionals and loops to return a list of elements that pass a certain condition

## Instructions

Let's take a look at some data about restaurants we retrieved from Yelp. We will use these restaurants later with our conditional statemtents.


```python
fork_fig = {
 'display_phone': '(505) 881-5293',
 'id': 'fork-and-fig-albuquerque',
 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/_-DpXKfS3jv6DyA47g6Fxg/o.jpg',
 'is_closed': False,
 'name': 'Fork & Fig',
 'phone': '+15058815293',
 'price': '$$',
 'rating': 4.5,
 'review_count': 604,
}

frontier_restaurant = {
 'display_phone': '(505) 266-0550',
 'distance': 4033.6583235266075,
 'id': 'frontier-restaurant-albuquerque-2',
 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/M9L2z6-G0NobuDJ6YTh6VA/o.jpg',
 'is_closed': True,
 'name': 'Frontier Restaurant',
 'phone': '+15052660550',
 'price': '$',
 'rating': 4.0,
 'review_count': 1369,
}
```

Now that we are familiar with the data, we can get to the fun stuff. Let's create conditional statements that allow us to decide whether a restaurant has enough reviews for us to feel comfortable with its rating. This means that we want to make sure there is enough data points to decide if the rating is a statistically relevant deciding factor and not an outlier. We are data scientists, after all!


```python
fork_fig_rating_relevance = None
frontier_restaurant_rating_relevance = None
# write conditional statements here to assign a True or False value to each restaurant rating relevance variable
# a rating is only relevant if there are over 750 reviews
```

## Using for loops with conditionals

Let's write a for loop that iterates over a list of restaurants and returns the restaurant with the better rating. 


```python
restuarnts = [fork_fig, frontier_restaurant]
```


```python
highest_rated = None
# write your for loop here using the list of restuarants above
# assign highest_rated the restaurant with highest rating
```


```python
print(highest_rated['name']) # 'Fork & Fig'
```

Now do the same for the most reviewed restaurant and the cheapest restaurant.


```python
most_reviewed = None
# write your for loop here using the list of restuarants above
# assign most_reviewed the restaurant with highest number of reviews
```


```python
cheapest_restaurant = None
# write your for loop here using the list of restuarants above
# assign cheapest_restaurant the restaurant with the fewest dollar signs
```

Next, use a for loop to return a list of restaurants that are currently open. 


```python
fork_fig['is_closed'] # False
```


```python
frontier_restaurant['is_closed'] # True
```


```python
open_restuarants = []
# write a for loop and conditional statements to choose only the open restaurants from the list of restaurants
# append the open restaurants to the list open_restaurants
```

### Summary

Great! In this lab we saw how to use for loops and conditions to return the restaurant(s) we want based on the questions we are trying to answer (i.e. which is highest rated, most reviewed, or open). We will continue to use conditional statements to create more dynamic and efficient code as we learn more and more about Python and programming.
