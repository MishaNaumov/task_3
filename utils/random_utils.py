import random
import string


class RandomUtils:

    @staticmethod
    def random_str(lens):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.sample(letters_and_digits, lens))

    @staticmethod
    def random_value(min_value, max_value, step):
        return random.randrange(min_value, max_value, step)

