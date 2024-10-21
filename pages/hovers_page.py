from pages.base_page import BasePage
from elements.webelement import WebElement
from elements.label import Label


class HoversPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//h3"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Label(
            self.driver,
            self.UNIQUE_LOC,
            description="Hovers page -> Hovers label"
        )

    def move_to_img(self, index):
        img_web_element_loc = f"//div[@class='figure'][{index}]"

        img_web_element = WebElement(
            self.driver,
            img_web_element_loc,
            description="Hovers page -> IMG"
        )

        img_web_element.move_to_element()

    def get_text_img(self, index):
        img_text_label = f"//div[@class='figure'][{index}]//h5"

        img_text_label = Label(
            self.driver,
            img_text_label,
            description="Hovers page -> IMG text"
        )

        img_text_label.is_displayed()
        return img_text_label.get_text()

    def click_img(self, index):
        img_a_label_text = f"//div[@class='figure'][{index}]//a"

        img_a_label = Label(
            self.driver,
            img_a_label_text,
            description="Hovers page -> IMG 3 href"
        )

        img_a_label.click()
