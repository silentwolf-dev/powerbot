import json




def require(path):
    with open(path, 'r') as jsonfile:
         return json.loads(jsonfile.read())