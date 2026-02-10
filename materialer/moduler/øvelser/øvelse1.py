import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

api_key = os.environ.get('API_KEY')
print(api_key)