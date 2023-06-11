from FlightRadar24.api import FlightRadar24API

print("Hello world")

fr_api = FlightRadar24API()

flights = fr_api.get_flights()

print(flights)