import requests


class Day:
    """Used for finding information on a weekday."""

    class Astro:
        def __init__(self, astro):
            self.sunrise = astro['sunrise']
            self.sunset = astro['sunset']
            self.moonrise = astro['moonrise']
            self.moonset = astro['moonset']

    class Main:
        def __init__(self, day):
            self.day = day
            self.maxtemp_c = day['maxtemp_c']
            self.maxtemp_f = day['maxtemp_f']
            self.mintemp_c = day['mintemp_c']
            self.mintemp_f = day['mintemp_f']
            self.avgtemp_c = day['avgtemp_c']
            self.avgtemp_f = day['avgtemp_f']
            self.maxwind_mph = day['maxwind_kph']
            self.totalprecip_mm = day['totalprecip_mm']
            self.totalprecip_in = day['totalprecip_in']
            self.avgvis_km = day['avgvis_km']
            self.avgvis_miles = day['avgvis_miles']
            self.avghumidity = day['avghumidity']

    class Condition:
        def __init__(self, condition):
            self.condition_text = condition['text']
            self.condition_icon = condition['icon']

    def __init__(self, data):
        self.data = data
        self.date = data['date']
        self.Day = self.Main(data['day'])
        self.Astro = self.Astro(data['astro'])
        self.Condition = self.Condition(self.Day.day['condition'])


class CurrentDay:
    """Used for finding information on a current day."""
    class Location:
        def __init__(self, location):
            self.location_name = location['name']
            self.location_region = location['region']
            self.location_country = location['country']
            self.location_coords = (location['lat'], location['lon'])
            self.tz_id = location['tz_id']
            self.localtime_epoch = location['localtime_epoch']
            self.localtime = location['localtime']

    class Current:
        def __init__(self, current):
            self.condition = current['condition']
            self.last_updated_epoch = current['last_updated_epoch']
            self.last_updated = current['last_updated']
            self.temp_c = current['temp_c']
            self.temp_f = current['temp_f']
            self.is_day = current['is_day']
            self.wind_mph = current['wind_mph']
            self.wind_kph = current['wind_kph']
            self.wind_degree = current['wind_degree']
            self.wind_dir = current['wind_dir']
            self.pressure_mb = current['pressure_mb']
            self.pressure_in = current['pressure_in']
            self.precip_mm = current['precip_mm']
            self.precip_in = current['precip_in']
            self.humidity = current['humidity']
            self.cloud = current['cloud']
            self.feelslike_c = current['feelslike_c']
            self.feelslike_f = current['feelslike_f']
            self.vis_km = current['vis_km']
            self.vis_miles = current['vis_miles']

    class Condition:
        def __init__(self, condition):
            self.condition_text = condition['text']
            self.condition_icon = condition['icon']

    def __init__(self, day):
        self.Location = self.Location(day['location'])
        self.Current = self.Current(day['current'])
        self.Condition = self.Condition(self.Current.condition)


class Weather:
    """Handler"""
    def __init__(self, location, key):
        self.location = location
        self.key = key
        status = requests.get("http://api.apixu.com/v1/current.json?key={0}&q={1}".format(key, location)).status_code
        if status != 200:
            raise ConnectionError("There was an issue connecting to the weather API!")

    def getforecast(self, days):
        """Returns the weather forecast an a dictionary."""
        data = {}
        forecast = requests.get("http://api.apixu.com/v1/forecast.json?key={2}&q={0}&days={1}".format(self.location, days, self.key)).json()

        week = forecast['forecast']['forecastday']
        for day in week:
            date = day['date']
            data[date] = Day(day)
        return data

    def getcurrent(self):
        """Returns the current weather as a CurrentDay object."""
        day = requests.get("http://api.apixu.com/v1/current.json?key={1}&q={0}".format(self.location, self.key)).json()
        return CurrentDay(day)
