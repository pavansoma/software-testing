import time
from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest
import HtmlTestRunner
class TestLaunch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/home/pavan/Downloads/chromedriver_linux64 (2)/chromedriver")
        self.driver.get("file:///home/pavan/Documents/assignment2[stp]/test.html")
        self.driver.maximize_window()

    def test_FindClass(self):
        source = self.driver.find_element_by_id("draggable")
        target = self.driver.find_element_by_id("droppable")
        mouse = ActionChains(self.driver).drag_and_drop(source, target)
        mouse.perform()
        time.sleep(4)
        source = self.driver.find_element_by_id("draggable1")
        target = self.driver.find_element_by_id("droppable1")
        mouse = ActionChains(self.driver).drag_and_drop(source, target)
        mouse.perform()
        time.sleep(4)
        source = self.driver.find_element_by_id("draggable2")
        target = self.driver.find_element_by_id("droppable2")
        mouse = ActionChains(self.driver).drag_and_drop(source, target)
        mouse.perform()
        time.sleep(4)

    def tearDown(self):
        self.driver.quit()
        if __name__ == '_main_':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="file:///home/pavan/PycharmProjects/assignment2/reports"))