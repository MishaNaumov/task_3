from pages.base_page import BasePage
from elements.label import Label
from elements.webelement import WebElement
from custom_elements.text_editor_input import TextEditorInput
from elements.button import Button
import selenium.common
from selenium.webdriver.common.keys import Keys


class IframePage(BasePage):
    UNIQUE_LOC = "//div[@class='crumb-sample']"

    IFRAME_WEB_ELEMENT_LOC = "//iframe[@class='e-rte-content']"
    FIELD_INPUT_LOC = "//body"
    TEXT_LABEL_LOC = "//strong[1]"

    ALIGN_BUTTON_LOC = "iframeRTE_toolbar_Alignments"

    ALIGN_RIGHT_BUTTON_LOC = "//ul[@role='menu']//li[3]"
    TEXT_STYLE_LABEL_LOC = "//body//p"

    FRONT_SIZE_BUTTON_LOC = "iframeRTE_toolbar_FontSize"
    PT8_BUTTON_LOC = "//ul[@role='menu']//li[2]"
    TEXT_STYLE2_LABEL_LOC = "//body//p//span"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Label(
            self.driver,
            self.UNIQUE_LOC,
            description="Iframe page -> Iframe label"
        )

        self.iframe_web_element = WebElement(
            self.driver,
            self.IFRAME_WEB_ELEMENT_LOC,
            description="Iframe page -> Iframe web element"
        )
        self.field_input = TextEditorInput(
            self.driver,
            self.FIELD_INPUT_LOC,
            description="Iframe page -> Field web element"
        )

        self.text_label = Label(
            self.driver,
            self.TEXT_LABEL_LOC,
            description="Iframe page -> Text label"
        )

        self.align_button = Button(
            self.driver,
            self.ALIGN_BUTTON_LOC,
            description="Iframe page -> Align button"
        )
        self.align_right_button = Button(
            self.driver,
            self.ALIGN_RIGHT_BUTTON_LOC,
            description="Iframe page -> Align right button"
        )

        self.text_style_label = Label(
            self.driver,
            self.TEXT_STYLE_LABEL_LOC,
            description="Iframe page -> Text style label"
        )

        self.front_size_button = Button(
            self.driver,
            self.FRONT_SIZE_BUTTON_LOC,
            description="Iframe page -> Text style label"
        )
        self.pt8_button = Button(
            self.driver,
            self.PT8_BUTTON_LOC,
            description="Iframe page -> Text style label"
        )

        self.text_style2_label = Label(
            self.driver,
            self.TEXT_STYLE2_LABEL_LOC,
            description="Iframe page -> Text style label"
        )

    def switch_iframe1(self):
        self.driver.switch_frame(self.iframe_web_element.wait_presence())

    def clear_field_iframe(self):
        self.field_input.clear()

    def send_keys_random(self, text):
        self.field_input.send_keys(text)

    def get_text(self):
        return self.field_input.get_text()

    def select_all_text(self):
        self.field_input.select_all_text()

    def select_all_text_bold(self):
        self.field_input.select_all_text_bold()

    def is_text_bold(self):
        try:
            self.text_label.wait_presence()
            return True
        except selenium.common.TimeoutException:
            return False

    def align_text_right(self):
        self.align_button.click()
        self.align_right_button.click()

    def get_style_text(self):
        return self.text_style_label.get_attribute("style")

    def select_half_text(self):
        half_text = int(len(self.text_style_label.get_text())/2)

        self.field_input.send_keys(Keys.CONTROL + Keys.RIGHT)
        self.field_input.key_down(Keys.SHIFT)
        self.field_input.send_keys(Keys.LEFT * half_text)

    def turn_text_8pt(self):
        self.front_size_button.click()
        self.pt8_button.click()

    def get_font_size_text(self):
        return self.text_style2_label.get_attribute("style")

    def clear_format(self):
        self.field_input.clear_format()

    def create_new_file(self):
        self.clear_format()
        self.clear_field_iframe()

    def is_clear_format(self):
        try:
            self.text_style_label.wait_presence()
            return False
        except selenium.common.TimeoutException:
            return True
