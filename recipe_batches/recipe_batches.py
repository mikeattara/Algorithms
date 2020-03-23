#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    if set(ingredients.keys()).issuperset(set(recipe.keys())):
        min_ratio = math.inf
        for key in recipe:
            ratio = ingredients[key] // recipe[key]
            if ratio < min_ratio:
                min_ratio = ratio
        return min_ratio
    return 0


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
