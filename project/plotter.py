import folium
import webbrowser
from coordinate import Coordinate

"""This module provides functionality for plotting the coordinates of the photos extracted from flickr API."""


class Plotter:
    """
    This class is used to create the map and plot the coordinates of photos, if applicable. To plot the coordinates
on the map. I used the folium module because it allows you to create interactive maps with various features.
    """
    @staticmethod
    def plot(coordinates: list[Coordinate]):
        """
        This static method plots the given coordinates on a map.
        :param coordinates: The coordinates extracted from the photos.
        :return: Creates the map and the opens it in the browser
        """
        m = folium.Map(location=[39.00, 34.00], zoom_start=2)
        markers = []
        for c in coordinates:
            folium.Marker([c.get_x(), c.get_y()], popup=c.get_label()).add_to(m)
        m.save('map.html')
        url = 'http://localhost:63342/project/project/map.html'
        webbrowser.open(url)
        print(f"Map: {url}")
