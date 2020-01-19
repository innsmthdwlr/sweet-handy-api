import json
# from registry_model import Day, Meal, Measurement

class MealParser:
    def __init__(self, registry_file_path):
        self.data = None
        with open(registry_file_path) as f:
            self.data = json.load(f)

    def create_meal(self, meal_data):
        print(f"add {meal_data}")

    def update_registry_file(self):
        print(f"update")
