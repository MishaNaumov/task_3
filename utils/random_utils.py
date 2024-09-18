import random
import string


class RandomUtils:

    @staticmethod
    def random_str(lens):
        return ''.join([random.choice(string.ascii_lowercase + string.digits
                                      if i != 5 else string.ascii_uppercase)
                        for i in range(lens)])
