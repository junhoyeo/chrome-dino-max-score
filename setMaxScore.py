import os
import json
import signal
import threading
from time import sleep
from chromote import Chromote

COMMAND = "'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' --remote-debugging-port=9222"

thread = threading.Thread(target=os.system, args=(COMMAND,))
thread.start()
sleep(3)

chrome = Chromote()

tab = chrome.tabs[0]
print(tab.set_url('chrome://dino'))
sleep(3)

res = tab.evaluate('window.errorPageController.updateEasterEggHighScore(67999979)')
print(res)

data = json.loads(res)
if data['result']['result']['value']:
  print('🦖 Success')

print(tab.reload())
print(tab.evaluate('Runner.instance_.playIntro()'))

os.kill(os.getpid(), signal.SIGTERM)
