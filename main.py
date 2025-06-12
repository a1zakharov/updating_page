import pyautogui
import time

print("Скрипт запущен. Нажатие F5 будет происходить раз в минуту.")
print("Для остановки нажми Ctrl+C.")

try:
    while True:
        pyautogui.press("f5")
        print("F5 нажата.")
        time.sleep(60)
except KeyboardInterrupt:
    print("Скрипт остановлен.")
