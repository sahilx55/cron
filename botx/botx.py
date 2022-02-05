import os
from pyrogram import Client, emoji, filters

def getList(dict): 
    list = [] 
    for key in dict.keys(): 
        list.append(key)
    return list

@Client.on_message(filters.command([f"logs"]))
async def logs(client, message):
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
    await client.send_document(chat_id=message.chat.id, document="logs.txt")
