import configparser
from keys import keys
import logging

logger = logging.getLogger(__name__)

def config_groups() -> configparser.ConfigParser:
    logger.debug("Parsing groups")
    config = configparser.ConfigParser()
    logger.debug("Reading config.ini")
    config.read("config.ini")
    if "keys" not in config:
        logger.warning("keys is not in config, adding default keys instead")
        config["keys"] = keys
        logger.debug(f"keys defaults: {config['keys']}")
        with open("config.ini", "w") as configfile:
            logger.debug("Writing config.ini")
            config.write(configfile)
    return config

def config_colors() -> configparser.ConfigParser:
    logger.debug("Parsing colors")
    config = configparser.ConfigParser()
    logger.debug("Reading colors.ini")
    config.read("colors.ini")
    if "colors" not in config:
        logger.warning("colors is not in config, adding default colors instead")
        config["colors"] = {
            "groupname": "#00000"
        }
        logger.debug(f"colors defaults: {config['colors']}")
    if "groups" not in config:
        logger.warning("groups is not in config, adding default groups instead")
        config["groups"] = {
            "groupname": "Esc, F1, F2, F3",
            "groupname2": "F10 F11 F12"
        }
        logger.debug(f"groups defaults: {config['groups']}")
    with open("colors.ini", "w") as configfile:
        logger.debug("Writing colors.ini")
        config.write(configfile)
    return config
