import threading
import requests
from datetime import datetime
from pytz import timezone
bot = ['https://google.com/', 'https://gmail.com/']

def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z
x = {}

def cronjob():
      threading.Timer(3.0, cronjob).start()
      tz = timezone('Asia/Kolkata')
      s = datetime.now(tz).strftime("%H:%M")
      sx = datetime.strptime(s, "%H:%M")
      z ='Date : ' + datetime.now(tz).strftime("%A %d-%m-%Y") + '\nTime : ' + sx.strftime("%r")
      mnb34x1 = open('response.txt', 'r')
      mnbxop1 = mnb34x1.read()
      ct1 = eval(mnbxop1)
      ct0 = {}
      print(ct1)
      for i in range(len(bot)):
          A = requests.get(bot[i])
          alive = bot[i] + ' Bot Is Alive'
          dead = bot[i] + ' Bot Is Dead'
          if not A.ok:
            print(bot[i] + ' [BOT IS DEAD]')
          else:
            print(bot[i] + ' [BOT IS ALIVE]')
          if not A.ok and dead not in ct1:
            if alive not in ct1:
              ct1[alive] = "['Alive1']"
            ct2 = eval(ct1[alive].replace('\n', '\\n'))
            if len(ct2)!=2:
              ct2.append('Alive2')
            ct0[dead] = f"['{ct2[1]}', '{z}\n{bot[i]}\nBot Is Dead']"
            l2 = merge_two_dicts(ct1, ct0)
            del l2[alive]
            ftx2 = open("response.txt", "w")
            ftx2.write(repr(l2))
            ftx2.close()
          if A.ok and alive not in ct1:
            if dead not in ct1:
              ct1[dead] = "['Dead1']"
            ct2 = eval(ct1[dead].replace('\n', '\\n'))
            if len(ct2)!=2:
              ct2.append('Dead2')
            ct0[alive] = f"['{ct2[1]}', '{z}\n{bot[i]}\nBot Is Alive']"
            l2 = merge_two_dicts(ct1, ct0)
            del l2[dead]
            ftx2 = open("response.txt", "w")
            ftx2.write(repr(l2))
            ftx2.close()
          

cronjob()
