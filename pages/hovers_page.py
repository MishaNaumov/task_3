from pages.base_page import BasePage
from elements.webelement import WebElement
from elements.label import Label


class HoversPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//h3"

    IMG1_WEB_ELEMENT_LOC = "//div[@class='figure'][1]"
    IMG2_WEB_ELEMENT_LOC = "//div[@class='figure'][2]"
    IMG3_WEB_ELEMENT_LOC = "//div[@class='figure'][3]"

    IMG1_TEXT_LABEL_LOC = f"{IMG1_WEB_ELEMENT_LOC}//h5"
    IMG2_TEXT_LABEL_LOC = f"{IMG2_WEB_ELEMENT_LOC}//h5"
    IMG3_TEXT_LABEL_LOC = f"{IMG3_WEB_ELEMENT_LOC}//h5"

    IMG1_A_LABEL_LOC = f"{IMG1_WEB_ELEMENT_LOC}//a"
    IMG2_A_LABEL_LOC = f"{IMG2_WEB_ELEMENT_LOC}//a"
    IMG3_A_LABEL_LOC = f"{IMG3_WEB_ELEMENT_LOC}//a"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Label(
            self.driver,
            self.UNIQUE_LOC,
            description="Hovers page -> Hovers label"
        )

        self.img1_web_element = WebElement(
            self.driver,
            self.IMG1_WEB_ELEMENT_LOC,
            description="Hovers page -> IMG 1"
        )
        self.img1_text_label = Label(
            self.driver,
            self.IMG1_TEXT_LABEL_LOC,
            description="Hovers page -> IMG 1 text"
        )
        self.img1_a_label = Label(
            self.driver,
            self.IMG1_A_LABEL_LOC,
            description="Hovers page -> IMG 1 href"
        )

        self.img2_web_element = WebElement(
            self.driver,
            self.IMG2_WEB_ELEMENT_LOC,
            description="Hovers page -> IMG 2"
        )
        self.img2_text_label = Label(
            self.driver,
            self.IMG2_TEXT_LABEL_LOC,
            description="Hovers page -> IMG 2 text"
        )
        self.img2_a_label = Label(
            self.driver,
            self.IMG2_A_LABEL_LOC,
            description="Hovers page -> IMG 2 href"
        )

        self.img3_web_element = WebElement(
            self.driver,
            self.IMG3_WEB_ELEMENT_LOC,
            description="Hovers page -> IMG 3"
        )
        self.img3_text_label = Label(
            self.driver,
            self.IMG3_TEXT_LABEL_LOC,
            description="Hovers page -> IMG 3 text"
        )
        self.img3_a_label = Label(
            self.driver,
            self.IMG3_A_LABEL_LOC,
            description="Hovers page -> IMG 3 href"
        )

    def move_to_img1(self):
        self.img1_web_element.move_to_element()

    def move_to_img2(self):
        self.img2_web_element.move_to_element()

    def move_to_img3(self):
        self.img3_web_element.move_to_element()

    def get_text_img1(self):
        self.img1_text_label.is_displayed()
        return self.img1_text_label.get_text()

    def get_text_img2(self):
        self.img2_text_label.is_displayed()
        return self.img2_text_label.get_text()

    def get_text_img3(self):
        self.img3_text_label.is_displayed()
        return self.img3_text_label.get_text()

    def click_img1(self):
        self.img1_a_label.click()

    def click_img2(self):
        self.img2_a_label.click()

    def click_img3(self):
        self.img3_a_label.click()

