import json
import os


class Utils:

    def validate_json(self, path_to_json):
        if not os.path.isfile(path_to_json):
            with open(path_to_json, "w") as json_file:
                json.dump({}, json_file)
        else:
            if os.path.getsize(path_to_json) == 0:
                with open(path_to_json, "w") as json_file:
                    json.dump({}, json_file)

class ClutterDB:

    def __init__(self, path_to_json: str):
        self.path_to_json = path_to_json
        self.utils = Utils()
        self.utils.validate_json(path_to_json)

    def set(self, key: str, value):
        self.utils.validate_json(self.path_to_json)
        with open(self.path_to_json, mode="r") as json_file:
            json_data = json.load(json_file)
        with open(self.path_to_json, mode="w") as json_file:
            json_data[key] = value
            json.dump(json_data, json_file, indent=4)

    def get(self, key: str, *, default=None):
        self.utils.validate_json(self.path_to_json)
        with open(self.path_to_json, mode="r") as json_file:
            json_data = json.load(json_file)
            return json_data.get(key, default)

    def all(self):
        self.utils.validate_json(self.path_to_json)
        with open(self.path_to_json, mode="r") as json_file:
            return json.load(json_file)

    def rem(self, key: str):
        self.utils.validate_json(self.path_to_json)
        with open(self.path_to_json, mode="r") as json_file:
            json_data = json.load(json_file)
        with open(self.path_to_json, mode="w") as json_file:
            json_data.pop(key, None)
            json.dump(json_data, json_file, indent=4)

    def nuke(self):
        self.utils.validate_json(self.path_to_json)
        with open(self.path_to_json, mode="w") as json_file:
            json.dump({}, json_file)
