# Flickr Image Scraper

Flickr Image Scraper is a Python tool for scraping and downloading images from Flickr based on a keyword.

## Project Structure

The project contains the following files and directories:

- `img/`: The directory where the downloaded images will be saved.
- `src/`: The directory containing the source code of the Flickr Image Scraper.
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ahmedkltn/flickr-image-scraper.git
   ```

1. Install the required dependencies:
    
    ```
    pip install -r requirements.txt
    ```
    

## Usage

1. Set up your Flickr API credentials:
    - Create a Flickr API account at https://www.flickr.com/services/apps/create/.
    - Obtain an API key and API secret.
2. create `.env` file in the root directory of the project.
3. Add your Flickr API key and API secret to the `.env` file:
    
    ```
    FLICKR_API_KEY=your-api-key
    FLICKR_API_SECRET=your-api-secret
    ```
    
- Modify the `src/main.py` file to specify the keyword, number of images per page, desired image size, and save directory.
- Run the script:
    
    ```
    cd src
    python main.py
    ```
    

The script will connect to the Flickr API, search for images based on the provided keyword, and save the downloaded images in the `img/` directory.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License
