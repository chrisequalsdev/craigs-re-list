# craigslist_renew
Simple Python 3 script to renew craigslist listings with Selenium

### Before running this script you will need to create this .env file in the project folder:
```
LOGIN_PW = 'your password here'
LOGIN_ID = 'your e-mail here'
WEBDRIVER_PATH = 'path to webdriver here'
USER_AGENT = 'your user agent string here'
```
To get your user agent: https://www.google.com/search?q=get+user+agent&oq=get+user+agent

### Toggle Headless

By default this will run headless. You can easily change that by setting

```selenium_options.headless = False```

