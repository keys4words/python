import json

a = {
    'name': 'Max',
    'age': 42,
    'marks':[90, 50, 80, 40],
    'pass': True,
    'object': {
        'color': ('red', 'blue')
    }
}

# print(json.dumps(a, indent=1, sort_keys=True))

# print(json.dumps({"name": "Max", "age": 22}))
# print(json.dumps(["1", "2"]))
# print(json.dumps(("1", "2")))
# print(json.dumps("Hello World"))
# print(json.dumps(100))
# print(json.dumps(34.43))
# print(json.dumps(False))
# print(json.dumps(True))
# print(json.dumps(None))


with open('demo.json', 'r') as fh:
    # fh.write(json.dumps(a, indent=1, sort_keys=True))
    json_str = fh.read()
    json_value = json.loads(json_str)
    print(json_value['name'])

with open('sample.json', 'r') as fh:
    # fh.write(json.dumps(a, indent=1, sort_keys=True))
    json_str = fh.read()
    json_value = json.loads(json_str)
    print(json_value['phone'][2])