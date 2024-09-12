from pages.base_page import BasePage
from elements.label import Label


class DynamicContentPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//h3"

    IMG1_LABEL_LOC = "//div[@class='row'][3]//img//preceding::img[2]"
    IMG2_LABEL_LOC = "//div[@class='row'][3]//img//preceding::img[1]"
    IMG3_LABEL_LOC = "//div[@class='row'][3]//img"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Label(self.driver, self.UNIQUE_LOC,
                                   description="Dynamic content page"
                                               " -> Dynamic content label")

        self.img1_label = Label(self.driver, self.IMG1_LABEL_LOC,
                                    description="Dynamic content page"
                                                " -> Img 1")
        self.img2_label = Label(self.driver, self.IMG2_LABEL_LOC,
                                description="Dynamic content page"
                                            " -> Img 2")
        self.img3_label = Label(self.driver, self.IMG3_LABEL_LOC,
                                description="Dynamic content page"
                                            " -> Img 3")

    def get_src_img1(self):
        return self.img1_label.get_attribute("src")

    def get_src_img2(self):
        return self.img2_label.get_attribute("src")

    def get_src_img3(self):
        return self.img3_label.get_attribute("src")

    def refresh_page_for_2_img(self):
        while (self.get_src_img1() != self.get_src_img2()) and\
                (self.get_src_img1() != self.get_src_img3()) and\
                (self.get_src_img2() != self.get_src_img3()):
            self.driver.refresh()

    def is_2_img_corrected(self):
        if (self.get_src_img1() == self.get_src_img2()) or\
                (self.get_src_img1() == self.get_src_img3()) or\
                (self.get_src_img2() == self.get_src_img3()):
            return True
        else:
            return False
