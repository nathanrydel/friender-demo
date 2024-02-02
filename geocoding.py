from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def find_coordinate(zipcode, country="USA"):
    """Receives an input of a zipcode and an optional country input
    and returns the longitude and latitude of that zipcode"""

    geolocator = Nominatim(user_agent="friender")
    location = geolocator.geocode(f"{zipcode}, {country}")
    # print(geolocator.reverse(f"{location.latitude}, {location.longitude}"))
    if location is not None:
        return location
    else:
        print(f"Location not found for zipcode: {zipcode}")

#TODO: Handle non-zipcodes? in route?

def is_within_radius(location, second_location, radius):
    """Receives two location objects of longitude and
    latitude coordinates and a distance in miles. Returns a boolean
    depending on whether the distance between the locations is within
    the allowed radius. """

    return (geodesic((location.latitude, location.longitude),
                     (second_location.latitude, second_location.longitude))
                     .miles <= radius)


#Only accepts USA zipcodes
#TODO: Potentially store longitude and latitude?  Avoid repeated geocoding requests
def find_nearby_users(user, other_users, radius):
    """Receives an input of a user object, an array of user objects, and a
    radius. Returns an array of user objects if those users' zipcodes are within
    the allowed radius of the initial user object."""

    # users = User.query.filter(User.username != user.username).all()

    nearby_users = []

    user_location = find_coordinate(user.zipcode)

    for other_user in other_users:
        other_user_location = find_coordinate(other_user.zipcode)
        if is_within_radius(user_location, other_user_location, radius):
            nearby_users.append(other_user)

    return nearby_users


#BUG STORY
#**** 1254, ဒဂုံဆိပ်ကမ်း, Yangon East, Yangon, ရန်ကုန်တိုင်းဒေသကြီး, မြန်မာ
#**** Свобода, Батівська селищна громада, Берегівський район, 90210, Закарпатська область, Україна
    user_location = (location.latitude, location.longitude)

    for other in users:
        other_location = find_coordinate(other.zipcode)
        if distance.distance(user_location, other_location).miles <= distance:
            nearby_users.append(other)
