from utils.config_utils import ConfigUtils
from pages.handlers_page import HandlersPage


def test_handlers(driver):
    driver.get(ConfigUtils.get_attribute("url_handlers_7"))
    handlers_page = HandlersPage(driver)
    handlers_page.wait_for_open()

    handlers_page.click_here()

    driver.switch_window(-1)
    window1_text = handlers_page.get_text()
    window1_title_text = driver.get_title_window()

    assert window1_text == "New Window" == window1_title_text,\
        "New window not opened"

    driver.switch_window(0)
    handlers_page.wait_for_open()

    handlers_page.click_here()

    driver.switch_window(-1)
    window2_text = handlers_page.get_text()
    window2_title_text = driver.get_title_window()

    assert window2_text == "New Window" == window2_title_text,\
        "New window not opened"

    driver.switch_window(0)
    handlers_page.wait_for_open()

    driver.switch_window(-2)
    driver.driver.close()

    assert len(driver.driver.window_handles) == 2, "Window not closed"

    driver.switch_window(-1)
    driver.driver.close()

    assert len(driver.driver.window_handles) == 1, "Window not closed"
