from geopy.geocoders import Nominatim



def find_coordinate(zipcode, country="USA"):
    """Receives an input of a zipcode and an optional country input
    and returns the longitude and latitude of that zipcode"""

    geolocator = Nominatim(user_agent="friender")
    location = geolocator.geocode(f"{zipcode}, {country}")
    print(geolocator.reverse(f"{location.latitude}, {location.longitude}"))
    return location

#BUG STORY
#**** 1254, ဒဂုံဆိပ်ကမ်း, Yangon East, Yangon, ရန်ကုန်တိုင်းဒေသကြီး, မြန်မာ
#**** Свобода, Батівська селищна громада, Берегівський район, 90210, Закарпатська область, Україна