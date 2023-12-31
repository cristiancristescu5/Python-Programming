import folium
import webbrowser
from coordinate import Coordinate


class Plotter:
    @staticmethod
    def plot(coordinates: list[Coordinate]):
        m = folium.Map(location=[39.00, 34.00], zoom_start=2)
        markers = []
        for c in coordinates:
            folium.Marker([c.get_x(), c.get_y()], popup=c.get_label()).add_to(m)
        m.save('map.html')
        url = 'http://localhost:63342/project/project/map.html'
        webbrowser.open(url)
        print(f"Map: {url}")
