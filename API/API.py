
from FlightRadar24.api import FlightRadar24API

print("Hello world")

fr_api = FlightRadar24API()

#login to get extra data if available to account
loginData = fr_api.login("james@live.com.my", "CHICKEN WING")


boundsData = "5.028,3.991,100.162,102.138"
flights = fr_api.get_flights(bounds=boundsData)

foundFlight = flights[0]

details = fr_api.get_flight_details(foundFlight.id)

foundFlight.set_flight_details(details)

print("Age:", foundFlight.aircraft_age)


