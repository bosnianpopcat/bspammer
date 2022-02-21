import pyautogui
import time
print('Enter name of the file with the script you want bspammer to spam (not including extension, extension must be .txt):')
fname = input()
print('Delay between messages (in seconds):')
dtime = input()
print('Time to select the chat box you want the bot to spam in before the bot starts spamming (in seconds):')
wtime = input()
time.sleep(wtime)
f = open(fname + ".txt", "r")
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")
	time.sleep(dtime)