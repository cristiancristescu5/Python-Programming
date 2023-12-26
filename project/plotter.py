import folium
import webbrowser


class Plotter:
    @staticmethod
    def plot(coordinates):
        m = folium.Map(location=[47.60332439417556, 27.25886081239678], zoom_start=2)
        markers = []
        for c in coordinates:
            folium.Marker([c[0], c[1]], popup=c[2]).add_to(m)
        m.save('map.html')
        webbrowser.open('file://C://Users//crist//OneDrive//Desktop//piton//project//map.html')
