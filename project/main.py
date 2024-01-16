import flickrapi
from api import Flickr_API
from photo_parser import Parser
from plotter import Plotter

"""This module contains the main function of the project."""


def main():
    """
    This is the main function of the project. It takes from the user input a hashtag or a list of hashtags and a maximum
    number of posts, and then using the other modules in the project, fetches photos from the Flickr API and the plots
    their locations on a map.
    :return:
    """
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


if __name__ == "__main__":
    main()
