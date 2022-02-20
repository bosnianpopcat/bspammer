import pyautogui
import time
print('Enter name of the file with the script you want bspammer to spam (not including extension, extension must be .txt:')
fname = input()
print('You have 5 seconds to select the type field you want the bot to spam in before the bot starts spamming.')
time.sleep(5)
f = open(fname + ".txt", "r")
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")
	time.sleep(0.4)
