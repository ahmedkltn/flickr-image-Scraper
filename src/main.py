from dotenv import load_dotenv
import os
from FlickrAPI import FlickrAPI
load_dotenv()

#Get API_key and secret from .env
api_key = os.getenv("FLICKR_API_KEY")
api_secret = os.getenv("FLICKR_API_SECRET")

flicker_api = FlickrAPI(api_key, api_secret)

#The keyword used for searching images
natural_objects = [
    'Tree',
    'Mountain',
    'River',
    'Beach',
    'Forest',
    'Sunset',
    'Clouds',
    'Wildlife',
    'Flower',
    'Landscape',
    'Sky',
    'Waterfall',
    'Desert',
    'Ocean',
    'Animal'
]
man_made_objects = [
    'Building',
    'Car',
    'Bicycle',
    'Airplane',
    'Smartphone',
    'Chair',
    'Table',
    'Book',
    'Clock',
    'Computer',
    'Camera',
    'Bridge',
    'Statue',
    'Tools',
    'Clothing'
]
objects = dict(natural_obj=dict(dir_file="natural-objects",keywords=natural_objects), 
               man_obj=dict(dir_file="man-made-objects",keywords=man_made_objects)
               )
#The number of images to retrieve per page
per_page = 100
#The desired size of the images to download (e.g., 'Large', 'Medium', 'Original','Small')
desired_size = "small"
#The directory path where the downloaded images will be saved
# function to get images
for obj in objects.keys():
    for keyword in objects[obj]["keywords"]:
        flicker_api.get_images(keyword, per_page, desired_size, objects[obj]["dir_file"])
