Simple Python script to renew craigslist listings with Selenium. Requires Python 3.8 or above.

## Setup

Clone the repo then create a venv:
```
python3 -m venv venv
```

## Install pip packages

Activate the venv:
```
source venv/bin/activate
```

Install packages:
```
pip install -r requirements.txt
```

## Configure 

Create a file called `.env` in the cloned repo folder to hold your login credentials.

```
LOGIN_PW = 'your password here'
LOGIN_ID = 'your e-mail here'
USER_AGENT = 'your user agent string here'
```
To get your user agent: https://www.google.com/search?q=get+user+agent&oq=get+user+agent

## Toggle Headless

By default this will run headless. To disable use `--no-headless`

## Run script via crontab on Linux

Add your username & full path to the cloned repo folder to the following and save as `/etc/cron.d/renew` 

```
PROJECT_FOLDER=<cloned repo folder>
0 17 * * * <username> $PROJECT_FOLDER/venv/bin/python $PROJECT_FOLDER/renew.py >> $PROJECT_FOLDER/renew.log 2>&1
```