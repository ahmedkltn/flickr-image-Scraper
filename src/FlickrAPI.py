import flickrapi
import urllib
import os

class FlickrAPI():
    """
        A wrapper class for interacting with the Flickr API to retrieve images.

        Attributes:
            api_key (str): The API key for accessing the Flickr API.
            api_secret (str): The API secret for accessing the Flickr API.
            keyword (str): The keyword used for searching images.
            flickr (FlickrAPI): The Flickr API instance.

        Methods:
            get_images(keyword, per_page, desired_size, save_directory):
                Retrieves images from Flickr based on the provided keyword and saves them in the specified directory.

    """
    def __init__(self, api_key, api_secret):
        """
        Initializes the FlickrAPI instance.

        Args:
            api_key (str): The API key for accessing the Flickr API.
            api_secret (str): The API secret for accessing the Flickr API.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.keyword = ""
        self.flickr = self._connect()
        

    def _connect(self):
        """
        Connects to the Flickr API using the provided API key and secret.

        Returns:
            FlickrAPI: The FlickrAPI instance.
        """
        try:
            flickr = flickrapi.FlickrAPI(self.api_key, self.api_secret, format="parsed-json")
        except Exception as e :
            print(e)
            return None
        return flickr
    
    def get_images(self, keyword, per_page, desired_size, save_directory):
        """
        Retrieves images from Flickr based on the provided keyword and saves them in the specified directory.

        Args:
            keyword (str): The keyword used for searching images.
            per_page (int): The number of images to retrieve per page.
            desired_size (str): The desired size of the images to download (e.g., 'Large', 'Medium', 'Original', 'small').
            save_directory (str): The directory path where the downloaded images will be saved.

        Returns:
            None
        """
        self.keyword = keyword
        photos = self.flickr.photos.search(text=keyword, per_page = per_page)
        save_dir = f"../img/{save_directory}"
        os.makedirs(save_dir, exist_ok=True)
        
        n_images = len(photos["photos"]["photo"])
        for index, photo in enumerate(photos["photos"]["photo"]):
            photo_id = photo["id"]
            photo_url = self._get_photo_url(photo_id, desired_size)
            if(photo_url):
                image_file_name = f"{photo_id}.jpg"
                file_path = os.path.join(save_dir,image_file_name)
                print(f"{index + 1 } / {n_images} saved")
                urllib.request.urlretrieve(photo_url,file_path)



    def _get_photo_url(self, id, desired_size):
        """
        Retrieves the URL of the desired size of the photo.

        Args:
            id (str): The photo ID.
            desired_size (str): The desired size of the photo.

        Returns:
            str: The URL of the photo in the desired size.
        """
        sizes = self.flickr.photos.getSizes(photo_id = id)
        photo_url = None
        for size in sizes["sizes"]["size"]:
            if size["label"].lower() == desired_size.lower():
                photo_url = size["source"]
                break
        return photo_url


        