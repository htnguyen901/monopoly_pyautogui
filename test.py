from pywinauto import Application
from pywinauto import Desktop
import time

app = Application(backend='uia').start("C:\Program Files\BlueStacks_nxt\HD-MultiInstanceManager.exe").connect(title='BlueStacks multi-instance manager')
# time.sleep(3)
# app = Desktop().window(title='BlueStacks App Player 1974')
#app2 = Desktop().window(title='Untitled - Notepad')
#app2 = Application(backend='uia').start("notepad.exe").connect(title='Untitled - Notepad')
print('done')
app.BlueStacksMultiInstanceManager.print_control_identifiers()
