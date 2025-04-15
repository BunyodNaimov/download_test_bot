import json
from os import getenv

import requests
from dotenv import load_dotenv
load_dotenv()

RAPID_KEY = getenv('RAPID_KEY')
def download_instagram(link):
	url = "https://instagram-downloader-download-instagram-stories-videos4.p.rapidapi.com/convert"

	querystring = {"url": link}

	headers = {
		"x-rapidapi-key": RAPID_KEY,
		"x-rapidapi-host": "instagram-downloader-download-instagram-stories-videos4.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	result = json.loads(response.text)
	return result
# print(download_instagram("https://www.instagram.com/reel/DHn2qIuM6V2/?igsh=MTRqZmZ0bjllZ3ozNA=="))
