from pywinauto.application import Application
from pywinauto import Desktop
import threading,subprocess,base64,cv2,random,requests,pyautogui
import os, time

IMG_FOLDER = 'images/'
print(f'{IMG_FOLDER}search_bar.png')

def create_clone():
    pyautogui.click(pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}clone_icon.png', grayscale=False))
    # try:
    #     pyautogui.click(pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}instance_to_clone_field.png', grayscale=False))
    #     pyautogui.click(pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}no_touch_instance.png', grayscale=False))
    # except:
    #     print(f'instance is already set to no_touch')
    time.sleep(1)
    nb_instance_x, nb_instance_y = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}nb_instances.png', confidence=0.5)
    pyautogui.click(nb_instance_x, nb_instance_y)
    time.sleep(1)
    pyautogui.press('left')
    pyautogui.press('del')
    pyautogui.write('5')
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}create_button.png', confidence=0.8))
    time.sleep(30)

def delete_clone():
    search = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}search_bar.png')
    print(search)
    if search is not None:
        pyautogui.click(search.x, search.y)
        time.sleep(1)
        pyautogui.write('blue')

    stop = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}stop_all.png')
    if stop is not None:
        pyautogui.click(stop.x, stop.y)
        time.sleep(1)
        pyautogui.write('blue')


    time.sleep(1)
    select = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}select_all.png')
    print(select)
    pyautogui.click(select.x, select.y)
    time.sleep(1)

    delete = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}delete_all.png', confidence=0.8)
    print(f'delete all button is {delete}')
    pyautogui.click(delete.x, delete.y)
    time.sleep(0.5)
    del_x, del_y = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}delete_confirmation.png', grayscale=False, confidence=0.8)
    print(del_x, del_y)
    pyautogui.click(del_x+25, del_y)

    pyautogui.click(pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}blue_search_bar.png', grayscale=False))

    with pyautogui.hold('shift'):
        pyautogui.press('left', presses=4)
    time.sleep(1)
    pyautogui.press('del', presses=4)

def run_automation():
    search_x, search_y = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}search_bar.png')
    pyautogui.click(search_x, search_y)
    time.sleep(2)
    pyautogui.write('blue')

    #select_x, select_y = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}select_all.png')
    pyautogui.click(f'{IMG_FOLDER}select_all.png')

    start_x, start_y = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}start_all.png', grayscale=False)
    pyautogui.click(start_x, start_y)
    time.sleep(50)

    for i in range(5):
        pyautogui.click(pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}note_app.png'))
        if i == 0:
            time.sleep(8)
        else:
            time.sleep(4)
        pyautogui.click(pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}link_view.png'))
        time.sleep(3)

        pyautogui.click(pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}to_link_click.png'))
        time.sleep(25)

        pyautogui.click(pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}agree_button.png'))
        time.sleep(2)

        pyautogui.click(pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}close_button.png'))
        time.sleep(2)
        pyautogui.click(pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}close_instance.png', confidence=0.8))
        time.sleep(2)

app = Application(backend='uia').start("C:\Program Files\BlueStacks_nxt\HD-MultiInstanceManager.exe", wait_for_idle=False)
time.sleep(1)
#delete_clone()
for i in range(60):
    create_clone()
    run_automation()
    time.sleep(5)
    delete_clone()