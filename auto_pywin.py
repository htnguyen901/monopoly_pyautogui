from pywinauto.application import Application
import win32gui
from win32gui import GetWindowText, GetForegroundWindow
import pyautogui
import time
import os
import math
import logging
from os.path import join, isfile
IMG_FOLDER = 'images/'
INSTANCE_FEED = int(input("How many instance to run? "))
INSTANCE_PER_RUN = 5
ROOT_DIR = os.getcwd()

def find_to_click(element):
    button = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}{element}.png', confidence=0.8)
    while button is None:
        button = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}{element}.png', confidence=0.8)
    time.sleep(0.5)
    pyautogui.click(button.x, button.y)
    return button

def save_runs_count(count):
    next_fname = join(ROOT_DIR, '.next.txt')
    if isfile(next_fname):
        with open(next_fname, 'w') as f:
            f.write(str(count))

def retrieve_runs_count():
    next_fname = join(ROOT_DIR, '.next.txt')
    if isfile(next_fname):
        with open(next_fname) as f:
            total_count = int(f.read())
    return total_count

def create_clone():
    pyautogui.click(pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}clone_icon.png', confidence=0.8))
    time.sleep(1)
    nb_instance_x, nb_instance_y = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}nb_instances.png', confidence=0.8)
    pyautogui.click(nb_instance_x, nb_instance_y)
    time.sleep(1)
    pyautogui.press('left')
    pyautogui.press('del')
    pyautogui.write(f'{INSTANCE_PER_RUN}')
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}create_button.png', confidence=0.8))

    signal_to_start_all = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}cancel_signal_to_start_all.png', confidence=0.8)
    while signal_to_start_all is not None:
        time.sleep(1)
        signal_to_start_all = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}cancel_signal_to_start_all.png',
                                                             confidence=0.8)
    #time.sleep(25)

def stop_all_instance():
    # stop_all_instance = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}stop_all_instance.png', confidence=0.8)
    # pyautogui.click(stop_all_instance.y, stop_all_instance.y)

    select = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}select_all.png', confidence=0.8)

    pyautogui.click(select.x, select.y)
    time.sleep(1)
    stop = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}stop_all.png', confidence=0.8)
    if stop is not None:
        pyautogui.click(stop.x,stop.y)
        time.sleep(1)
        stop_confirm = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}stop_all_confirmation.png', confidence=0.8)
        pyautogui.click(stop_confirm.x, stop_confirm.y)

def delete_clone():
    search = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}search_bar.png', confidence=0.8)

    if search is not None:
        pyautogui.click(search.x, search.y)
        time.sleep(1)
        pyautogui.write('blue')

    select = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}select_all.png', confidence=0.8)
    pyautogui.click(select.x, select.y)

    delete = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}delete_all.png', confidence=0.8)

    pyautogui.click(delete.x, delete.y)
    time.sleep(0.5)
    del_x, del_y = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}delete_confirmation.png', grayscale=False, confidence=0.8)

    pyautogui.click(del_x+25, del_y)

    pyautogui.click(pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}blue_search_bar.png', grayscale=False, confidence=0.8))

    with pyautogui.hold('shift'):
        pyautogui.press('left', presses=4)
    time.sleep(1)
    pyautogui.press('del', presses=4)

def run_automation():
    global n_completed

    clone_window_lists = []
    while len(clone_window_lists) == 0:
        search_x, search_y = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}search_bar.png', confidence=0.8)
        pyautogui.click(search_x, search_y)
        time.sleep(1)
        pyautogui.write('blue')

        select = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}select_all.png', confidence=0.8)
        while select is None:
            print('Cant find Delete All button')
            select = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}select_all.png', confidence=0.8)
        pyautogui.click(select.x, select.y)

        start_x, start_y = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}start_all.png', grayscale=False, confidence=0.8)
        pyautogui.click(start_x, start_y)
        time.sleep(25)

        clone_window_lists = []
        for x in pyautogui.getAllWindows():
            if x.title.startswith('BlueStacks App'):
                clone_window_lists.append(x.title)
        clone_window_lists = clone_window_lists[::-1]
        print(clone_window_lists)

    run_ = 0
    u = 0

    for clone_window_list in clone_window_lists:
        nth_instance = clone_window_list.split(' ')[-1]
        handle_ = win32gui.FindWindow(0, f'BlueStacks App Player {nth_instance}')
        win32gui.SetForegroundWindow(handle_)
        print(f'Instance foreground {nth_instance}')
        while GetWindowText(GetForegroundWindow()) != clone_window_list:
            win32gui.SetForegroundWindow(handle_)
        #time.sleep(1)

        note_app = None
        link_view = None
        while note_app is None and link_view is None:
            win32gui.SetForegroundWindow(handle_)
            note_app = find_to_click('note_app')
            link_view = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}link_view.png', confidence=0.9)
            while link_view is None:
               # print('finding link view')
                pyautogui.moveTo(1000, 500)
                note_app = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}note_app.png', confidence=0.8)
                while note_app is None:
                    note_app = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}note_app.png', confidence=0.8)
                # while note_app is not None:
                #     #print('app is not opened. found note app')
                pyautogui.click(note_app.x, note_app.y)
                note_app = None
                link_view = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}link_view.png', confidence=0.9)
                while link_view is None:
                    link_view = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}link_view.png', confidence=0.9)
                    #print('found link view')
            print('clicking link view')
            link_view = find_to_click('link_view')

            # while link_view is None:
            #     while note_app is None:
            #         note_app = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}note_app.png', confidence=0.8)
            #         if note_app is not None:
            #             print('clicking on note app')
            #             note_app = find_to_click('note_app')
            #     print('finding link view')
            #     link_view = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}link_view.png', confidence=0.9)
            # print('clicking on link view')
            # link_view = find_to_click('link_view')

        print(run_)
        if run_ == 0:
            run_ = run_+1

        link_click = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}to_link_click.png', confidence=0.9)
        while link_click is None:
            link_view = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}link_view.png', confidence=0.9)
            while link_view is not None:
                pyautogui.click(link_view.x, link_view.y)
                link_view = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}link_view.png', confidence=0.9)
            link_click = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}to_link_click.png', confidence=0.9)
        pyautogui.click(link_click.x, link_click.y)

        if link_click is not None:
            time.sleep(1)
            confirm_link = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}confirm_open_link.png', confidence=0.8)
            while confirm_link is None:
                find_to_click('to_link_click')
                confirm_link = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}confirm_open_link.png', confidence=0.8)
                print('finding confirm button')
            if confirm_link is not None:
                pyautogui.click(confirm_link.x, confirm_link.y)
                u = u + 1
                print(f'Instance passed')
            else:
                print('Link open failed')
        else:
            print(f'Instance failed')

        time.sleep(2)
        print(f'At the end of instance {nth_instance}')

    time.sleep(10)
    return u

def main_run(count_run):
    count_run = retrieve_runs_count()
    Application(backend='uia').start("C:\Program Files\BlueStacks_nxt\HD-MultiInstanceManager.exe", wait_for_idle=False)
    time.sleep(3)
    n_completed = 0
    for i in range(int(math.ceil(INSTANCE_FEED - retrieve_runs_count())/INSTANCE_PER_RUN)):
        print(f'Run {count_run}th')
        create_clone()
        try:
            success_run = run_automation()
            n_completed = n_completed + success_run
            count_run = count_run + success_run
            print(f'Instance ran {count_run}th succeed')
        except:
            print(f'count run failed')
            return count_run
        print(f'Total instances passed: {n_completed}')
        handle = win32gui.FindWindow(0, 'BlueStacks Multi Instance Manager')
        win32gui.SetForegroundWindow(handle)
        #time.sleep(13)
        timeout = 20
        timeout_loading_screen = 20
        timeout_loading_screen_start = time.time()
        loading_screen = None
        while loading_screen is None and time.time() < timeout_loading_screen_start + timeout_loading_screen:
            while loading_screen is None:
                loading_screen = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}loading_screen.png', confidence=0.8)
            # timeout_start = time.time()
            # while loading_screen is None and time.time() < timeout_start + timeout:
            #     loading_screen = find_to_click('loading_screen')
        save_runs_count(count_run)
        stop_all_instance()
        #time.sleep(1)
        done_stopping = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}signal_to_done_stop.png', confidence=0.8)
        while done_stopping is not None:
            done_stopping = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}signal_to_done_stop.png',
                                                           confidence=0.8)
        delete_clone()
        print(f'Completed loop {i}, total instances: {INSTANCE_PER_RUN*(i+1)}')
        print(f'No of count to save {count_run}')
    print(f'Total instances passed: {n_completed}')
    return count_run

trial = 0
if INSTANCE_FEED:
    start_key = input("Press j to run the program ")
    if start_key == 'j':
        while trial < 50:
            try:
                current_total_runs = retrieve_runs_count()
                print(current_total_runs)
                run_ups = main_run(current_total_runs)
                print(f'Successfully completed total of {run_ups} instances for client')
            except Exception as e:
                print(f'Program failed {trial + 1} times')
                trial = trial + 1
                Application(backend='uia').start("C:\Program Files\BlueStacks_nxt\HD-MultiInstanceManager.exe",
                                                 wait_for_idle=False)
                stop_all_instance()
                #time.sleep(7)
                done_stopping = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}signal_to_done_stop.png', confidence=0.8)
                while done_stopping is not None:
                    done_stopping = pyautogui.locateCenterOnScreen(f'{IMG_FOLDER}signal_to_done_stop.png',
                                                                   confidence=0.8)
                delete_clone()
                continue