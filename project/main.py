import flickrapi
from api import Flickr_API
flickr = Flickr_API()

hashtag = "nature"
photos = flickr.get_api().photos.search(tags=hashtag, per_page=20, extras='url_c', sor='relevance')

for p in photos['photos']['photo']:
    print('Title: ', p['title'])
    print(f'Url: {p["url_c"]}')
    try:
        location = flickr.get_api().photos.geo.getLocation(photo_id=p['id'])
        print('Latitude: ', location['photo']['location']['latitude'])
        print('Longitude: ', location['photo']['location']['longitude'])
    except flickrapi.exceptions.FlickrError:
        print("This post does not have a location")
    print('----------------------------------------------------------------')
