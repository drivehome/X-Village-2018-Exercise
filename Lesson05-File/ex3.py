import json

with open('show.json',encoding='utf-8') as f:
    show = json.load(f)
    print(show)
    print(json.dumps(show, indent=4))