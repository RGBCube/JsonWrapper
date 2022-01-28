### Table of Contents
* [*class* `json_wrapper.JsonWrapper(json_path: str)`](#class-json_wrapperjsonwrapperjson_path-str)
# *class* `json_wrapper.JsonWrapper(json_path: str)`

### Methods
* [*def* `set(key: str, value, *, pathmagic: Union[str, List[str] = "")`](#def-setkey-str-value--pathmagic-unionstr-liststr--)
* [*def* `get(key: str, *, default=None, pathmagic: Union[str, List[str] = "")`](#def-getkey-str--defaultnone-pathmagic-unionstr-liststr--)
* [*def* `all()`](#def-all)
* [*def* `rem(key: str, *, pathmagic: Union[str, List[str] = "")`](#def-remself-key-str--pathmagic-unionstr-liststr--)
* [*def* `nuke(*, pathmagic: Union[str, List[str] = "")`](#def-nuke-pathmagic-unionstr-liststr--)

## *def* `set(key: str, value, *, pathmagic: Union[str, List[str] = "")`
Sets the key value pair in the json.

If the pathmagic kwarg is given, (if str)it will split it by the +'s and make dicts inside dicts(or use existing ones) until the list ends. Then it will set the key value pair in the last dict.

#### Args
* key (`str`): The key for the key value pair.
* value (`Any`): The value for the key value pair.
* pathmagic (`Union[str, List[str]]`, optional): The path to follow. Defaults to `""`.

#### [Example Usage]() TODO

## *def* `get(key: str, *, default=None, pathmagic: Union[str, List[str] = "")`
Returns the key's value in the json. Will return the default kwarg if not found.

If the pathmagic kwarg is given, (if str)it will split it by the +'s and follow the dicts inside the dicts until the list ends. Then it will return the value of the key in the last dict. The default kwarg applies.

#### Args
* key (`str`): The key to get the value of.
* default (`Any`, optional): The value to return if the key is not found. Defaults to `None`.
* pathmagic (`Union[str, List[str]]`, optional): The path to follow. Defaults to `""`.

#### Returns
* `Any`: The value of the key. Will return the default kwarg if the key is not found.

#### [Example Usage]() TODO

## *def* `all()`
Returns all the json data.

#### Returns
* `dict`: All the json data.

#### [Example Usage]() TODO

## *def* `rem(self, key: str, *, pathmagic: Union[str, List[str]] = "")`
Removes the key value pair in the json.

If the pathmagic kwarg is given, (if str)it will split it by the +'s and follow the dicts inside the dicts until the list ends. Then it will remove the key value pair in the last dict. Does nothing if the key value pair doesn't exist.

#### Args
* key (`str`): The key to remove.
* pathmagic (`Union[str, List[str]]`, optional): The path to follow. Defaults to `""`.

#### [Example Usage]() TODO

## *def* `nuke(*, pathmagic: Union[str, List[str]] = "")`
Nukes the entire database.

If the pathmagic kwarg is given, (if str)it will split it by the +'s and follow the dicts inside the dicts until the list ends. Then it will nuke the last dict.

#### Args
* pathmagic (`Union[str, List[str]]`, optional): The path to follow. Defaults to `""`.

#### [Example Usage]() TODO
