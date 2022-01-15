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

    def path_magic(self, main_dict: dict, path: str, *, key: str, value):
        def magic(alt_dict: dict, key: str):
            if key in alt_dict.keys():
                return alt_dict
            else:
                alt_dict[key] = {}
                return alt_dict
        exec_str = "main_dict"
        for dict_name in path.split("+"):
            exec_str = f"magic({exec_str}, '{dict_name}')['{dict_name}']"
            if path.index(dict_name) == len(path) - 1:
                exec_str = f"{exec_str}['{key}'] = {value}"
        exec(exec_str)
        return main_dict

class ClutterDB:

    def __init__(self, path_to_json: str):
        self.path_to_json = path_to_json
        self.utils = Utils()
        self.utils.validate_json(path_to_json)

    def set(self, key: str, value, *, pathmagic=""):
        self.utils.validate_json(self.path_to_json)
        with open(self.path_to_json, mode="r") as json_file:
            json_data = json.load(json_file)
        with open(self.path_to_json, mode="w") as json_file:
            if pathmagic == "":
                json_data[key] = value
                json.dump(json_data, json_file, indent=4)
            else:
                json.dump(self.utils.path_magic(json_data, pathmagic, key=key, value=value), json_file, indent=4)

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
