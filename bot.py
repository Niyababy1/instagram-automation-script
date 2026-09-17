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
import os
from dotenv import load_dotenv
from instagrapi import Client

load_dotenv()

cl = Client()

# Safely pull the proxy URL from environment variables
proxy_url = os.getenv("PROXY_URL")
if proxy_url:
    cl.set_proxy(proxy_url)
    print("Proxy configured successfully.")

try:
    cl.login(os.getenv("INSTAGRAM_USERNAME"), os.getenv("INSTAGRAM_PASSWORD"))
    print("Logged into Instagram through proxy!")
except Exception as e:
    print(f"Error: {e}")import os
from dotenv import load_dotenv
from instagrapi import Client

load_dotenv()

cl = Client()

# Safely pull the proxy URL from environment variables
proxy_url = os.getenv("PROXY_URL")
if proxy_url:
    cl.set_proxy(proxy_url)
    print("Proxy configured successfully.")

try:
    cl.login(os.getenv("INSTAGRAM_USERNAME"), os.getenv("INSTAGRAM_PASSWORD"))
    print("Logged into Instagram through proxy!")
except Exception as e:
    print(f"Error: {e}")
import os
from dotenv import load_dotenv
from instagrapi import Client

load_dotenv()

cl = Client()

# Safely pull the proxy URL from environment variables
proxy_url = os.getenv("PROXY_URL")
if proxy_url:
    cl.set_proxy(proxy_url)
    print("Proxy configured successfully.")

try:
    cl.login(os.getenv("INSTAGRAM_USERNAME"), os.getenv("INSTAGRAM_PASSWORD"))
    print("Logged into Instagram through proxy!")
except Exception as e:
    print(f"Error: {e}")

