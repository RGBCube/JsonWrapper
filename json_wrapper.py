import json
import os
from typing import Any, Union, List


class _JsonUtils:

    def __init__(self, json_path: str) -> None:
        self.json_path = json_path

    def data(self) -> dict:
        """Returns all the json data.

        Returns:
            dict: All the json data.
        """
        with open(self.json_path, mode="r") as json_file:
            return json.load(json_file)

    def dump(self, data: dict) -> None:
        """Dumps the dict into the json.

        Args:
            data (dict): The data to dump.
        """
        with open(self.json_path, mode="w") as json_file:
            json.dump(data, json_file, indent=4)

    def validate(self) -> None:
        """Validates the json if the json is not a valid dict.
        """
        try:
            with open(self.json_path, mode="r") as json_file:
                data = json.load(json_file)

        except (FileNotFoundError, json.JSONDecodeError):
            with open(self.json_path, mode="w") as json_file:
                json.dump({}, json_file)
                return

        if not isinstance(data, dict):
            with open(self.json_path, mode="w") as json_file:
                json.dump({}, json_file)


class _PathMagic:

    @staticmethod
    def set(main_dict: dict, path: Union[str, List[str]], *, dump: dict) -> dict:
        """Sets the key value pair in the path given. Will override.

        Args:
            main_dict (dict): The dict to modify.
            path (Union[str, List[str]]): The path to follow.
            dump (dict): The key value pairs to set in the last scope.

        Returns:
            dict: The modified dict.
        """
        def magic(alt_dict: dict, key: str) -> dict:
            """Validates the key(dict) in the alt_dict.

            Args:
                alt_dict (dict): The dict to modify.
                key (str): The key to validate(dict).

            Returns:
                dict: The modified dict.
            """
            if key in alt_dict.keys() and isinstance(alt_dict[key], dict):
                return alt_dict

            alt_dict[key] = {}
            return alt_dict

        main_dict_ref, i = main_dict, 0

        if isinstance(path, str):
            path = path.split("+")

        for dict_name in path:
            i += 1
            main_dict = magic(main_dict, dict_name)[dict_name]

            if i == len(path):
                main_dict.update(dump)

        return main_dict_ref

    @staticmethod
    def get(main_dict: dict, path: Union[str, List[str]], *, key: str, default=None) -> Any:
        """Gets the value for the key in the path given. Will return the default kwarg if the key can't be found.

        Args:
            main_dict (dict): The dict to get the value of the key in.
            path (Union[str, List[str]]): The path to follow.
            key (str): The key to get the value of.
            default ([type], optional): The value to return if the key is not found. Defaults to None.

        Returns:
            Any: The value of the key. Will return the default kwarg if the key is not found.
        """
        if isinstance(path, str):
            path = path.split("+")

        for dict_name in path:
            try:
                main_dict = main_dict[dict_name]

            except (KeyError, TypeError, AttributeError):
                return default

        return main_dict.get(key, default)

    @staticmethod
    def rem(main_dict: dict, path: Union[str, List[str]], *, key: str) -> dict:
        """Removes a key value pair from the path given.

        Args:
            main_dict (dict): The dict to modify.
            path (Union[str, List[str]]):The path to follow.
            key (str): The key for the key value pair to remove.

        Returns:
            dict: The modified dict.
        """
        main_dict_ref, i = main_dict, 0

        if isinstance(path, str):
            path = path.split("+")

        for dict_name in path:
            try:
                i += 1
                main_dict = main_dict[dict_name]
                if i == len(path):
                    main_dict.pop(key, None)

            except (KeyError, TypeError, AttributeError):
                return main_dict_ref

        return main_dict_ref

    @staticmethod
    def nuke(main_dict: dict, path: Union[str, List[str]]) -> dict:
        """Nukes the given path in the main_dict.

        Args:
            main_dict (dict): The dict to modify.
            path (Union[str, List[str]]): The path to follow.

        Returns:
            dict: The modified dict.
        """
        main_dict_ref, i = main_dict, 0

        if isinstance(path, str):
            path = path.split("+")

        if len(path) == 1:  # lazy but works
            main_dict[path[-1]] = {}

        else:
            for dict_name in path:
                try:
                    i += 1
                    main_dict = main_dict[dict_name]
                    if i == len(path) - 1:
                        main_dict[path[-1]] = {}
                        break

                except (KeyError, TypeError, AttributeError):
                    return main_dict_ref

        return main_dict_ref


class JsonWrapper:

    def __init__(self, json_path: str) -> None:
        self.json_path = json_path
        self.pathmagic = _PathMagic
        self.json = _JsonUtils(json_path)
        self.json.validate()

    def set(self, key: str, value, *, pathmagic: Union[str, List[str]] = "") -> None:
        """Sets the key value pair in the json. If the pathmagic kwarg is given, (if str)it will split it by the +'s and make dicts inside dicts(or use existing ones) until the list ends. Then it will set the key value pair in the last dict.

        Args:
            key (str): The key for the key value pair.
            value ([type]): The value for the key value pair.
            pathmagic (Union[str, List[str]], optional): The path to follow. Defaults to "".
        """
        self.json.validate()

        json_data = self.json.data()

        if pathmagic == "" or pathmagic == []:
            json_data[key] = value
            self.json.dump(json_data)

        else:
            self.json.dump(self.pathmagic.set(
                json_data, pathmagic, dump={key: value}))

    def get(self, key: str, *, default=None, pathmagic: Union[str, List[str]] = "") -> Any:
        """Returns the key's value in the json. Will return the default kwarg if not found. If the pathmagic kwarg is given, (if str)it will split it by the +'s and follow the dicts inside the dicts until the list ends. Then it will return the value of the key in the last dict. The default kwarg applies.

        Args:
            key (str): The key to get the value of.
            default ([type], optional): The value to return if the key is not found. Defaults to None.
            pathmagic (Union[str, List[str]], optional): The path to follow. Defaults to "".

        Returns:
            Any: The value of the key. Will return the default kwarg if the key is not found.
        """
        self.json.validate()

        json_data = self.json.data()

        if pathmagic == "" or pathmagic == []:
            return json_data.get(key, default)

        else:
            return self.pathmagic.get(json_data, pathmagic, key=key, default=default)

    def all(self) -> dict:  # The same as _JsonUtils.data()
        """Returns all the json data.

        Returns:
            dict: All the json data.
        """
        self.json.validate()

        return self.json.data()

    def rem(self, key: str, *, pathmagic: Union[str, List[str]] = "") -> None:
        """Removes the key value pair in the json. If the pathmagic kwarg is given, (if str)it will split it by the +'s and follow the dicts inside the dicts until the list ends. Then it will remove the key value pair in the last dict. Does nothing if the key value pair doesn't exist.

        Args:
            key (str): The key to remove.
            pathmagic (Union[str, List[str]], optional): The path to follow. Defaults to "".
        """
        self.json.validate()

        json_data = self.json.data()

        if pathmagic == "" or pathmagic == []:
            json_data.pop(key, None)
            self.json.dump(json_data)

        else:
            self.json.dump(self.pathmagic.rem(
                json_data, pathmagic, key=key))

    def nuke(self, *, pathmagic: Union[str, List[str]] = "") -> None:
        """Nukes the entire database. If the pathmagic kwarg is given, (if str)it will split it by the +'s and follow the dicts inside the dicts until the list ends. Then it will nuke the last dict.

        Args:
            pathmagic (Union[str, List[str]], optional): The path to follow. Defaults to "".
        """
        if pathmagic == "" or pathmagic == []:
            self.json.dump({})

        else:
            self.json.dump(self.pathmagic.nuke(self.json.data(), pathmagic))
