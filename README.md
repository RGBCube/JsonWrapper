# ClutterDB
Extremely simple JSON database which behaves like a dict.

This was made for ClutterBot (still in development).
# Usage
Clone [this](https://github.com/Clutter-Cluster/ClutterDB/blob/main/db.py) file into your project folder.

Add `from db import CluttterDB` to the top of your project.
# Docs
## `db.set(key: str, value, *, pathmagic="")`
Sets the key to the value in the JSON.
if the `pathmagic` is given, it will spit it by the `+`'s and make dicts(or use existing ones) until it finishes, then it will set the value to the key in the last dict.
## `db.get(key: str, *, default=None)`
Returns the value of the key in the json, if the key isn't set in the json, it returns the default kwarg.
## `db.all()`
Returns all the JSON data.
## `db.rem(key: str)`
Removes the key and value pair from the JSON.

Note that this will not do anything if the key isn't set in the JSON.
## `db.nuke()`
Deletes everything in the JSON.

Use with caution.
# Examples
## `db.set("test", 123)`
Code
```python
from db import ClutterDB

db = ClutterDB("db.json")

db.set("test", 123)

data = db.all()

print(data)
```
Output
`{'test': 123}`
## `db.rem("test")`
Code
```python
from db import ClutterDB

db = ClutterDB("db.json")

db.set("test", 123)

data = db.all()

print(data)

db.rem("test")

data = db.all()

print(data)
```
Output
`{'test': 123}
{}`
