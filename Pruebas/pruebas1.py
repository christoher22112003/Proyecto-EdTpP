
from tkinter import X
from tkinter.constants import Y
import time
import webbrowser as wb
import pyautogui as pyto

pn = "1"
s = "2"
d1 = "3"
d2 = "4"
m = "5"
a = "6"

ndapdf = "Proyecto numero " + pn + " Semana numero "+ s + " ("+ d1 + " - " + d2 + " del "+ m + " de año "+ a + " )"

wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Taskkill\tke.bat')

time.sleep(5)

wb.open_new(r'M:\Documents\Ofimatica\Edicion de documentos\Escaneados\Escaneados')

time.sleep(5)

pyto.hotkey("ctrl", "e")

pyto.moveTo(x = 800, y = 550, duration=1)
pyto.click(button="right")
pyto.moveTo(x = 912, y = 280, duration=1)
pyto.click(button="left")

time.sleep(5)

pyto.moveTo(x = 1068, y =692, duration=1)
pyto.click(button="left")
pyto.moveTo(x = 808, y = 557, duration=1)
pyto.click(button="left")

time.sleep(3)

i = 1

while i <= 13:
  pyto.press("backspace")
  i = i + 1

time.sleep(3)

pyto.write(ndapdf)

pyto.moveTo(x = 1041, y = 632, duration=1)
pyto.click(button="left")

time.sleep(5)

wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Taskkill\tke.bat')
wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Taskkill\tknp.bat')

exit()