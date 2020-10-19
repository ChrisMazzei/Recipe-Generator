# Recipe Generator
# Developed by Chris Mazzei
Note: This is cloned from my private repo version of the web app. Private repo along with all the commits is viewable upon request. 

Recipe Generator uses the Python and the Twitter API to fetch tweets that include 7 different and unique foods in the tweet.
HTML and CSS is used to display the tweets data on a webpage. The data displayed is the user of the tweet, the tweet itself, and time and date of the tweet.
The Spoonacular API is used to display data for one of the unique foods such as, the recipe, prep time, serve time, and link to the recipe.

To use this repository, you must following these steps:
NOTE: THESE STEPS ASSUME Cloud9 IS BEING USED. RESULTS MAY VARY ON OTHER PLATFORMS.
NOTE: ASSUMES YOU ALREADY HAVE GIT.

(Section 1) Setup Twitter API & Installs for tweepy, flask, and spoonacular:
1. Sign up for a twitter developer account here: https://developer.twitter.com
2. Navigate to https://developer.twitter.com/en/portal/projects-and-apps and make a new app.
3. After creating your project click on the key symbol, your keys and tokens will be displayed. NOTE: access token and secret can be regenerated if needed.
4. Clone this repository by using git clone https://github.com/NJIT-CS490/project1-cm544
5. Run the following commands in your terminal:
    sudo pip install tweepy
    (or) sudo pip3 install tweepy
    (or) pip install tweepy
    (or) pip3 install tweepy
6. Install flask using the same process as above ([sudo] pip[3] install flask)
7. Install python-dotenv using the same process as above ([sudo] pip[3] install python-dotenv)
8. Install spoonacular using the same process as above ([sudo] pip[3] install spoonacular)
9. The secret keys from step 2 must be concealed by creating a root-level file called twilio.env.
   NOTE: FILE MUST BE CALLED twilio.env in order for your API keys to not be public. You do NOT want this. 
10. Copy and paste the following into the twilio.env file.
    export consumer_key="xxxxxxxxxxxxxxxxxxxxxxx"
    export consumer_secret="xxxxxxxxxxxxxxxxxxxxxxx"
    export access_token="xxxxxxxxxxxxxxxxxxxxxxx"
    export access_token_secret="xxxxxxxxxxxxxxxxxxxxxxx"
11. Replace xxxxxxxxxxxxxxxxxxxxxxx with the appropiate keys from step 3.
12. Now, twilio.env must be sourced. To do this first make sure you are in the directory containing the twilio.env file.
    Next, run the command 'source twilio.env'

(Section 2) Setup Spoonacular API:
1. NOTE: You must complete Section 1 before completing the following steps.
2. Sign up for the spoonacular api here: https://spoonacular.com/food-api
3. Navigate to your profile here: https://spoonacular.com/food-api/console#Profile
4. Click on show your API Key, this API Key will be refered to in the upcoming steps.
5. We will be concealing the API Key from step 4 by making a root-level file called spoonacular.env
   NOTE: FILE MUST BE CALLED spoonacular.env in order for your API keys to not be public. You do NOT want this.
6. Paste the following into the spoonacular.env file.
   export api_key="xxxxxxxxxxxxxxxxxxxxxxx"
7. Replace xxxxxxxxxxxxxxxxxxxxxxx with the appropiate key from step 4.
8. Now, spoonacular.env must be sourced. To do this first make sure you are in the directory containing the spoonacular.env file.
   Next, run the command 'source spoonacular.env'

(Section 3) Running the web app: 
1. NOTE: You must complete Section 1 & Section 2 before completing the following steps.
2. To run the web app run the command 'python main.py' in the terminal while in the RecipeGenerator directory.
3. Click the Preview tab on the toolbar and then click Preview Running Application, the webpage should appear.
4. If any issues occur please refer to the sections below.

(Section 4) Deploy to Heroku
1. NOTE: You must complete Section 1 & Section 2 & Section 3 before completing the following steps.
2. Create a Heroku account here: https://id.heroku.com/login
3. Run the command 'npm install -g heroku' in the terminal to install Heroku
4. Verify the install with the command 'heroku --version', if errors occur debug with this source: https://devcenter.heroku.com/articles/heroku-cli#uninstalling-the-legacy-heroku-gem
5. Login to heroku through the terminal with the command 'heroku login', if errors occur use 'heroku login -i'
6. Now, go to the RecipeGenerator directory and run the command 'heroku create'. This creates a Heroku app for you.
7. Open your newly created Heroku App here: https://dashboard.heroku.com/apps
8. Navigate to the settings tab and click on "Reveal Configs". Here you will enter your keys from Section 1 and Section 2.
   Enter the variable names in the left textbox. These must be exact names as used in Section 1 and Section 2.
   Example of left textbox 'consumer_key' , Example of right textbox 'xxxxxxxxxxxxxxxxxxxxxxx'. Replace xxxx... with appropiate key.
   Repeat this step for all keys in Section 1 and Section 2.
9. Under 'Config Vars' you should see 'Buildpacks', click 'Add buildpack' and select the python option.
10. Run the following command in the RecipeGenerator directory to push your code to the heroku project: 'git push heroku master'
11. The termial will output a lot of text, when it is done outputting your project is ready to view on Heroku.
12. At the bottom of the output text there will be two links. To go to the projects deployed webpage use the link that looks like the following, or manually type it yourself on your browser:
    'https://projectname.herokuapp.com/'
13. To debug any errors run the command 'heroku logs'

See below sections for Known Problems / Common Issues / Future Improvements.

Known Problems:
1. Currently none, will be updated as needed.

Common Issuses:
1. When changing the HTML and CSS code a "hard refresh" may be required.
   This is done by pressing the following keys while on the webpage: "ctrl + shift + r"
2. When Cloud9 is fully closed and reopened the twilio.env and spoonacular.env file may need to be sourced again.
   Refer to Section 1 step 11 and Section 2 step 8 from above for sourcing the files.
3. Load time for program can be increased or decreased depending on sample size of tweets (currently 100).
   The tradeoff here is increased load time for better randomization or decreased load time for worse randomization.
4. Spoonacular API has quite a small daily limit (for free version). This can be avoided by using mock input when running test cases.
5. If new API keys are generated for spoonacular and or tweepy, do not forget to replace them in all the appropiate locations.
   locations are: .env files and heroku 'Config Vars'. Of course, you must resource again as well. Refer to step 2 above.

Future Improvements:
1. Improve the HTML and CSS.
2. Implement a more user friendly way to view new tweet and recipe data such as a "View Next" button or a scrolling option that refreshes the page.
3. Implement options for user to decide timeframe tweet was published.
4. Filter irrelevant / garbage tweets. Example: When searching for the type of food bread, a tweet displayed saying "LETS GET THIS BREAD",
   which is a slang reference, making it a garbage result. Another Example: Option to filter profanity.
5. Provide links to user of tweet. 
6. Provide links to tagged users.
