from utils.config_utils import JsonUtils
from pages.handlers_page import HandlersPage


def test_alerts(driver):
    driver.get(JsonUtils.get_attribute("url_handlers_7"))
    handlers_page = HandlersPage(driver)
    handlers_page.wait_for_open()

    handlers_page.click_here()

    window1_text = handlers_page.get_text()
    window1_title_text = driver.get_title_window()

    assert window1_text == "New Window" == window1_title_text,\
        "New window not opened"

    driver.switch_back_window()

    assert handlers_page.is_page_opened(), "Page not opened"

    handlers_page.click_here()

    window2_text = handlers_page.get_text()
    window2_title_text = driver.get_title_window()

    assert window2_text == "New Window" == window2_title_text,\
        "New window not opened"

    driver.switch_back_window()

    assert handlers_page.is_page_opened(), "Page not opened"

    driver.switch_first_window()
    driver.driver.close()

    assert len(driver.driver.window_handles) == 2, "Window not closed"

    driver.switch_second_window()
    driver.driver.close()

    assert len(driver.driver.window_handles) == 1, "Window not closed"
