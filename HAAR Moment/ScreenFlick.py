import imp
import win32gui
import time
import pyautogui 


def screenshot(window_title="FTL: Faster Than Light"):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(x, y, x1, y1))
            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im






time.sleep(10)

screenshot()
