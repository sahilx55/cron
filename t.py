import os
from os import environ
import threading
import requests
from datetime import datetime
from pytz import timezone
from aiohttp import web
import aiohttp_jinja2
import jinja2
from urllib.request import urlopen
from bs4 import BeautifulSoup

def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z
x = {}

def getvx(dict): 
    list = [] 
    for key in dict.values(): 
        list.append(key)
    return list
def getList(dict): 
    list = [] 
    for key in dict.keys(): 
        list.append(key)
    return list

hostx = os.getcwd()
botx = os.getenv('BOT')
bot = botx.split(";")

def cronjob():
      threading.Timer(20.0, cronjob).start()
      tz = timezone('Asia/Kolkata')
      s = datetime.now(tz).strftime("%H:%M")
      sx = datetime.strptime(s, "%H:%M")
      z ='Date : ' + datetime.now(tz).strftime("%A %d-%m-%Y") + '\nTime : ' + sx.strftime("%r")
      mnb34x1 = open('response.txt', 'r')
      mnbxop1 = mnb34x1.read()
      ct1 = eval(mnbxop1)
      ct0 = {}
      ftx2c = open("check.txt", "w")
      ftx2c.write(z)
      ftx2c.close()
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
              ct2.append('Alive Time Is Not Measured Yet')
            ct0[dead] = f"['{ct2[1]}', '{z}']"
            del ct1[alive]
            l2 = merge_two_dicts(ct1, ct0)
            ftx2 = open("response.txt", "w")
            ftx2.write(repr(l2))
            ftx2.close()
          if A.ok and alive not in ct1:
            if dead not in ct1:
              ct1[dead] = "['Dead1']"
            ct2 = eval(ct1[dead].replace('\n', '\\n'))
            if len(ct2)!=2:
              ct2.append('Dead Time Is Not Measured Yet')
            ct0[alive] = f"['{ct2[1]}', '{z}']"
            del ct1[dead]
            l2 = merge_two_dicts(ct1, ct0)
            ftx2 = open("response.txt", "w")
            ftx2.write(repr(l2))
            ftx2.close()
          

cronjob()

async def hello(request):
    mnb34x19 = open('check.txt', 'r')
    mnbxop19 = mnb34x19.read()
    mnb34x1 = open('response.txt', 'r')
    mnbxop1 = mnb34x1.read()
    ct1 = eval(mnbxop1)
    ct2 = getList(ct1)
    ct3 = '\n\n\n\n'.join([f'🤖 BOT URL {i+1}: ' + '[' + ct2[i].replace(' Bot Is Alive', '') + '] 🤖\n' + '🟢 Current Status : ALIVE\n\n' + '😵 Dead On: \n' + eval(ct1[ct2[i]].replace('\n', '\\n'))[0] + '\n\n💪 Alive On: \n' + eval(ct1[ct2[i]].replace('\n', '\\n'))[1]
                  if 'Alive' in ct2[i]
                  else 
                  f'🤖 BOT URL {i+1}: ' + '[' + ct2[i].replace(' Bot Is Dead', '') + '] 🤖\n' + '🟡 Current Status : DEAD\n\n' + '💪 Alive On: \n' + eval(ct1[ct2[i]].replace('\n', '\\n'))[0] + '\n\n😵 Dead On: \n' + eval(ct1[ct2[i]].replace('\n', '\\n'))[1]
                  for i in range(len(ct2))])
    
    return web.Response(text=f"Last Check On : \n{mnbxop19}\n\n" + ct3)


async def main():
    app = web.Application()
    aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(hostx + '/views'))
    app.add_routes(
        [
            web.get('/', hello)
        ]
    )
    return app

if __name__ == "__main__":
    web.run_app(main())
