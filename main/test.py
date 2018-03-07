from weather import Weather

KEY = "..."
LOCATION = "Washington, US"
w = Weather(LOCATION, KEY)
# ... is your APIXU key

forecast = w.getforecast(3)
current = w.getcurrent()

for i in forecast:
    print("Conditions for {0}: ".format(i) + str(forecast[i].Day.avgtemp_f))

print("Current location: ", current.Location.location_name)
