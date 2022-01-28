# 📋 Table of Contents
<!-- will be updated soon -->
# *class* `json_wrapper.JsonWrapper(json_path: str)`
### Methods
* [*def* `set(key: str, value, *, pathmagic: (str, list) = "")`](https://github.com/RGBCube/json-wrapper/tree/main/docs#def-setkey-str-value--pathmagic-str-list--)
* [*def* `get(key: str, *, default=None, pathmagic: (str, list) = "")`]() TODO
* [*def* `all()`]() TODO
* [*def* `rem(key: str, *, pathmagic: (str, list) = "")`]() TODO
* [*def* `nuke(*, pathmagic: (str, list) = "")`]() TODO
## *def* `set(key: str, value, *, pathmagic: (str, list) = "")`
Sets the key value pair in the json.

If the pathmagic kwarg is given, (if str)it will split it by the +'s and make dicts inside dicts(or use existing ones) until the list ends. Then it will set the key value pair in the last dict.

#### Args:
* key `(str)`: The key for the key value pair.
* value `(Any)`: The value for the key value pair.
* pathmagic `(Union[str, List[str]], optional)`: The path to follow. Defaults to `""`.

#### [Example Usage]() TODO
