# in the name of Allah

# initial imports
from datetime import datetime, timezone
from datetime import datetime as dt
import time

# telegram imports
from telethon.sync import TelegramClient

# creat table
import dataset
con = dataset.sql_connection()
dataset.sql_table(con)

# setup / change only the first time you use it
username = 'Hz_mazinani' # here you put your username from your telegram account
phone = '+989912013899'  # here you put your phone number from your telegram account
api_id = '4839324' # here you put your api_id from https://my.telegram.org/apps
api_hash = '2bdf43e1cb92fedbe611a7e36723b52e' # here you put your api_hash from https://my.telegram.org/apps

data = []
url = ''
index = 1

# setup / change every time to use to define scraping
channel = '@PalestineNews' # here you put the name of the channel or group that you want to scrap (ex: '@jairbolsonarobrasil' or 'https://t.me/jairbolsonarobrasil/' / not: 'https://web.telegram.org/z/#-1273465589' or '-1273465589')
worksheet_name = 'PalestineNews' # here you put the name of the file you want as output, it will create a file on your google drive home screen
d_min = 1 # start day / this date will be included
m_min = 1 # start month
y_min = 2021 # start year
d_max = 9 # final day / only the day before this date will be included, that is, this date will not be included
m_max = 11 # final month
y_max = 2023 # final year
key_search = '' # only if you want to search a keyword, if not, keep as ''
