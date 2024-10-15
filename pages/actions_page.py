from pages.base_page import BasePage
from elements.input import Input
from elements.label import Label
import random


class ActionsPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//input"

    ACTIONS_INPUT_LOC = "//*[@id='content']//input"
    VALUE_LABEL_LOC = "range"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Input(
            self.driver,
            self.UNIQUE_LOC,
            description="Actions page -> Actions input"
        )

        self.actions_input = Input(
            self.driver,
            self.ACTIONS_INPUT_LOC,
            description="Actions page -> Actions input")
        self.value_label = Label(
            self.driver,
            self.VALUE_LABEL_LOC,
            description="Actions page -> Value label")

    def get_random_value(self):
        minimum = float(self.actions_input.get_attribute("min"))
        maximum = float(self.actions_input.get_attribute("max"))
        center = maximum / 2

        list_value = [i / 2 for i in range(int(minimum) + 1, int(maximum) * 2)]
        random_value = random.choice(list_value)

        if random_value > center:
            random_value_1 = ((random_value - center) / 0.5) * 11
        elif random_value < center:
            random_value_1 = ((center - random_value) / 0.5) * (-10)
        else:
            random_value_1 = 0

        if random_value.is_integer():
            random_value = str(int(random_value))
        else:
            random_value = str(random_value)

        self.actions_input.click_and_hold(random_value_1)

        return random_value

    def get_value(self):
        return self.value_label.get_text()
