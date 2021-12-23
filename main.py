import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(executable_path=r"C:\Users\Kivanc's Account\Desktop\Selenium Drivers\chromedriver.exe")
driver.get("https://www.dominos.ca/")
driver.implicitly_wait(8)

element_1 = driver.find_element_by_class_name('smart-order__cta-container')
element_1.click()

element_2 = driver.find_element_by_id('Street')
element_2.click()
element_2.send_keys("181 King Street South")

element_3 = driver.find_element_by_id('City')
element_3.click()
element_3.send_keys("Waterloo")

element_4 = driver.find_element_by_id('Region')
element_4.click()
element_4.send_keys("ON")
element_4.click()

element_5 = driver.find_element_by_id('Postal_Code')
element_5.click()
element_5.send_keys("N2J0E7")

element_6 = driver.find_element_by_xpath('//*[@id="locationSearchForm"]/div/div[4]/button')
element_6.click()

element_7 = driver.find_element_by_xpath('//*[@id="entree-Pizza"]/a/div[2]/h2')
element_7.click()

element_8 = driver.find_element_by_xpath('//*[@id="categoryPage2"]/section/div/div[12]/div/a[1]')
element_8.click()

element_9 = driver.find_element_by_xpath('//*[@id="_dpz"]/header/nav[1]/div[1]/ul/li[3]/a')
element_9.click()

element_10 = driver.find_element_by_xpath('//*[@id="entreesPage"]/div[2]/div[11]/a/div[2]/h2')
element_10.click()

element_11 = driver.find_element_by_xpath('//*[@id="categoryPage2"]/section[2]/div/div[1]/div/a')
actions = ActionChains(driver)
actions.move_to_element(element_11).perform()

element_12 = driver.find_element_by_xpath('//*[@id="categoryPage2"]/section[2]/div/div[1]/div/a')
element_12.click()

element_13 = driver.find_element_by_xpath('//*[@id="pageModal"]/div/section/div/div/div/form/div/button[2]')
element_13.click()

element_14 = driver.find_element_by_xpath('//*[@id="_dpz"]/header/nav[1]/div[1]/ul/li[2]/a')
element_14.click()

element_15 = driver.find_element_by_xpath('//*[@id="homeWrapper"]/main/section[2]/div/div[2]/a')
element_15.click()

element_16 = driver.find_element_by_xpath('//*[@id="genericOverlay"]/section/header/button')
element_16.click()

element_17 = driver.find_element_by_xpath('//*[@id="js-checkoutColumns"]/aside/div[3]/div[1]/a')
element_17.click()
