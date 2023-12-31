import flickrapi
from api import Flickr_API
from photo_parser import Parser
from plotter import Plotter

flickr = Flickr_API()

while 1:
    confirm = input("Do you want to continue? yes/no:")
    if confirm == 'no':
        break
    hashtag = input("Enter your hashtags:")
    num_posts = 10  # default

    try:
        num_posts = int(input("Enter the number of posts:"))
    except Exception as e:
        print(e)

    coordinates = Parser.parse(hashtag, flickr, num_posts)
    Plotter.plot(coordinates)

