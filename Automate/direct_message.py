import pyautogui as auto
import pyperclip as clipboard
import time
import pandas as pd

def write_it(message):
    auto.write(message)
    time.sleep(2)
    type_it("enter")
    
def type_it(key):
    auto.press(key)
    time.sleep(1)

if __name__ == "__main__":
    type_it("win")
    write_it("Chrome")
    write_it("Instagram")
    time.sleep(5)
    auto.click(x=1258, y=132)
    time.sleep(5)
    auto.click(x=552, y=303)
    time.sleep(3)
    write_it("fala doido")
    write_it("mandando essa mensagem via automacao em python")
    write_it("pagou um pau, ne?")
