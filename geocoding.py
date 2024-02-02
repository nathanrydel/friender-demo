from geopy.geocoders import Nominatim
from geopy.distance import geodesic

#Only accepts USA zipcodes
def find_coordinates(zipcode, country="USA"):
    """Receives an input of a zipcode and an optional country input
    and returns the longitude and latitude of that zipcode"""

    geolocator = Nominatim(user_agent="friender")
    location = geolocator.geocode(f"{zipcode}, {country}")
    if location is not None:
        return location
    else:
        return None


def is_within_radius(location, second_location, radius):
    """Receives two location objects of longitude and
    latitude coordinates and a distance in miles. Returns a boolean
    depending on whether the distance between the locations is within
    the allowed radius. """

    return (geodesic((location["latitude"], location["longitude"]),
                     (second_location["latitude"], second_location["longitude"]))
                     .miles <= radius)


def find_nearby_users(user, other_users, radius):
    """Receives an input of a user object, an array of user objects, and a
    radius. Returns an array of user objects if those users' zipcodes are within
    the allowed radius of the initial user object."""

    nearby_users = []

    user_location = {"latitude": user.latitude, "longitude": user.longitude}

    if user.latitude == None or user.longitude == None:
        raise ValueError("Invalid Zipcode")

    for other_user in other_users:
        if other_user.latitude and other_user.longitude:
            other_user_location = {"latitude": other_user.latitude,
                                   "longitude": other_user.longitude}
            if is_within_radius(user_location, other_user_location, radius):
                nearby_users.append(other_user)

    return nearby_users


