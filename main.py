from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import tweepy as tw
import spoonacular as sp
import requests
#from datetime import datetime, date, time, timedelta
#from collections import Counter
import sys
import os
import flask
import random

foodLst = ["taco", "soup", "sushi", "chicken", "pizza", "bacon", "spaghetti"]
foodType = ""
user = ""
tweet = ""
date = ""
title = ""
ingredients = ""
image = ""
url = ""
servings = ""
readyInMinutes = ""
ingredMap = {}

tweetLst = []

def spoonacular_function():
  # define globals
  global title
  global ingredients
  global image
  global url
  global servings
  global readyInMinutes
  global ingredMap
  
  # spoonacular api
  spoon_api_key = os.environ['api_key']
  spoon_api = sp.API(spoon_api_key)
  
  # requests for 100 recipes
  response = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?query={foodType}&number=100&apiKey={spoon_api_key}")
  quote = response.json()
  totalResults = {'total':quote['totalResults']}
  recipes = {'results':quote['results']}
  
  # store ID to recipes in list
  lstOfRecipeIDS = []
  for recipe in recipes['results']:
    lstOfRecipeIDS.append(recipe['id'])
  
  # pick random ID from list of recipe IDs
  randomRecipe = random.choice(lstOfRecipeIDS)
  
  
  # requests recipe for randomRecipe
  ingredMap.clear()
  response = requests.get(f"https://api.spoonacular.com/recipes/{randomRecipe}/ingredientWidget.json?apiKey={spoon_api_key}")
  quote = response.json()
  result = {'ingredients':quote['ingredients']}
  
  # map out measurements for each ingredient
  for res in result['ingredients']:
    tmpLst = [res['amount']['us']['value'], res['amount']['us']['unit']]
    ingredMap[res['name']] = tmpLst

  # example code below to print out ingredient info
  # 0 represents the value (ex: the 2 in 2 cups), 1 represents the unit (ex: the cups in 2 cups)
  """
  for ingred in ingredMap:
    print(ingredMap[ingred][0], ingredMap[ingred][1], ingred)
  """
  # end example
  
  # requests recipe info: title, id, image urls, servings, readyInMinutes
  response = requests.get(f"https://api.spoonacular.com/recipes/{randomRecipe}/information?includeNutrition=false&apiKey={spoon_api_key}")
  quote = response.json()
  
  title = quote['title']
  url = quote['spoonacularSourceUrl']
  image = quote['image']
  servings = quote['servings']
  readyInMinutes = quote['readyInMinutes']

  # end spoonacular_function()

app = flask.Flask(__name__)

@app.route('/') # Python decorator

def index():
  global foodType
  
  # get random food from list of 7 food types
  foodType = random.choice(foodLst)
  
  # get ingredient info for foodType through spoonacular api
  spoonacular_function()
  
  # twilio api keys
  consumer_key = os.environ['consumer_key']
  consumer_secret = os.environ['consumer_secret']
  access_token = os.environ['access_token']
  access_token_secret = os.environ['access_token_secret']
  # twilio api
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  auth_api = API(auth)
  api = tw.API(auth, wait_on_rate_limit=True)
  
  # get 100 tweets containing the query of foodType in the english langauge since the date 2020-01-01
  tweets = tw.Cursor(api.search, q=foodType, lang="en", since = "2020-01-01").items(100)
  for tweet in tweets:
    tweetLst.append(tweet)
  
  # select 1 random tweet from the 100  
  useTweet = random.choice(tweetLst)
  
  # get info from tweet: user, tweet, and date
  user = useTweet.user.screen_name
  tweet = useTweet.text
  date = useTweet.created_at
  
  # empty the list of 100 tweets, this allows us to select from 100 different tweets upon page refresh
  tweetLst.clear()
  
  # sending python variables to index.html through flask
  return flask.render_template(
    "index.html",
    foodType = foodType,
    user = user,
    tweet = tweet,
    date = date,
    title = title,
    image = image,
    url = url,
    servings = servings,
    readyInMinutes = readyInMinutes,
    ingredMap = ingredMap
    )

# run the web application    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
    # can add ,debug=True
    # if deployed to heroku with debug=True it will not work
    # must delete before deplyoing
)