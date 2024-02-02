from geopy.geocoders import Nominatim
import geopy

#TODO:
def find_location():
    print("hit")
    geolocator = Nominatim(user_agent="friender")
    # location = geolocator.reverse("52.509669, 13.376294")
    location = geolocator.geocode('60047-1254')
    print("****", location)
    return location

find_location()

#BUG STORY
#**** 1254, ဒဂုံဆိပ်ကမ်း, Yangon East, Yangon, ရန်ကုန်တိုင်းဒေသကြီး, မြန်မာ
#**** Свобода, Батівська селищна громада, Берегівський район, 90210, Закарпатська область, Україна