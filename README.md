# 🈷️ JsonWrapper
Easy JSON wrapper packed with features. 
# 📥 Usage
Execute `pip install json_wrapper`.

Add `from json_wrapper import JsonWrapper` to the top of your project.
# 📄 Docs
> Assume that we did `db = JsonWrapper("example.json)`
## `db.set(key: str, value, *, pathmagic="")`
Sets the key to the value in the JSON.

if the `pathmagic` kwarg is given, it will spit it by the `+`'s and make dicts(or use existing ones) until it finishes, then it will set the value to the key in the last dict.

Note that the `pathmagic` kwarg will override its path if it isnt a dict.
## `db.get(key: str, *, default=None, pathmagic="")`
Returns the value of the key in the json, if the key isn't set in the json, it returns the default kwarg.

if the `pathmagic` kwarg is given, it will spit it by the `+`'s and follow the path in it in the JSON data, it will return the `default` kwarg if the path is empty or has a value that isnt a dict.
## `db.all()`
Returns all the JSON data.
## `db.rem(key: str, *, pathmagic="")`
Removes the key and value pair from the JSON.

Note that this will not do anything if the key isn't set in the JSON or the path is invalid.

if the `pathmagic` kwarg is given, it will spit it by the `+`'s and follow the path in it in the JSON data, then it will remove the key and value pair.
## `db.nuke()`
Deletes everything in the JSON.

Use with caution.
# 📘 Examples
> Assume that the `example.json` file is empty
## `db.set()`
### Normal usage
Code
```python
from json_wrapper import JsonWrapper

db = JsonWrapper("example.json")

db.set("test", 123)

data = db.all()

print(data)
```
Output
```
{'test': 123}
```
### Using with `pathmagic` kwarg
Code
```python
from json_wrapper import JsonWrapper

db = JsonWrapper("example.json")

db.set("test", 123, pathmagic="a+b+c")

data = db.all()

print(data)
```
Output
```
{'a': {'b': {'c': {'test': 123}}}}
```
## `db.get()`
### Normal usage
Code
```python
from json_wrapper import JsonWrapper

db = JsonWrapper("example.json")

db.set("test", 123)

data = db.get("test")

print(data)
```
Output
```
123
```
### Using without `default` kwarg
Code
```python
from json_wrapper import JsonWrapper

db = JsonWrapper("example.json")

data = db.get("test")

print(data)
```
Output
```
None
```
### Using with `default` kwarg
Code
```python
from json_wrapper import JsonWrapper

db = JsonWrapper("example.json")

data = db.get("test", default=123)

print(data)
```
Output
```
123
```
### Using with `pathmagic` kwarg
Code
```python
from json_wrapper import JsonWrapper

db = JsonWrapper("example.json")

db.set("test", 123, pathmagic="a+b+c")

data = db.get("test", pathmagic="a+b+c")

print(data)
```
Output
```
123
```
## `db.rem()`
### Normal usage
Code
```python
from json_wrapper import JsonWrapper

db = JsonWrapper("example.json")

db.set("test", 123)

data = db.all()

print(data)

db.rem("test")

data = db.all()

print(data)
```
Output
```
{'test': 123}
{}
```
### Using with `pathmagic` kwarg
Code
```python
from json_wrapper import JsonWrapper

db = JsonWrapper("example.json")

db.set("test", 123, pathmagic="a+b+c")

data = db.all()

print(data)

db.rem("test", pathmagic="a+b+c")

data = db.all()

print(data)
```
Output
```
{'a': {'b': {'c': {'test': 123}}}}
{'a': {'b': {'c': {}}}}
```
