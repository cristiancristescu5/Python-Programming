import flickrapi
from api import Flickr_API
from photo_parser import Parser
from plotter import Plotter

flickr = Flickr_API()

hashtag = "nature"

coordinates = Parser.parse(hashtag, flickr)

Plotter.plot(coordinates)

