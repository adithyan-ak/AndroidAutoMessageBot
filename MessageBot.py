from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://messages.google.com/web/")

input("Press anything after QR scan")
time.sleep(5)

names = [''] #Enter the contact names

Message = "" #Enter the Message 

for name in names:

    driver.find_element_by_xpath("//span/div[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//input[@placeholder='Type a name, phone number, or email']").clear()
    driver.find_element_by_xpath("//input[@placeholder='Type a name, phone number, or email']").send_keys(name)
    time.sleep(7)
    driver.find_element_by_xpath("//mw-contact-row/div/div/div[2]").click()
    time.sleep(7)
    driver.find_element_by_xpath("//textarea[@placeholder='Text message']").clear()
    driver.find_element_by_xpath("//textarea[@placeholder='Text message']").send_keys(Message) #type message
    driver.find_element_by_xpath("//mws-message-compose/div/mws-message-send-button/button/span").click() #send button click


