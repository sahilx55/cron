import os
from os import environ
import logging
from pyrogram import Client, idle, filters
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
import threading
import requests
from datetime import datetime
from pytz import timezone

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

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

botx = os.getenv('BOT')
bot = botx.split(";")
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

app = Client(
    ":memory:",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    plugins=dict(root="botx"),
)

def cronjob():
      threading.Timer(5.0, cronjob).start()
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
          if not A.ok and dead not in ct1:
            app.send_message(chat_id=-1001184862744, text=f'{bot[i]}\n\n😵 Is Dead\n\n{z}', disable_web_page_preview=True)
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
            mnb34x19 = open('check.txt', 'r')
            mnbxop19 = mnb34x19.read()
            mnb34x1 = open('response.txt', 'r')
            mnbxop1 = mnb34x1.read()
            ct1 = eval(mnbxop1)
            ct2 = getList(ct1)
            ct3 = '\n\n----------------\n\n'.join([f'🤖 BOT URL {i+1}: ' + '[' + ct2[i].replace(' Bot Is Alive', '') + '] 🤖\n' + '🟢 Current Status : ALIVE\n\n' + '😵 Dead On: \n' + eval(ct1[ct2[i]].replace('\n', '\\n'))[0] + '\n\n💪 Alive On: \n' + eval(ct1[ct2[i]].replace('\n', '\\n'))[1]
                  if 'Alive' in ct2[i]
                  else 
                  f'🤖 BOT URL {i+1}: ' + '[' + ct2[i].replace(' Bot Is Dead', '') + '] 🤖\n' + '🟡 Current Status : DEAD\n\n' + '💪 Alive On: \n' + eval(ct1[ct2[i]].replace('\n', '\\n'))[0] + '\n\n😵 Dead On: \n' + eval(ct1[ct2[i]].replace('\n', '\\n'))[1]
                  for i in range(len(ct2))])
            logx = f"Last Check On : \n{mnbxop19}\n\n" + ct3
            ftx2c = open("logs.txt", "w")
            ftx2c.write(logx)
            ftx2c.close()
            app.send_document(chat_id=-1001184862744, document="logs.txt")
          if A.ok and alive not in ct1:
            app.send_message(chat_id=-1001184862744, text=f'{bot[i]}\n\n💪 Is Alive\n\n{z}', disable_web_page_preview=True)
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
            mnb34x19 = open('check.txt', 'r')
            mnbxop19 = mnb34x19.read()
            mnb34x1 = open('response.txt', 'r')
            mnbxop1 = mnb34x1.read()
            ct1 = eval(mnbxop1)
            ct2 = getList(ct1)
            ct3 = '\n\n----------------\n\n'.join([f'🤖 BOT URL {i+1}: ' + '[' + ct2[i].replace(' Bot Is Alive', '') + '] 🤖\n' + '🟢 Current Status : ALIVE\n\n' + '😵 Dead On: \n' + eval(ct1[ct2[i]].replace('\n', '\\n'))[0] + '\n\n💪 Alive On: \n' + eval(ct1[ct2[i]].replace('\n', '\\n'))[1]
                  if 'Alive' in ct2[i]
                  else 
                  f'🤖 BOT URL {i+1}: ' + '[' + ct2[i].replace(' Bot Is Dead', '') + '] 🤖\n' + '🟡 Current Status : DEAD\n\n' + '💪 Alive On: \n' + eval(ct1[ct2[i]].replace('\n', '\\n'))[0] + '\n\n😵 Dead On: \n' + eval(ct1[ct2[i]].replace('\n', '\\n'))[1]
                  for i in range(len(ct2))])
            logx = f"Last Check On : \n{mnbxop19}\n\n" + ct3
            ftx2c = open("logs.txt", "w")
            ftx2c.write(logx)
            ftx2c.close()
            app.send_document(chat_id=-1001184862744, document="logs.txt")

if __name__ == "__main__":
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} Started")
    cronjob()
    idle()
    app.stop()
    print("Bot stopped. Alvida!")
