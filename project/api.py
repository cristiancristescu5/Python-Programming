import yaml
import flickrapi


class Flickr_API:
    def __init__(self):
        with open('conf.yaml', 'r') as f:
            credentials = yaml.safe_load(f)

        self.__key = credentials['api_key']
        self.__secret = credentials['api_secret']
        self.__flicker_api = flickrapi.FlickrAPI(self.__key, self.__secret, format='parsed-json')

    def get_api(self):
        return self.__flicker_api
