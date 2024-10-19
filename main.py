from users import Rider, Driver
from vehicle import Car, Bike
from ride import Ride, Ride_matching, Ride_request, Ride_sharing

niya_jao = Ride_sharing("Niya Jao")

rahim = Rider("Rahim", "rahim@gmail.com", 12864, "wari", 500)
niya_jao.add_rider(rahim)

karim = Driver("Karim", "karim@gmail.com", 29723, "banani")
niya_jao.add_driver(karim)

rahim.request_ride(niya_jao, "uttara", "car")

karim.reach_destination(rahim.current_ride)

rahim.show_current_ride()

# print(niya_jao)





