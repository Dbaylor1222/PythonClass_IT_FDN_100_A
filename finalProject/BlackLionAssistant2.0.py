#! usr/bin/env python
"""
blackLionAssistant2.0.py

by David Baylor on 9/8/19

uses python 3 and guildwars2api from PyPI

Asks the user what crafting profession they are using. Then reads itemInfo.json and instantiates an object for each
item. If that item has a recipe it will populate the recipes attribute by instantiating the recipes class. Once it has
done this for every item it will loop back through each item and calculate the profit margin for crafting and selling
that item. To do this, it will first loop through all the recipes for an object and if it is craftable by the chosen
profession it will call the get price function. The get price function is a recursive function that gets the price of
the most basic components for and item and returns the sum of those components. This program then prints out the 5 items
with the best profit and saves the rest to a separate file.

The guild wars 2 server has a limit of 600 requests a minuet so I slow down my requests with a wait command in the
program.
"""


from operator import itemgetter
import json
import time
import pprint

from guildwars2api.v2 import GuildWars2API # this imports the guild wars 2api
from guildwars2api.base import GuildWars2APIError

class Item:
    """
    This class is instantiated for each item and holds all the data on an item
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.recipes = None
        self.buyPrice = None
        self.sellPrice = None


    def __repr__(self):
        return "<{}: {}>".format(self.id, self.name)

class Recipes:
    """
    this class holds all the data on an item's recipes
    """
    def __init__(self, id, ingredients, disciplines):
        self.outputId = id
        self.ingredients = ingredients
        self.disciplines = disciplines

    def __repr__(self):
        return "<{} recipe>".format(self.outputId)

def getprice(itemObj):
    """
    this is a recursive function that gets the price of the most basic components for and item and returns the sum of
    those components
    :param itemObj:
    :return the buy price for an item:
    """
    if not itemObj.buyPrice:
        time.sleep(.00166) # this slows down the get requests to the server so that it does not exceed the server's limit
        prices = api.prices.get(ids=itemObj.id) # this gets the prices of an the item if there are not already prices
        if not itemObj.recipes: # if there are no recipes this sets the buy price to the current price on the in game market place
            buyprice = prices[0]['buys']['unit_price']
            itemObj.buyPrice = buyprice
            return buyprice
        else: # if the item has a recipe this calls this function again on each ingredient
            bestPrice = None
            sellprice = prices[0]['sells']['unit_price']
            itemObj.sellPrice = sellprice
            for recipes in itemObj.recipes:
                if usrDiscipline in recipes.disciplines:
                    recipePrice = 0
                    for ingredients in recipes.ingredients:
                        ingredientPrice = getprice(objects[str(ingredients['item_id'])])
                        recipePrice += ingredientPrice*ingredients["count"]
                    if bestPrice is None or recipePrice < bestPrice:
                        bestPrice = recipePrice
            itemObj.buyPrice = bestPrice

            return bestPrice
    return itemObj.buyPrice

api = GuildWars2API()


usrDiscipline = ""
# this asks the user what crafting discipline they are using
while not usrDiscipline in ["Armorsmith", "Artificer", "Chef", "Huntsman", "Jeweler", "Leatherworker", "Scribe", "Tailor", "Weaponsmith"]:
    usrDiscipline = input("What crafting discipline are you using? Armorsmith, Artificer, Chef, Huntsman, "
                          "Jeweler, Leatherworker, Scribe, Tailor, Weaponsmith?  ")
    usrDiscipline = usrDiscipline.capitalize()

# this switches the file so that the program only runs with a small sample of items.
# with open("test.json", "r") as itemInfo:
#     items = json.load(itemInfo)

# this opens the file and reads every file in the game
with open("itemInfo.json", "r") as itemInfo:
    items = json.load(itemInfo)



objects = {}
for itemId in items: # this loops through the items and instantiates the Item class for each one.
    objects[itemId] = Item(items[itemId]['id'], items[itemId]['name'])
    if items[itemId]['recipes']:
        i = 0
        objects[itemId].recipes = []
        for recipes in items[itemId]['recipes']:
            item = items[itemId]
            itemRecipes = item['recipes']
            itemRecipe = itemRecipes[i]
            objects[itemId].recipes.append(Recipes(itemId, itemRecipe['ingredients'], itemRecipe['disciplines']))
            i += 1

profitList = []
for itemId in items: # this loops back through all the items and finds the price to craft each one
    if objects[itemId].recipes:
        for recipe in objects[itemId].recipes:
            if usrDiscipline in recipe.disciplines:
                try:
                    getprice(objects[itemId])

                # this passes the item and prints the name and ID if it fails. They could fail for a few reasons
                # including if there is and item that cannot be bought of crafted in their recipe
                except:
                    print(objects[itemId], recipe)
                    pass

        if objects[itemId].buyPrice and objects[itemId].sellPrice: # this makes a list of all the items and their profits
            profitList.append((objects[itemId].name, objects[itemId].sellPrice - objects[itemId].buyPrice))

profitList = sorted(profitList, key=itemgetter(1), reverse=True)
with open('profitList.txt', 'w') as outputFile: # this saves the sorted list of profits to a file
    for i in profitList:
        outputFile.write('{}\n'.format(i))

pprint.pprint(profitList[:5]) # this prints the top 5 most profitable items to craft





