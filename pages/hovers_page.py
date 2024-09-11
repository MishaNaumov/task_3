from pages.base_page import BasePage
from elements.webelement import WebElement
from elements.label import Label


class HoversPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//h3"

    ING1_WEB_ELEMENT_LOC = "//div[@class='figure'][1]"
    ING2_WEB_ELEMENT_LOC = "//div[@class='figure'][2]"
    ING3_WEB_ELEMENT_LOC = "//div[@class='figure'][3]"
    IMG1_TEXT_LABEL_LOC = "//div[@class='figure'][1]//h5"
    IMG2_TEXT_LABEL_LOC = "//div[@class='figure'][2]//h5"
    IMG3_TEXT_LABEL_LOC = "//div[@class='figure'][3]//h5"
    IMG1_HREF_LABEL_LOC = "//div[@class='figure'][1]//a"
    IMG2_HREF_LABEL_LOC = "//div[@class='figure'][2]//a"
    IMG3_HREF_LABEL_LOC = "//div[@class='figure'][3]//a"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Label(self.driver, self.UNIQUE_LOC,
                                   description="Hovers page -> Hovers label")

        self.img1_web_element = WebElement(self.driver, self.ING1_WEB_ELEMENT_LOC,
                                   description="Hovers page -> IMG 1")
        self.img1_text_label = Label(self.driver, self.IMG1_TEXT_LABEL_LOC,
                                     description="Hovers page -> IMG 1 text")
        self.img1_href_label = Label(self.driver, self.IMG1_HREF_LABEL_LOC,
                                     description="Hovers page -> IMG 1 href")

        self.img2_web_element = WebElement(self.driver, self.ING2_WEB_ELEMENT_LOC,
                                   description="Hovers page -> IMG 2")
        self.img2_text_label = Label(self.driver, self.IMG2_TEXT_LABEL_LOC,
                                     description="Hovers page -> IMG 2 text")
        self.img2_href_label = Label(self.driver, self.IMG2_HREF_LABEL_LOC,
                                     description="Hovers page -> IMG 2 href")

        self.img3_web_element = WebElement(self.driver, self.ING3_WEB_ELEMENT_LOC,
                                   description="Hovers page -> IMG 3")
        self.img3_text_label = Label(self.driver, self.IMG3_TEXT_LABEL_LOC,
                                     description="Hovers page -> IMG 3 text")
        self.img3_href_label = Label(self.driver, self.IMG3_HREF_LABEL_LOC,
                                     description="Hovers page -> IMG 3 href")

    def move_to_img1(self):
        self.img1_web_element.move_to_element()

    def move_to_img2(self):
        self.img2_web_element.move_to_element()

    def move_to_img3(self):
        self.img3_web_element.move_to_element()

    def is_img_1_corrected(self):
        if self.img1_text_label.presence_wait().is_displayed() and \
                self.img1_text_label.get_text()[6:] == "user1":
            return True
        else:
            return False

    def is_img_2_corrected(self):
        if self.img2_text_label.presence_wait().is_displayed() and \
                self.img2_text_label.get_text()[6:] == "user2":
            return True
        else:
            return False

    def is_img_3_corrected(self):
        if self.img3_text_label.presence_wait().is_displayed() and \
                self.img3_text_label.get_text()[6:] == "user3":
            return True
        else:
            return False

    def click_for_img1(self):
        self.img1_href_label.click()

    def click_for_img2(self):
        self.img2_href_label.click()

    def click_for_img3(self):
        self.img3_href_label.click()

    def is_url1_corrected(self):
        if self.driver.get_url()[-1] == "1":
            return True
        else:
            return False

    def is_url2_corrected(self):
        if self.driver.get_url()[-1] == "2":
            return True
        else:
            return False

    def is_url3_corrected(self):
        if self.driver.get_url()[-1] == "3":
            return True
        else:
            return False
