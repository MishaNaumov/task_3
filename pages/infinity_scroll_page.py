from bs4 import BeautifulSoup
from pages.base_page import BasePage
from elements.label import Label


class InfinityScrollPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//h3"

    PARAGRAPH_LABEL_LOC = "//div[@class='jscroll-added'][last()]"
    PARAGRAPH_23_LABEL_LOC = "//div[@class='jscroll-added'][23]"
    ALL_PARAGRAPHS_LABEL_LOC = "//div[@class='jscroll-inner']"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Label(
            self.driver,
            self.UNIQUE_LOC,
            description="Infinite Scroll page"
                        " -> Infinite Scroll label"
        )

        self.paragraph_last_label = Label(
            self.driver,
            self.PARAGRAPH_LABEL_LOC,
            description="Infinite Scroll page"
                        " -> Paragraph last label"
        )
        self.paragraph_23_label = Label(
            self.driver,
            self.PARAGRAPH_23_LABEL_LOC,
            description="Infinite Scroll page"
                        " -> Paragraph 23 label"
        )
        self.all_paragraphs_label = Label(
            self.driver,
            self.ALL_PARAGRAPHS_LABEL_LOC,
            description="Infinite Scroll page"
                        " -> All paragraph label"
        )

    def scroll_until_paragraph(self, paragraph):
        while True:
            self.paragraph_last_label.scroll_down()
            src = self.all_paragraphs_label.get_attribute("innerHTML")
            soup = BeautifulSoup(src, "html.parser")
            if len(soup.find_all(class_="jscroll-added")) == paragraph:
                break
        return len(soup.find_all(class_="jscroll-added"))
