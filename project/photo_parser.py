import flickrapi


class Parser:
    @staticmethod
    def parse(hashtag, flickr):
        locations = []
        photos = flickr.get_api().photos.search(tags=hashtag, per_page=10, extras='url_c', sort='relevance')
        for p in photos['photos']['photo']:
            print('Title: ', p['title'])
            print(f'Url: {p["url_c"]}')
            try:
                location = flickr.get_api().photos.geo.getLocation(photo_id=p['id'])
                print('Latitude: ', location['photo']['location']['latitude'])
                print('Longitude: ', location['photo']['location']['longitude'])
                locations.append(
                    (float(location['photo']['location']['latitude']),
                     float(location['photo']['location']['longitude']),
                     p['title']))

            except flickrapi.exceptions.FlickrError:
                print("This post does not have a location")
            print('----------------------------------------------------------------')

        return locations
