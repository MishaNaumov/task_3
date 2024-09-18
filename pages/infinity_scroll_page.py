import time
from bs4 import BeautifulSoup
import requests


from pages.base_page import BasePage
from elements.label import Label
import selenium.common


class InfinityScrollPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//h3"

    PARAGRAPH_LABEL_LOC = "//div[@class='jscroll-added'][last()]"
    PARAGRAPH_23_LABEL_LOC = "//div[@class='jscroll-added'][23]"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Label(self.driver, self.UNIQUE_LOC,
                                   description="Infinite Scroll page"
                                               " -> Infinite Scroll label")

        self.paragraph_label = Label(self.driver, self.PARAGRAPH_LABEL_LOC,
                                    description="Infinite Scroll page"
                                                " -> Paragraph label")
        self.paragraph_23_label = Label(self.driver, self.PARAGRAPH_23_LABEL_LOC,
                                     description="Infinite Scroll page"
                                                 " -> Paragraph label")

    def test_12(self):
        response = self.driver.get_layout()
        soup = BeautifulSoup(response, "lxml")

        return soup

    def scroll_new(self):
        src = self.driver.get_layout()
        soup = BeautifulSoup(src, "lxml")
        next_label = soup.find(class_="jscroll-added").find_next_sibling()
        return next_label

    def scroll(self):
        d = []
        while True:
            self.driver.scroll_down(self.paragraph_label.presence_wait())
            src = self.driver.get_layout()
            soup = BeautifulSoup(src, "lxml")
            d.append(soup.find(class_="jscroll-added").find_next_sibling())
            if len(d) == 24:
                break
