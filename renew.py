from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os, argparse
from datetime import datetime

load_dotenv()

def config_selenium(headless):
    selenium_options = Options()
    # selenium_options.add_argument("--no-sandbox")
    if not headless == False:
        selenium_options.add_argument("--headless=new")
    user_agent = os.getenv('USER_AGENT') 
    selenium_options.add_argument('user-agent={0}'.format(user_agent))
    return selenium_options

def get_driver(home_url, headless):
    selenium_options = config_selenium(headless)
    driver = webdriver.Chrome(service=Service(), options=selenium_options)
    driver.get(home_url)
    return driver

def login(driver):
    username = driver.find_element(by=By.NAME, value='inputEmailHandle')
    username.send_keys(os.getenv('LOGIN_ID'))
    password = driver.find_element(by=By.NAME, value='inputPassword')
    password.send_keys(os.getenv('LOGIN_PW'))
    driver.find_element(by=By.XPATH, value='//*[@id="login"]').click()

def check_for_renewals(driver):
    renew_links = driver.find_elements(by=By.XPATH, value="//input[contains(@class, 'managebtn') and contains(@value, 'renew')]")
    return renew_links

parser = argparse.ArgumentParser()
parser.add_argument('--headless', action=argparse.BooleanOptionalAction, help="Use --no-headless to show browser")

def main():
    home_url = 'https://accounts.craigslist.org/login/home'
    driver = get_driver(home_url, args.headless)
    login(driver)
    renew_links = check_for_renewals(driver)
    print(f"{datetime.now()}: Found {len(renew_links)} listing(s) that can be renewed")

    while renew_links:
        renew_links[0].click()
        renewed_listing = driver.find_element(by=By.ID, value='titletextonly').text
        print(f"{datetime.now()}: Renewed {renewed_listing}")
        driver.get(home_url)
        renew_links = check_for_renewals(driver) #Refresh renewal list
        print(f"{datetime.now()}: Found {len(renew_links)} more listing(s) that can be renewed")

    driver.quit()

if __name__ == '__main__':
    args = parser.parse_args()
    main()
