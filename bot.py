import os
from dotenv import load_dotenv
from instagrapi import Client

# 1. Load your secret credentials from the hidden .env file
load_dotenv()
IG_USERNAME = os.getenv("INSTAGRAM_USERNAME")
IG_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

# 2. Initialize the Instagram API client
cl = Client()

try:
    # 3. Log into Instagram automatically
    print("Logging into Instagram...")
    cl.login(IG_USERNAME, IG_PASSWORD)
    print("Login successful!")
    
    # 4. Example Action: Fetch and print details of a specific user
    user_info = cl.user_info_by_username("instagram")
    print(f"Target Account Biography: {user_info.biography}")

except Exception as e:
    print(f"An error occurred: {e}")
