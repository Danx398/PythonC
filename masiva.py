import pyautogui as pt
import time

limite = input("cantidad de mensajes: ")
msg = input("Mensaje: ")
i=0

time.sleep(3)

while i < int(limite):
    pt.typewrite(msg)
    pt.press("enter")
    i+=1