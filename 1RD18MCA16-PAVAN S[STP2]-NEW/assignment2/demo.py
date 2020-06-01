import time
import urllib.request

import xlsxwriter
from selenium import webdriver
import openpyxl
from openpyxl import Workbook

driver = webdriver.Chrome("/home/pavan/Downloads/chromedriver_linux64(1)/chromedriver")
driver.get("file:///home/pavan/Documents/assignment2[stp]/demo2.html")
driver.maximize_window()
time.sleep(1)
driver.find_element_by_id("save").click()
print("Button clicked")
time.sleep(4)
pic = driver.find_element_by_xpath('//*[@id="loading"]/img')
src = pic.get_attribute('src')
#fname=driver.find_element_by_xpath("//*[contains(text(),'Last Name')]")

#fname = driver.find_element_by_xpath("//*[@id='loading']/contains(text(),'Last Name')")
#print(fname.text)
urllib.request.urlretrieve(src, "captcha.png")
names = driver.find_element_by_xpath('//*[@id="loading"]').text
name=names.splitlines()
fname=(name[0].rstrip().split(' '))
print(fname[3])

lname=(name[2].rstrip().split(' '))
print(lname[3])


workbook = xlsxwriter.Workbook('assign.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A',15)
worksheet.set_row(1,65)
worksheet.write('A1','Picture')
worksheet.write('B1','First Name')
worksheet.write('C1','Last Name')
worksheet.insert_image('A2','captcha.png',{'x_scale': 0.5, 'y_scale': 0.5})
worksheet.write('B2',fname[3])
worksheet.write('C2',lname[3])

print("saved successfully")
workbook.close()