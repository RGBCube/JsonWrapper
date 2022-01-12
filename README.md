# ClutterDB
extremely simple JSON database which behaves like a dict
this was made for ClutterBot (still in development)
# Docs
### `db.set(key: str, value)`
Sets the key to the value in the JSON.
### `db.rem(key: str)`
Removes the key and value pair from the JSON.
Note that this will not do anything if the key isn't set in the JSON.
### `db.get(key: str, default=None)`
Returns the value of the key in the json, if the key isn't set in the json, it returns the default kwarg.
### `db.nuke()`
Deletes everything in the JSON.
Use with caution.
# Usage
```python
from db import ClutterDB

# initialization
db = ClutterDB("path/to/json/file.json")

# defining a variable 
# (this will overrride the previous a if it was defined before)
db.set("a", 12345)

# getting a variable 
# (default kwarg will be returned if the key was not defined in the json)
data = db.get("a", default="a was not defined in the json")

# prints data
print(data)

# removes the a from the json
db.rem("a")

# nukes the json
db.nuke()
```
