import sendgrid
import os
from selenium import webdriver
#import chromedriver_binary
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
from dotenv import load_dotenv

# /usr/bin/python
chrome_options = Options()

chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-setuid-sandbox")

load_dotenv()
url = 'https://shopee.com.my/Sony-Playstation-5-PS5-825GB-1TB-Slim-Disc-Edition-(Sony-Malaysia-Warranty)-i.27398815.7864756558?sp_atk=9ba66097-b5e1-4563-88eb-b98765420e9b&xptdk=9ba66097-b5e1-4563-88eb-b98765420e9b'
# url = 'https://shopee.com.my/product/724335/2212828002' // sample for testing purpose
driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)

driver.get(url)

# click the english language button
#driver.find_element_by_xpath("""//*[@id="modal"]/div[1]/div[1]/div/div[3]/div[1]/button""").click()

sleep(3)
# click disc version 
driver.find_element_by_xpath("""//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[1]/div/button[1]""").click();
# stock reading count on the product detail section
out = driver.find_element_by_xpath("""//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[2]/div[2]/div[2]""").text

# print(buy_now)
if out == "0 piece available":
    print("Product still out of stock")
    message = Mail(
        from_email='muaz.noreply@gmail.com',
        to_emails='ahmedmuaz0152@gmail.com',
        subject='Shopee Script - Your item is still empty!',
        html_content='<div><p>Item is still empty in the cart</p></div><div style="text-align: center;"><img src="https://i.redd.it/9d7sw78owea11.png" width="50%" height="50%"  alt="meme_empty_cart"></img></div>')
    try:
        sg = SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        print(e)
else:
    print("Product is available to purchase!")
    #to insert in else block
      # variant for ps5 shopee page
    # variant = driver.find_element_by_xpath("""//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[1]/div/button[1]""").click();
    # variant = driver.find_element_by_xpath("""//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[2]/div/button[1]""").click();
    # buy_now = driver.find_element_by_xpath("""//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]""").click();
    # sleep(2);
    # file_credential = open('./credentials.txt', 'r')
    # credential = file_credential.readlines()
    # exit(0)
    # print(credential)

    # username = driver.find_element_by_xpath("""//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/div[2]/div[1]/input""").send_keys(credential[0].rstrip('\n'))
    # password = driver.find_element_by_xpath("""//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/div[3]/div[1]/input""").send_keys(credential[1])
    # sleep(2);
    # submit = driver.find_element_by_xpath("""//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button""");
    # sleep(2)
    # submit.click();
    # sleep(10);

    message = Mail(
        from_email='muaz.noreply@gmail.com',
        to_emails='ahmedmuaz0152@gmail.com',
        subject='Shopee Script - Your item is back in stock!',
        html_content='<strong>Buy now!. Item is available and selling like hot cakes. </strong>')
    try:
        sg = SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

driver.quit()
