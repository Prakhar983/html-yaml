import yaml

with open('output2.yaml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)

print(data)
