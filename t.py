import threading
import requests
bot = ['https://classroombysahil.nolia.repl.co/', 'https://ctest.nolia.repl.co/']

def cronjob():
      threading.Timer(5.0, cronjob).start()
      for i in range(len(bot)):
          A = requests.get(bot[i])
          if not A.ok:
            print(bot[i])
            print('BOT IS DEAD')
          else:
            print(bot[i])
            print(A)

cronjob()
