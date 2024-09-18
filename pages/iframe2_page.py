from pages.base_page import BasePage
from elements.webelement import WebElement
from elements.label import Label


class Iframe2Page(BasePage):
    UNIQUE_LOC = "//*[@id='framesWrapper']"

    NEST_FRAME_WEB_ELEMENT_LOC = "//div[@class='element-list collapse show']//li[@id='item-3']"
    FRAME_WEB_ELEMENT_LOC = "//div[@class='element-list collapse show']//li[@id='item-2']"
    TITLE_NEST_FRAME_LABEL_LOC = "//*[@id='framesWrapper']//h1"
    TITLE_FRAMES_LABEL_LOC = "//*[@id='framesWrapper']//h1"

    PAGE1_IFRAME1_WEB_ELEMENT_LOC = "//iframe[@id='frame1']"
    PAGE1_IFRAME2_WEB_ELEMENT_LOC = "//iframe[not(@id='frame1')]"

    PAGE1_IFRAME1_TEXT_WEB_ELEMENT_LOC = "//body"
    PAGE1_IFRAME2_TEXT_WEB_ELEMENT_LOC = "//body//p"

    PAGE2_IFRAME1_WEB_ELEMENT_LOC = "//*[@id='frame1']"
    PAGE2_IFRAME2_WEB_ELEMENT_LOC = "//*[@id='frame2']"

    PAGE2_IFRAME1_TEXT_WEB_ELEMENT_LOC = "//*[@id='sampleHeading']"
    PAGE2_IFRAME2_TEXT_WEB_ELEMENT_LOC = "//*[@id='sampleHeading']"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = WebElement(self.driver, self.UNIQUE_LOC,
                                   description="Iframe page -> Iframe web element")

        self.nest_frame_web_element = WebElement(self.driver, self.NEST_FRAME_WEB_ELEMENT_LOC,
                                         description="Iframe page -> Iframe web element")
        self.frame_web_element = WebElement(self.driver, self.FRAME_WEB_ELEMENT_LOC,
                                                 description="Iframe page -> Iframe web element")
        self.title_nest_frame_label = Label(self.driver, self.TITLE_NEST_FRAME_LABEL_LOC,
                                                 description="Iframe page -> Title label")
        self.title_frame_label = Label(self.driver, self.TITLE_FRAMES_LABEL_LOC,
                                 description="Iframe page -> Title label")

        self.page1_iframe1_web_element = WebElement(self.driver,
                                            self.PAGE1_IFRAME1_WEB_ELEMENT_LOC,
                                            description="Iframe page -> Iframe web element")
        self.page1_iframe2_web_element = WebElement(self.driver,
                                              self.PAGE1_IFRAME2_WEB_ELEMENT_LOC,
                                              description="Iframe page -> Iframe web element")

        self.page1_iframe1_text_web_element = WebElement(self.driver,
                                              self.PAGE1_IFRAME1_TEXT_WEB_ELEMENT_LOC,
                                              description="Iframe page -> Iframe web element")
        self.page1_iframe2_text_web_element = WebElement(self.driver,
                                                   self.PAGE1_IFRAME2_TEXT_WEB_ELEMENT_LOC,
                                                   description="Iframe page -> Iframe web element")

        self.page2_iframe1_web_element = WebElement(self.driver,
                                                    self.PAGE2_IFRAME1_WEB_ELEMENT_LOC,
                                                    description="Iframe page -> Iframe web element")
        self.page2_iframe2_web_element = WebElement(self.driver,
                                                    self.PAGE2_IFRAME2_WEB_ELEMENT_LOC,
                                                    description="Iframe page -> Iframe web element")

        self.page2_iframe1_text_web_element = WebElement(self.driver,
                                                         self.PAGE2_IFRAME1_TEXT_WEB_ELEMENT_LOC,
                                                         description="Iframe page -> Iframe web element")
        self.page2_iframe2_text_web_element = WebElement(self.driver,
                                                         self.PAGE2_IFRAME2_TEXT_WEB_ELEMENT_LOC,
                                                         description="Iframe page -> Iframe web element")

    def click_nest_frame(self):
        self.nest_frame_web_element.click()

    def click_frame(self):
        self.frame_web_element.click()

    def get_text_title_nest_frame(self):
        return self.title_nest_frame_label.get_text()

    def get_text_title_frame(self):
        return self.title_frame_label.get_text()

    def page1_switch_iframe1(self):
        self.driver.frame(self.page1_iframe1_web_element.presence_wait())

    def get_text_page1_iframe1(self):
        return self.page1_iframe1_text_web_element.get_text()

    def page1_switch_iframe2(self):
        self.driver.frame(self.page1_iframe2_web_element.presence_wait())

    def get_text_page1_iframe2(self):
        return self.page1_iframe1_text_web_element.get_text()

    def page2_switch_iframe1(self):
        self.driver.frame(self.page2_iframe1_web_element.presence_wait())

    def page2_switch_iframe2(self):
        self.driver.frame(self.page2_iframe2_web_element.presence_wait())

    def get_text_page2_iframe1(self):
        return self.page2_iframe1_text_web_element.get_text()

    def get_text_page2_iframe2(self):
        return self.page2_iframe1_text_web_element.get_text()



