from pages.base_page import BasePage
from elements.input import Input
from elements.label import Label
from selenium.webdriver.common.keys import Keys


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

    def set_value(self, value):
        start_value = 2.5
        step_value = 0.5

        delta = int((value - start_value) / step_value)

        self.actions_input.send_keys(
            (Keys.RIGHT if delta > 0 else Keys.LEFT) * abs(delta))

        return str(int(value)) if value.is_integer() else str(value)

    def move_action(self, arg):
        self.actions_input.click_and_hold()
        return self.set_value(arg)

    def get_value(self):
        return self.value_label.get_text()
