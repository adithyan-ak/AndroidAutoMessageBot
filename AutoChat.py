from selenium import webdriver
import time
from time import sleep
from chatterbot import ChatBot

def Main():

    driver = webdriver.Firefox()

    driver.get("https://messages.google.com/web/")

    input("Press anything after QR scan")
    time.sleep(5)

    driver.find_element_by_xpath("//span/div[2]").click() #Click on Search box
    time.sleep(5)
    driver.find_element_by_xpath("//input[@placeholder='Type a name, phone number, or email']").clear()
    driver.find_element_by_xpath("//input[@placeholder='Type a name, phone number, or email']").send_keys('Cute Camillus') #Type in Searchbox
    time.sleep(7)
    driver.find_element_by_xpath("//mw-contact-row/div/div/div[2]").click() #Click contact name in search box
    time.sleep(7)
    lastmessage = driver.find_element_by_xpath("//mws-message-wrapper[@is-last='true']//div[@class='text-msg ng-star-inserted']")

    last_mes = lastmessage.text
    Message = str(getQuery(last_mes))
    time.sleep(3)
    driver.find_element_by_xpath("//textarea[@placeholder='Text message']").clear()
    driver.find_element_by_xpath("//textarea[@placeholder='Text message']").send_keys(Message)  # type message
    driver.find_element_by_xpath("//mws-message-compose/div/mws-message-send-button/button/span").click()  # send button click

    while (True):

        lastmessage = driver.find_element_by_xpath("//mws-message-wrapper[@is-last='true']//div[@class='text-msg ng-star-inserted']")
        if lastmessage.text != last_mes and lastmessage.text != Message:
            last_mes = lastmessage.text
            Message = str(getQuery(last_mes))
            time.sleep(3)
            driver.find_element_by_xpath("//textarea[@placeholder='Text message']").clear()
            driver.find_element_by_xpath("//textarea[@placeholder='Text message']").send_keys(Message)  # type message
            driver.find_element_by_xpath("//mws-message-compose/div/mws-message-send-button/button/span").click()  # send button click

        sleep(5)

def getQuery(query):
    try:
        user_input = query

        bot_response = bot.get_response(user_input)

        return bot_response

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        pass

    # //mws-message-wrapper[@is-last='true']//div[@class='text-msg ng-star-inserted']




if __name__ == '__main__':
    bot = ChatBot(
        'Terminal',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            'chatterbot.logic.BestMatch'
        ],
        database_uri='sqlite:///database.db'
    )
    Main()


#last_text = last_message.find_element_by_xpath("//div[@class='text-msg ng-star-inserted']")
#print(last_text.text)

#Type a name, phone number, or email

# //div[@class='text-msg ng-star-inserted']



# //mws-message-wrapper[@is-last='true'] //finds last message
