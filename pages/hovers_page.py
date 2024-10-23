from pages.base_page import BasePage
from elements.webelement import WebElement
from elements.label import Label


class HoversPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//h3"
    IMG_WEB_ELEMENT_LOC = "//div[@class='figure'][{}]"
    IMG_TEXT_LABEL = f"{IMG_WEB_ELEMENT_LOC}//h5"
    IMG_A_LABEL_TEXT = f"{IMG_WEB_ELEMENT_LOC}//a"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Label(
            self.driver,
            self.UNIQUE_LOC,
            description="Hovers page -> Hovers label"
        )

    def move_to_img(self, index):
        img_web_element_loc = self.IMG_WEB_ELEMENT_LOC.format(index)

        img_web_element = WebElement(
            self.driver,
            img_web_element_loc,
            description=f"Hovers page -> IMG {index}"
        )

        img_web_element.move_to_element()

    def get_text_img(self, index):
        img_text_label = self.IMG_TEXT_LABEL.format(index)

        img_text_label = Label(
            self.driver,
            img_text_label,
            description=f"Hovers page -> IMG {index} text"
        )

        img_text_label.is_displayed()
        return img_text_label.get_text()

    def click_img(self, index):
        img_a_label_text = self.IMG_A_LABEL_TEXT.format(index)

        img_a_label = Label(
            self.driver,
            img_a_label_text,
            description=f"Hovers page -> IMG {index} href"
        )

        img_a_label.click()
