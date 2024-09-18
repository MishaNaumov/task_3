from pages.base_page import BasePage
from elements.label import Label
from elements.webelement import WebElement
from elements.input import Input
from elements.button import Button
from utils.random_utils import RandomUtils
import selenium.common


class IframePage(BasePage):
    UNIQUE_LOC = "//div[@class='crumb-sample']"

    IFRAME_WEB_ELEMENT_LOC = "//iframe[@class='e-rte-content']"
    FIELD_INPUT_LOC = "//body"
    TEXT_LABEL_LOC = "//strong[1]"

    ALIGN_BUTTON_LOC = "//button[@id='iframeRTE_toolbar_Alignments']"

    ALIGN_RIGHT_BUTTON_LOC = "//ul[@role='menu']//li[3]"
    TEXT_STYLE_LABEL_LOC = "//body//p"

    FRONT_SIZE_BUTTON_LOC = "//button[@id='iframeRTE_toolbar_FontSize']"
    PT8_BUTTON_LOC = "//ul[@role='menu']//li[2]"
    TEXT_STYLE2_LABEL_LOC = "//body//p//span"


    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Label(self.driver, self.UNIQUE_LOC,
                                   description="Iframe page -> Iframe label")

        self.iframe_web_element = WebElement(self.driver, self.IFRAME_WEB_ELEMENT_LOC,
                                    description="Iframe page -> Iframe web element")
        self.field_input = Input(self.driver, self.FIELD_INPUT_LOC,
                                    description="Iframe page -> Field web element")

        self.text_label = Label(self.driver, self.TEXT_LABEL_LOC,
                                 description="Iframe page -> Text label")

        self.align_button = Button(self.driver, self.ALIGN_BUTTON_LOC,
                                description="Iframe page -> Align button")
        self.align_right_button = Button(self.driver, self.ALIGN_RIGHT_BUTTON_LOC,
                                   description="Iframe page -> Align right button")

        self.text_style_label = Label(self.driver,
                                         self.TEXT_STYLE_LABEL_LOC,
                                         description="Iframe page -> Text style label")

        self.front_size_button = Button(self.driver,
                                       self.FRONT_SIZE_BUTTON_LOC,
                                       description="Iframe page -> Text style label")
        self.pt8_button = Button(self.driver,
                                       self.PT8_BUTTON_LOC,
                                       description="Iframe page -> Text style label")

        self.text_style2_label = Label(self.driver,
                                      self.TEXT_STYLE2_LABEL_LOC,
                                      description="Iframe page -> Text style label")


    def switch_iframe1(self):
        self.driver.frame(self.iframe_web_element.presence_wait())

    def clear_field(self):
        self.field_input.clear()

    def send_keys_random(self):
        text = RandomUtils().random_str(20)
        self.field_input.send_keys(text)
        return text

    def get_text(self):
        return self.field_input.get_text()

    def select_all_text(self):
        self.field_input.select_all_text()

    def select_all_text_bold(self):
        self.field_input.select_all_text_bold()

    def is_text_bold(self):
        return self.text_label.presence_wait()

    def align_text_right(self):
        self.align_button.click()
        self.align_right_button.click()

    def get_style_text(self):
        return self.text_style_label.get_attribute("style")[-6:-1]

    def select_half_text(self):
        self.field_input.select_text()

    def turn_text_8pt(self):
        self.front_size_button.click()
        self.pt8_button.click()

    def get_font_size_text(self):
        return self.text_style2_label.get_attribute("style")[-4:-1]

    def clear_format(self):
        self.field_input.clear_format()

    def is_clear_format(self):
        try:
            self.text_style_label.get_attribute("style")
            return False
        except selenium.common.NoSuchElementException:
            return True
