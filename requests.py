import urllib.request,json
import requests
from .models import Post

url = 'http://quotes.stormconsultancy.co.uk/popular.json'
def get_post():
    response = requests.get(url).json()

    random_post = Quote(response.get("author"),response.get("post"))
    return random_post