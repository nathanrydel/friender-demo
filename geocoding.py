from geopy.geocoders import Nominatim
from models import User
import geodesic



def find_coordinate(zipcode, country="USA"):
    """Receives an input of a zipcode and an optional country input
    and returns the longitude and latitude of that zipcode"""

    geolocator = Nominatim(user_agent="friender")
    location = geolocator.geocode(f"{zipcode}, {country}")
    print(geolocator.reverse(f"{location.latitude}, {location.longitude}"))
    return location

def is_within_radius(location, distance, user):

    users = User.query.filter(User.username != user.username).all()

    nearby_users = []

    user_location = (location.latitude, location.longitude)

    for other in users:
        other_location = find_coordinate(other.zipcode)
        if geodesic(user_location, other_location).km <= distance:
            nearby_users.append(other)


    return nearby_users
#BUG STORY
#**** 1254, ဒဂုံဆိပ်ကမ်း, Yangon East, Yangon, ရန်ကုန်တိုင်းဒေသကြီး, မြန်မာ
#**** Свобода, Батівська селищна громада, Берегівський район, 90210, Закарпатська область, Україна