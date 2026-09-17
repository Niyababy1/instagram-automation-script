import os
from dotenv import load_dotenv
from instagrapi import Client

# 1. Load the hidden settings
load_dotenv()

cl = Client()

# 2. Inject the proxy link if it exists
proxy_link = os.getenv("PROXY_URL")
if proxy_link:
    cl.set_proxy(proxy_link)
    print("Connecting through the proxy tunnel...")

# 3. Log in safely
try:
    cl.login(os.getenv("INSTAGRAM_USERNAME"), os.getenv("INSTAGRAM_PASSWORD"))
    print("Login successful!")
except Exception as e:
    print(f"Failed to connect: {e}")
