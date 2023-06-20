from dotenv import load_dotenv
import os
from FlickrAPI import FlickrAPI
load_dotenv()

#Get API_key and secret from .env
api_key = os.getenv("FLICKR_API_KEY")
api_secret = os.getenv("FLICKR_API_SECRET")

flicker_api = FlickrAPI(api_key, api_secret)

#The keyword used for searching images
keyword = "Forest in fire"
#The number of images to retrieve per page
per_page = 100
#The desired size of the images to download (e.g., 'Large', 'Medium', 'Original','Small')
desired_size = "small"
#The directory path where the downloaded images will be saved
save_dir = "forest_fire"
# function to get images
flicker_api.get_images(keyword, per_page, desired_size, save_dir)
