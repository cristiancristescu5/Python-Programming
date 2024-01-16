import yaml
import flickrapi

"""This module is used for connecting to the flickr API."""


class Flickr_API:
    """This class is used to generate the connection to the Flickr API"""
    def __init__(self):
        """
            The constructor opens a .yaml file that contains the credentials required to connect to the API,
            and the generates a FlickrAPI object, used to make requests to the API
        """
        with open('conf.yaml', 'r') as f:
            credentials = yaml.safe_load(f)

        self.__key = credentials['api_key']
        self.__secret = credentials['api_secret']
        self.__flicker_api = flickrapi.FlickrAPI(self.__key, self.__secret, format='parsed-json')

    def get_api(self):
        """
        :return: The FlickrAPI object used to make requests.
        """
        return self.__flicker_api
