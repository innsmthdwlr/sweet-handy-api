import json

class Day:
    def __init__(self, date, meals):
        self.date = date
        self.meals = meals

class Meal:
    def __init__(self, time, image, description, noTag, measurements):
        self.time = time
        self.image = image
        self.description = description
        self.noTag = noTag
        self.measurements = measurements

class Measurement:
    def __init__(self, time, value):
        self.time = time
        self.value = value

class DiabetesEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            iterable = iter(0)
        except TypeError:
            pass
        else:
            return list(iterable)
        return json.JSONEncoder.default(self, o)
