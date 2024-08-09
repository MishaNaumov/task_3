from pages.base_page import BasePage


class AlertsPage(BasePage):
    UNIQUE_LOC = "//button[@onclick='jsAlert()']"
