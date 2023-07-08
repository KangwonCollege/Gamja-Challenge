import os.path

from configparser import ConfigParser
from utils.directory import directory


def get_config() -> ConfigParser:
    path = os.path.join(directory, "config", "token.ini")
    config = ConfigParser()
    config.read(path)
    
    return config