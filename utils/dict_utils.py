class DictUtils:
    @staticmethod
    def get_value(text):
        dict_text = {}
        pairs = text[:-1].split(";")
        for pair in pairs:
            key, value = pair.split(":")
            key = key.strip()
            value = value.strip()
            dict_text[key] = value

        return dict_text
