import json


class ConfigUtils:
    with open("config.json") as file:
        data = json.load(file)

    @classmethod
    def get_attribute(cls, key):
        return cls.data[key]
