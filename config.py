import configparser
from keys import keys

def config_groups() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read("config.ini")
    if "keys" not in config:
        config["keys"] = keys
        with open("config.ini", "w") as configfile:
            config.write(configfile)
    return config

def config_colors() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read("colors.ini")
    if "colors" not in config:
        config["colors"] = {
            "groupname": "#00000"
        }
    if "groups" not in config:
        config["groups"] = {
            "groupname": "Esc, F1, F2, F3",
            "groupname2": "F10 F11 F12"
        }
    with open("colors.ini", "w") as configfile:
        config.write(configfile)
    return config
