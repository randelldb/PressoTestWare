import sys

import yaml

config_file = "src/config/config.yml"


def readConfig():
    with open(config_file, "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    return cfg


def writeConfig(parent, child, value):
    with open(config_file, 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)

    cfg[parent][child] = value

    with open(config_file, 'w') as ymlfile:
        yaml.dump(cfg, ymlfile)

