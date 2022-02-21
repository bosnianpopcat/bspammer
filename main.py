import pyautogui
import time
print('Enter name of the file with the script you want bspammer to spam (not including extension, extension must be .txt):')
fname = input()
print('Delay between messages (in seconds, must be decimal number (ex. 0.4, 1.0, etc.)):')
dtime = float(input())
print('Time to select the chatbox you want the bot to spam in before the bot start spamming (in seconds, must be a full number (ex. 3, 5, etc.)):')
wtime = int(input())
time.sleep(wtime)
f = open(fname + ".txt", "r")
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")
	time.sleep(dtime)