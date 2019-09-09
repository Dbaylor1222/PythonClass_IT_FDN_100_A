#! usr/bin/env python
"""
gw2ApiInfo.py

by David Baylor on 9/8/19

uses python 3 and guildwars2api from PyPI

downloads the item id, the name, and the recipe used to craft it off of the guild wars 2 server. Then stores that info
in a dictionary and dumps it into itemInfo.json.

The guild wars 2 server has a limit of 600 requests a minuet so I slow down my requests with a wait command in the
program.
"""
from guildwars2api.v2 import GuildWars2API  # this imports the guild wars 2 api
import json
import time

api = GuildWars2API()
itemIDs = api.items.get()  # this gets a list of all of the item IDs in GuildWars2
itemNumber = len(itemIDs)
print("There are {} items to go through. This might take a while.".format(itemNumber))
fivePercent = itemNumber/20
percent = 0
counter = 0
errors = []
items = {}

# this is a temporary file used to save data from previous runs. if a run fails for any reason I can rename the partial
# file to itemInfo1.json and restart where I left off.
with open("itemInfo1.json", "r") as itemInfo:
    items = json.load(itemInfo)

for itemID in itemIDs:
    if not str(itemID) in items:
        time.sleep(.3)  # this slows down the get requests to the server so that it does not exceed the server's limit

        try: # this try/except statement stops the program if there is an error but allows it to save the data to a file
            recipes = api.recipes_search.get(output=itemID) # this gets all the recipes for an item
            if recipes:
                itemRecipes = []
                for recipe in recipes:
                    recipeData = api.recipes.get(ids=recipe)[0]
                    itemDisciplines = recipeData["disciplines"]
                    itemIngredients = recipeData["ingredients"]
                    itemRecipe = {"disciplines":itemDisciplines, "ingredients":itemIngredients}
                    itemRecipes.append(itemRecipe) # this adds the recipe to a list
            else:
                itemRecipes = None # if the item does not have a recipe this will set itemRecipes to none

            item = {"id":itemID, "name":api.items.get(ids=itemID)[0]["name"], "recipes":itemRecipes}
            items[itemID] = item # this adds the data on a item to the items dictionary



        except Exeption as err:
            errors.append(itemID)
            logger.error(err)
            break

    counter += 1 # this counter prints the percent of items completed every 5 percent
    if counter >= fivePercent:
        counter = 0
        percent += 5
        print("{}%".format(percent))
with open("itmeInfoErrors.json", "w") as errorfile: # this dumps any items that produced errors into a file
    json.dump(errors, errorfile, indent=2)

with open("itemInfo.json", "w") as outfile: # this dumps all of the data into a file
    json.dump(items, outfile, indent=2)
