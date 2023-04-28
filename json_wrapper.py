import json

from io import TextIOWrapper
from typing import Any


JsonType = str | int | bool | dict | list | None


class JsonFile:
    def __init__(self, path: str, **kwargs: Any) -> None:
        self.path = path
        self._json_kwargs = kwargs

    def open(self, mode: str = "r", /) -> TextIOWrapper:
        return open(self.path, mode)

    def dump(self, data: dict, /) -> None:
        """Dumps the data to the JSON file."""
        with self.open("w") as file:
            json.dump(data, file, **self._json_kwargs)

    def data(self) -> dict[Any, Any]:
        """Returns the all data in the JSON file."""
        with self.open() as file:
            return json.load(file, **self._json_kwargs)

    def validate(self) -> dict:
        """Validates the JSON file contents and returns them."""
        try:
            data = self.data()

            if not isinstance(data, dict):
                data = {}
                self.dump(data)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
            self.dump(data)

        return data


class JsonWrapper(JsonFile):
    def __init__(self, path: str, /, *, indent: int = 4) -> None:
        super().__init__(path, indent=indent)
        self.validate()

    def get(self, path: str | list[str] = [], /, default: Any = None) -> JsonType:
        """
        Returns the value of the key in given path. If the key is not found in the path, returns the default value.
        For example, if `jw.get("foo.bar.baz")` is called and the JSON is `{"foo": {"bar": {"baz": 123}}}`, `123` will be returned.
        
        Args:
            path: The path to the key. If not given, returns the whole JSON.
            default: The default value.

        Returns:
            The value of the key in given path.
        """
        data = self.validate()
        path = path.split(".") if isinstance(path, str) else path

        for part in path:
            if part not in data:
                return default

            data = data[p]

        return data

    def set(self, path: str | list[str], value: JsonType, /, *, force: bool = False) -> None:
        """Sets the path to the value. If the path is not found, creates the path.
        If the path is blocked by a non-dictionary value, it will raise TypeError, to override this behavior, set force to True.

        Note: Use `JsonWrapper.dump` if you want to set the whole JSON to a dict.

        Args:
            path: The path to set the value in.
            value: The value to set.
            force: If True, it overrides the path if the path is blocked by a non-dictionary value.

        Raises:
            ValueError: If the path is an empty string. See note.
            TypeError: If the path is blocked by a non-dictionary value while force is False.
        """
        data = self.validate()
        data_root = data

        path = path.split(".") if isinstance(path, str) else path

        if not path:
            raise ValueError("Path is empty.")

        # All except the last.
        for p in path[:-1]:
            if p not in data:
                data[p] = {}

            elif not isinstance(data[p], dict):
                if force:
                    data[p] = {}
                else:
                    raise TypeError("Path is blocked by a non-dictionary value. Use force=True to override.")

            data = data[p]

        data[path[-1]] = value

        self.dump(data_root)

    def rem(self, path: str | list[str] = [], /) -> bool:
        """Removes the key in given path.

        Args:
            path: The path to the key. If the path is not given, nukes the whole json.

        Returns:
            bool: True if the key was removed, False if the key was not found.
        """
        data = self.validate()
        data_root = data

        path = path.split(".") if isinstance(path, str) else path

        if not path:
            if data:
                self.dump({})
                return True

            return False

        # All except the last.
        for part in path[:-1]:
            if part not in data or not isinstance(data[part], dict):
                return False

            data = data[part]

        if path[-1] not in data:
            return False

        del data[path[-1]]

        self.dump(data_root)
        return True

    def __getitem__(self, key: str, /) -> JsonType:
        return self.validate()[key]

    def __setitem__(self, key: str, value: Union[str, int, bool, dict, list, None]) -> None:
        data = self.validate()
        data[key] = value
        self.dump(data)

    def __delitem__(self, key: str, /) -> None:
        data = self.validate()
        del data[key]
        self.dump(data)

    def __contains__(self, key: str, /) -> bool:
        return key in self.validate()

    def __repr__(self) -> str:
        return repr(self.validate())

    def __str__(self) -> str:
        return str(self.validate())

    def __reversed__(self):
        return reversed(self.validate())

    def __eq__(self, other: Any, /) -> bool:
        return self.data == other

    def __ior__(self, other: Any) -> bool:
        data = self.validate()
        data |= other
        self.dump(data)        

    def __ror__(self, other: Any) -> bool:
        return other | self.validate()

    def __sizeof__(self) -> bytes:
        return self.validate().__sizeof__()
