from pyautogui import *
import pyautogui
import time
import keyboard
import win32api
import win32con
from loguru import logger


def _click(x, y):
    # print("pressing ", x, y)
    _move(x, y)
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def _move(x, y):
    win32api.SetCursorPos((x, y))


while keyboard.is_pressed('q') == False:

    if pyautogui.locateOnScreen('Team.png', region=(3, 520, 445, 304), grayscale=True, confidence=0.7) != None:
        logger.info("unclicking teaming option..")
        _click(171, 675)
        time.sleep(1)

    if pyautogui.locateOnScreen('ManuNotReady.png', region=(0,538,447,528), grayscale=True, confidence=0.7) != None:
        logger.info("clicking ready button..")
        _click(300, 1000)
        time.sleep(0.5)
                
    if pyautogui.locateOnScreen('ManuReady.png', region=(0,538,447,528), grayscale=True, confidence=0.7) != None:
        logger.info("Waiting to join lobby..")
        time.sleep(5)
    
    
    if pyautogui.locateOnScreen('InGame.png', region=(87,755,379,304), grayscale=True, confidence=0.8) != None:
        logger.info("In game waiting..")
        keyboard.press_and_release('W')
        time.sleep(10)
    
    if pyautogui.locateOnScreen('dead.png', region=(441,19,1017,304), grayscale=True, confidence=0.6) != None:
        logger.info("game end, returning to lobby..")
        _click(1771, 1040)
        time.sleep(0.5)
        _click(1771, 1040)
                
    
    if pyautogui.locateOnScreen('leave.png', region=(0,0,1920,1080), grayscale=True, confidence=0.6) != None:
        _click(963, 623)
        time.sleep(0.5)
     
    if pyautogui.locateOnScreen('space.png', region=(676,777,619,304), grayscale=True, confidence=0.6) != None:
        keyboard.press_and_release('space')
     
    if pyautogui.locateOnScreen('yes.png', region=(506,550,912,304), grayscale=True, confidence=0.6) != None:
        _click(850, 713)
        time.sleep(0.5)
        _click(850, 713)
         
    if pyautogui.locateOnScreen('jump.PNG', region=(715,743,513,304), grayscale=True, confidence=0.9) != None:
        keyboard.press_and_release('Enter')
        time.sleep(0.5)
        keyboard.press_and_release('L')
        time.sleep(0.5)
        keyboard.press_and_release('O')
        time.sleep(0.5)
        keyboard.press_and_release('L')         
        time.sleep(0.5)
        keyboard.press_and_release('Enter')

    if pyautogui.locateOnScreen('Contunue.PNG', region=(773,581,379,304), grayscale=True, confidence=0.6) != None:
        _click(952, 717)
        time.sleep(0.5)
        _click(952, 717)
         
    if pyautogui.locateOnScreen('startmanu.PNG', region=(773,581,379,304), grayscale=True, confidence=0.6) != None:
        _click(952, 717)
        time.sleep(0.5)
        _click(952, 717)
