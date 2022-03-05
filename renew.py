from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
home_url = 'https://accounts.craigslist.org/login/home'

# Selenium config
selenium_options = Options()
selenium_options.headless = True
user_agent = os.getenv('USER_AGENT') 
selenium_options.add_argument('user-agent={0}'.format(user_agent))

def login(driver):
    username = driver.find_element_by_name('inputEmailHandle')
    username.send_keys(os.getenv('LOGIN_ID'))
    password = driver.find_element_by_name('inputPassword')
    password.send_keys(os.getenv('LOGIN_PW'))
    driver.find_element_by_xpath('//*[@id="login"]').click()

def check_for_renewals(driver):
    renew_links = driver.find_elements_by_xpath("//input[contains(@class, 'managebtn') and contains(@value, 'renew')]")
    return renew_links

def main():
    driver = webdriver.Chrome(executable_path=os.getenv('WEBDRIVER_PATH'), options=selenium_options)
    driver.get(home_url)
    login(driver)
    renew_links = check_for_renewals(driver)
    print(f"{datetime.now()}: Found {len(renew_links)} listing(s) that can be renewed")

    while len(renew_links):
        renew_links[0].click()
        renewed_listing = driver.find_element_by_id('titletextonly').text
        print(f"{datetime.now()}: Renewed {renewed_listing}")
        driver.get(home_url)
        renew_links = check_for_renewals(driver) #Refresh renewal list
        print(f"{datetime.now()}: Found {len(renew_links)} more listing(s) that can be renewed")

    driver.quit()

if __name__ == '__main__':
    main()
