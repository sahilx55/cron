import threading
import requests
from datetime import datetime
from pytz import timezone
bot = ['https://classroombysahil.nolia.repl.co/', 'https://ctest.nolia.repl.co/']

def cronjob():
      threading.Timer(3.0, cronjob).start()
      tz = timezone('Asia/Kolkata')
      s = datetime.now(tz).strftime("%H:%M")
      sx = datetime.strptime(s, "%H:%M")
      z ='Date : ' + datetime.now(tz).strftime("%A %d-%m-%Y") + '\nTime : ' + sx.strftime("%r")
      print(z)
      for i in range(len(bot)):
          A = requests.get(bot[i])
          if not A.ok:
            print(bot[i])
            print('BOT IS DEAD')
          else:
            print(bot[i])
            print('BOT IS ALIVE')

cronjob()
