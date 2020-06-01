
import urllib.request
import xlsxwriter
import xlrd, os, time
from selenium import webdriver
import unittest
import HtmlTestRunner
class TestLaunch(unittest.TestCase):
    def setUp(self):
        self.driver =    self.driver = webdriver.Chrome("/home/pavan/Downloads/chromedriver_linux64 (2)/chromedriver")
        self.driver.get("file:///home/pavan/Documents/assignment2[stp]/demo2.html")
        self.driver.maximize_window()

    def test_FindClass(self):
        workbook = xlsxwriter.Workbook('assign.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.set_column('A:A', 15)

        worksheet.write(0, 0, 'Picture')
        worksheet.write(0, 1, 'First Name')
        worksheet.write(0, 2, 'Last Name')
        for i in range(1, 4):
            self.driver.find_element_by_id("save").click()
            worksheet.set_row(i, 65)
            # print("clicked")
            time.sleep(5)
            pic = self.driver.find_element_by_xpath('//*[@id="loading"]/img')
            src = pic.get_attribute('src')
            urllib.request.urlretrieve(src, "captcha" + str(i) + ".png")
            names = self.driver.find_element_by_xpath('//*[@id="loading"]').text
            name = names.splitlines()
            fname = (name[0].rstrip().split(' '))
            lname = (name[2].rstrip().split(' '))
            print(fname[3] + " " + lname[3])
            worksheet.insert_image(i, 0, 'captcha' + str(i) + '.png', {'x_scale': 0.5, 'y_scale': 0.5})
            worksheet.write(i, 1, fname[3])
            worksheet.write(i, 2, lname[3])
        print("Image and  Names saved successfully")
        workbook.close()

    def tearDown(self):
        self.driver.quit()
        if __name__ == '_main_':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="file:///home/pavan/PycharmProjects/assignment2/reports"))
