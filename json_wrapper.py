import json
from typing import Any, Union


class JsonBase:

    def __init__(self, *, fp: str, indent: int) -> None:
        self._fp = fp
        self._indent_size = indent

    @property
    def data(self) -> dict:
        """Returns the all data of the json file."""
        with open(self._fp) as f:
            return json.load(f)

    def dump(self, data: dict) -> None:
        """Dumps the data to the json file."""
        with open(self._fp, mode="w") as f:
            json.dump(data, f, indent=self._indent_size)

    def validate(self) -> None:
        """Validates the json file."""
        try:
            with open(self._fp, mode="r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            with open(self._fp, mode="w") as f:
                json.dump({}, f)
                return
        if not isinstance(data, dict):
            with open(self._fp, mode="w") as f:
                json.dump({}, f)


class JsonWrapper(JsonBase):

    def __init__(self, fp: str, *, indent: int = 4) -> None:
        super().__init__(fp=fp, indent=indent)
        self.validate()

    def get(self, path: str = "", default: Any = None) -> Union[str, int, bool, dict, list, None]:
        """Returns the value of the key in given path. If the key is not found in the path, returns the default value.

        Args:
            path (str): The path to the key. If the path is not given, returns the whole json as a dict.
            default (Any): The default value.

        Returns:
            Union[str, int, bool, dict, list, None]: The value of the key in given path.
        """
        self.validate()
        path, data = [p for p in path.split(".") if p != ""], self.data
        for p in path:
            if p not in data:
                return default
            data = data[p]
        return data

    def set(self, path: str, value: Union[str, int, bool, dict, list, None], *, force: bool = False) -> None:
        """Sets the path to the value. If the path is not found, creates the path.
        If the path is blocked by a non-dictionary value, it will raise TypeError, to override this behavior, set force to True.

        Args:
            path (str): The path to set the value in.
            value (Union[str, int, bool, dict, list, None]): The value to set.
            force (bool): If True, it overrides the path if the path is blocked by a non-dictionary value.

        Raises:
            ValueError: If the path is an empty string.
            TypeError: If the path is blocked by a non-dictionary value and force is False.
        """
        self.validate()
        path, data = [p for p in path.split(".") if p != ""], self.data
        reference = data
        if not path:
            raise ValueError("Path is empty.")
        for p in path[:-1]:
            if p not in data.keys():
                data[p] = {}
            elif not isinstance(data[p], dict):
                if force:
                    data[p] = {}
                else:
                    raise TypeError("Path is blocked by a non-dictionary value. Use force=True to override.")
            data = data[p]
        data[path[-1]] = value
        self.dump(reference)

    def rem(self, path: str = "") -> bool:
        """Removes the key in given path.

        Args:
            path (str): The path to the key. If the path is not given, nukes the whole json.

        Returns:
            bool: True if the key was removed, False if the key was not found.
        """
        self.validate()
        path, data = [p for p in path.split(".") if p != ""], self.data
        reference = data
        if not path:
            if data:
                self.dump({})
                return True
            return False
        for p in path[:-1]:
            if p not in data.keys():
                return False
            elif not isinstance(data[p], dict):
                return False
            data = data[p]
        if path[-1] not in data.keys():
            return False
        del data[path[-1]]
        self.dump(reference)
        return True

    def __contains__(self, key: str) -> bool:
        self.validate()
        return key in self.data

    def __delitem__(self, key: str) -> None:
        self.validate()
        data = self.data
        del data[key]
        self.dump(data)

    def __eq__(self, other: Any) -> bool:
        return self.data == other

    def __getitem__(self, key: str) -> Union[str, int, bool, dict, list, None]:
        self.validate()
        return self.data[key]

    def __ge__(self, other: Any) -> bool:
        self.validate()
        return self.data >= other

    def __gt__(self, other: Any) -> bool:
        self.validate()
        return self.data > other

    def __ior__(self, other) -> None:
        self.validate()
        data = self.data
        data.update(other)
        self.dump(data)

    def __iter__(self):
        self.validate()
        return iter(self.data)

    def __len__(self) -> int:
        self.validate()
        return len(self.data)

    def __le__(self, other: Any) -> bool:
        self.validate()
        return self.data <= other

    def __lt__(self, other: Any) -> bool:
        self.validate()
        return self.data < other

    def __ne__(self, other: Any) -> bool:
        self.validate()
        return self.data != other

    def __or__(self, other: Any) -> Any:
        self.validate()
        return self.data | other

    def __repr__(self) -> str:
        self.validate()
        return repr(self.data)

    def __reversed__(self):
        self.validate()
        return reversed(self.data)

    def __ror__(self, other: Any) -> bool:
        self.validate()
        return other | self.data

    def __setitem__(self, key: str, value: Union[str, int, bool, dict, list, None]) -> None:
        self.validate()
        data = self.data
        data[key] = value
        self.dump(data)

    def __sizeof__(self) -> bytes:
        self.validate()
        return bytes(self.data)
