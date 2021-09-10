import yaml
import os

with open('config.yaml', 'r') as stream:
    data = yaml.safe_load(stream)

def get_config(module):
    module = os.path.basename(module).split('.')[0]
    return data[module]

