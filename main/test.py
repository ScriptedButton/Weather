from weather import Weather

w = Weather("20061", "") # ... is your APIXU key
forecast = w.getForcecast(3)
current = w.getCurrent()

for i in forecast:
    print("Conditions for {0}: ".format(i) + forecast[i].condition_text)

print("Current time: ", current.localtime)