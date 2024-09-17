from pages.base_page import BasePage
from elements.button import Button
from elements.label import Label


class AlertsPage(BasePage):
    UNIQUE_LOC = "//button[@onclick='jsAlert()']"

    ALERT_BUTTON_LOC = "//button[@onclick='jsAlert()']"
    CONFIRM_BUTTON_LOC = "//button[@onclick='jsConfirm()']"
    PROMPT_BUTTON_LOC = "//button[@onclick='jsPrompt()']"
    RESULT_LABEL_LOC = "//*[@id='result']"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Button(self.driver, self.UNIQUE_LOC,
                                   description="Alert page -> Alert button")

        self.alert_button = Button(self.driver, self.ALERT_BUTTON_LOC,
                                   description="Alert page -> Alert button")
        self.confirm_button = Button(self.driver, self.CONFIRM_BUTTON_LOC,
                                   description="Alert page -> Confirm button")
        self.prompt_button = Button(self.driver, self.PROMPT_BUTTON_LOC,
                                   description="Alert page -> Prompt button")

        self.result_label = Label(self.driver, self.RESULT_LABEL_LOC,
                                   description="Alert page -> Result label")

    def click_alert(self):
        self.alert_button.click()

    def click_confirm(self):
        self.confirm_button.click()

    def click_prompt(self):
        self.prompt_button.click()

    def click_js_alert(self):
        self.driver.click_js(self.alert_button.presence_wait())

    def click_js_confirm(self):
        self.driver.click_js(self.confirm_button.presence_wait())

    def click_js_prompt(self):
        self.driver.click_js(self.prompt_button.presence_wait())

    def get_text_result(self):
        return self.result_label.get_text()
