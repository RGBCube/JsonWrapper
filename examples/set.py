from json_wrapper import JsonWrapper  # Initialization

db = JsonWrapper("example.json")  # Initialization


# set normal
db.set("a", 123)

data = db.all()

print(data)  # {'a': 123}

db.nuke()


# set pathmagic
db.set("a", 123, pathmagic="example+path")

data = db.all()

print(data)  # {'example': {'path': {'a': 123}}}

db.nuke()
