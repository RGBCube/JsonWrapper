import json
import os


class Utils:

    @staticmethod
    def validate_json(path_to_json):
        if not os.path.isfile(path_to_json):
            with open(path_to_json, "w") as json_file:
                json.dump({}, json_file)
        else:
            if os.path.getsize(path_to_json) == 0:
                with open(path_to_json, "w") as json_file:
                    json.dump({}, json_file)

    class PathMagic:

        @staticmethod
        def set(main_dict: dict, path: str, *, key: str, value):
            def magic(alt_dict: dict, key: str):
                if key in alt_dict.keys() and isinstance(alt_dict[key], dict):
                    return alt_dict
                alt_dict[key] = {}
                return alt_dict
            main_dict_ref, i = main_dict, 0
            for dict_name in path.split("+"):
                i += 1
                main_dict = magic(main_dict, dict_name)[dict_name]
                if i == len(path.split("+")):
                    main_dict[key] = value
            return main_dict_ref
    
        @staticmethod
        def get(main_dict: dict, path: str, *, key, default=None):
            for dict_name in path.split("+"):
                try:
                    main_dict = main_dict[dict_name]
                except (KeyError, TypeError, AttributeError):
                    return default
            return main_dict.get(key, default)
        
        @staticmethod
        def rem(main_dict: dict, path: str, *, key):
            main_dict_ref, i = main_dict, 0
            for dict_name in path.split("+"):
                try:
                    i += 1
                    main_dict = main_dict[dict_name]
                    if i == len(path.split("+")):
                        main_dict.pop(key, None)
                except (KeyError, TypeError, AttributeError):
                    return main_dict_ref
            return main_dict_ref

class JsonWrapper:

    def __init__(self, path_to_json: str):
        self.path_to_json = path_to_json
        self.utils = Utils
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
                json.dump(self.utils.PathMagic.set(json_data, pathmagic, key=key, value=value), json_file, indent=4)

    def get(self, key: str, *, default=None, pathmagic=""):
        self.utils.validate_json(self.path_to_json)
        with open(self.path_to_json, mode="r") as json_file:
            json_data = json.load(json_file)
            if pathmagic == "":
                return json_data.get(key, default) 
            else:
                return self.utils.PathMagic.get(json_data, pathmagic, key=key, default=default)

    def all(self):
        self.utils.validate_json(self.path_to_json)
        with open(self.path_to_json, mode="r") as json_file:
            return json.load(json_file)

    def rem(self, key: str, *, pathmagic=""):
        self.utils.validate_json(self.path_to_json)
        with open(self.path_to_json, mode="r") as json_file:
            json_data = json.load(json_file)
        with open(self.path_to_json, mode="w") as json_file:
            if pathmagic == "":
                json_data.pop(key, None)
                json.dump(json_data, json_file, indent=4)
            else:
                json.dump(self.utils.PathMagic.rem(json_data, pathmagic, key=key), json_file, indent=4)

    def nuke(self):
        with open(self.path_to_json, mode="w") as json_file:
            json.dump({}, json_file)
