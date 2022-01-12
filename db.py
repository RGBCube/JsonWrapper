import json
import os


class ClutterDB:

    def __init__(self, path_to_json: str):
        self.path_to_json = path_to_json
        if not os.path.isfile(path_to_json):
            with open(path_to_json, "w") as json_file:
                json.dump({}, json_file)
        else:
            if os.path.getsize(path_to_json) == 0:
                with open(path_to_json, "w") as json_file:
                    json.dump({}, json_file)

    def set(self, key: str, value):
        with open(self.path_to_json, mode="r") as json_file:
            json_data = json.load(json_file)
        with open(self.path_to_json, mode="w") as json_file:
            json_data[key] = value
            json.dump(json_data, json_file, indent=4)

    def get(self, key: str, **kwargs):
        with open(self.path_to_json, mode="r") as json_file:
            json_data = json.load(json_file)
            if key in json_data:
                return json_data[key]
            elif "default" in kwargs:
                return kwargs["default"]
            else:
                return None

    def rem(self, key: str):
        with open(self.path_to_json, mode="r") as json_file:
            json_data = json.load(json_file)
        with open(self.path_to_json, mode="w") as json_file:
            json_data.pop(key, None)
            json.dump(json_data, json_file, indent=4)

    def nuke(self):
        with open(self.path_to_json, mode="w") as json_file:
            json.dump({}, json_file)
