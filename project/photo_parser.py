import flickrapi
from coordinate import Coordinate


class Parser:
    @staticmethod
    def parse(hashtag, flickr, num_posts):
        locations = []
        photos = flickr.get_api().photos.search(tags=hashtag, per_page=num_posts, extras='url_c'
                                                , sort='date-posted-desc')
        for p in photos['photos']['photo']:
            print('Title: ', p['title'])
            try:
                print(f'Url: {p["url_c"]}')
            except Exception as e:
                print("Url Error")
            try:
                location = flickr.get_api().photos.geo.getLocation(photo_id=p['id'])
                print('Latitude: ', location['photo']['location']['latitude'])
                print('Longitude: ', location['photo']['location']['longitude'])
                locations.append(Coordinate
                                 (float(location['photo']['location']['latitude']),
                                  float(location['photo']['location']['longitude']),
                                  p['title']))

            except flickrapi.exceptions.FlickrError:
                print("This post does not have a location")
            print('----------------------------------------------------------------')

        return locations
