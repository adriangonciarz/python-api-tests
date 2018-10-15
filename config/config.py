import yaml

with open("config/config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
    API_URL = cfg['api']['url']
