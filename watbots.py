from selenium import webdriver
import time
from time import sleep

def Main():
    driver = webdriver.Firefox()

    driver.get("https://messages.google.com/web/")

    input("Press anything after QR scan")
    time.sleep(5)

    driver.find_element_by_xpath("//span/div[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//input[@placeholder='Type a name, phone number, or email']").clear()
    driver.find_element_by_xpath("//input[@placeholder='Type a name, phone number, or email']").send_keys('Baddy')
    time.sleep(7)
    driver.find_element_by_xpath("//mw-contact-row/div/div/div[2]").click()
    time.sleep(7)


    # //mws-message-wrapper[@is-last='true']//div[@class='text-msg ng-star-inserted']


    lastmessage = driver.find_element_by_xpath("//mws-message-wrapper[@is-last='true']//div[@class='text-msg ng-star-inserted']")

    last_mes = lastmessage.text
    print(last_mes)

    while(True):

        lastmessage = driver.find_element_by_xpath("//mws-message-wrapper[@is-last='true']//div[@class='text-msg ng-star-inserted']")
        if lastmessage.text != last_mes:
            last_mes = lastmessage.text

        sleep(15)


if __name__ == '__main__':
    Main()


#last_text = last_message.find_element_by_xpath("//div[@class='text-msg ng-star-inserted']")
#print(last_text.text)

#Type a name, phone number, or email

# //div[@class='text-msg ng-star-inserted']



# //mws-message-wrapper[@is-last='true'] //finds last message
