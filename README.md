# ClutterDB
extremely simple JSON database which behaves like a dict
this was made for ClutterBot (still in development)
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
