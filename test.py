import win32gui
import pyautogui

clone_window_list =[]
for x in pyautogui.getAllWindows():
    if x.title.startswith('BlueStacks App'):
        clone_window_list.append(x.title)
print(clone_window_list)
# NUM = 590
# handle = win32gui.FindWindow(0, f'BlueStacks App Player {NUM}')
# win32gui.SetForegroundWindow(handle)

print('BlueStacks App Player 591'.split(' ')[-1])
