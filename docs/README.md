### Table of Contents
* [*class* `json_wrapper.JsonWrapper(json_path: str)`](https://github.com/RGBCube/json-wrapper/tree/main/docs#class-json_wrapperjsonwrapperjson_path-str)
# *class* `json_wrapper.JsonWrapper(json_path: str)`

### Methods
* [*def* `set(key: str, value, *, pathmagic: (str, list) = "")`](https://github.com/RGBCube/json-wrapper/tree/main/docs#def-setkey-str-value--pathmagic-str-list--)
* [*def* `get(key: str, *, default=None, pathmagic: (str, list) = "")`](https://github.com/RGBCube/json-wrapper/blob/main/docs/README.md#def-getkey-str--defaultnone-pathmagic-str-list--)
* [*def* `all()`]() TODO
* [*def* `rem(key: str, *, pathmagic: (str, list) = "")`]() TODO
* [*def* `nuke(*, pathmagic: (str, list) = "")`]() TODO

## *def* `set(key: str, value, *, pathmagic: (str, list) = "")`
Sets the key value pair in the json.

If the pathmagic kwarg is given, (if str)it will split it by the +'s and make dicts inside dicts(or use existing ones) until the list ends. Then it will set the key value pair in the last dict.

#### Args:
* key (`str`): The key for the key value pair.
* value (`Any`): The value for the key value pair.
* pathmagic (`Union[str, List[str]]`, optional): The path to follow. Defaults to `""`.

#### [Example Usage]() TODO

## *def* `get(key: str, *, default=None, pathmagic: (str, list) = "")`
Returns the key's value in the json. Will return the default kwarg if not found.

If the pathmagic kwarg is given, (if str)it will split it by the +'s and follow the dicts inside the dicts until the list ends. Then it will return the value of the key in the last dict. The default kwarg applies.

#### Args:
* key (`str`): The key to get the value of.
* default (`Any`, optional): The value to return if the key is not found. Defaults to `None`.
* pathmagic (`Union[str, List[str]]`, optional): The path to follow. Defaults to `""`.

#### Returns:
* `Any`: The value of the key. Will return the default kwarg if the key is not found.
