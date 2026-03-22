# use pip install to install public/external libraries on global machine

# must then actually import those libraries into this file to use them
import requests
from dotenv import load_dotenv
import os # os lib is used to access environment variables (API keys)

load_dotenv() # makes everything in the .env file visible to program

# access .env variables (api keys)
odds_key = os.getenv("ODDS_API_KEY")
kaggle_key = os.getenv("KAGGLE_API_TOKEN")