import requests
import configparser

class ImageCollector():
    def __init__(self, query):
        self.config = configparser.ConfigParser()
        self.config.read('config.cfg')
        self.image_search_url = self.config['API']['image_search_url']
        self.x_rapidapi_key = self.config['API']['x-rapidapi-key']
        self.x_rapidapi_host = self.config['API']['x-rapidapi-host']
        self.query = query
        
    def find_images(self):
        headers = {
            'x-rapidapi-key': self.x_rapidapi_key,
            'x-rapidapi-host': self.x_rapidapi_host
        }
        params = {
            'q': self.query,
            'pageNumber': 1,
            'pageSize': 50,
            'autoCorrect': True,
            'safeSearch': True
        }
        response = requests.get(self.image_search_url, params=params, headers=headers)
        images_data = response.json()['value']
        image_urls = []
        for image_data in images_data:
            image_urls.append(image_data['url'])
        return image_urls