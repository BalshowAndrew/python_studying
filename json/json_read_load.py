import json

with open('json/sw_templates.json') as f:
    templates = json.load(f)

print(templates)


for section, commands in templates.items():
    print(section)
    print('\n'.join(commands))
