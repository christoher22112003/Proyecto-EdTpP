from turtle import left
import webbrowser as wb
import pyautogui as pyto
import time
import sys

# idce = input("Escriba el correo electronico de la profesora>>>   ") (Esta linea de codigo es si se envian a mas de una persona las tareas)
idce = "aklexysmuzo33@outlook.com"

print("""
  --------------------------------------
****    Nombre del archivo pdf >>>    ****
  --------------------------------------
""")
pn = input("¿Que numero de proyecto?>>>   ")
s = input("¿Que numero de semana?>>>   ")
d1 = input("¿Que dia empieza?>>>   ")
d2 = input("¿Que dia termina?>>>   ")
m = input ("¿Que mes se realiza?>>>   ")
a = input ("¿Que año se realiza?>>>   ")

ndapdf = "Proyecto numero " + pn + " Semana numero "+ s + " ("+ d1 + " - " + d2 + " del "+ m + " del año "+ a + " )"

adce = "Deber de domenica Muzo" + ndapdf

wb.open_new(r'C:\Program Files\Mozilla Thunderbird\thunderbird.exe')

time.sleep(10)

pyto.moveTo(x = 221, y = 148, duration = 1)
pyto.scroll(-800)
pyto.moveTo(x = 126, y = 575, duration = 1)
pyto.click(button="left")
pyto.moveTo(x = 443, y = 170, duration = 1)
pyto.click(button="left")

time.sleep(5)

pyto.write(idce)

time.sleep(2)

pyto.press("tab")

time.sleep(2)

pyto.press("tab")
pyto.write(adce)

wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Taskkill\tke.bat')

time.sleep(3)

wb.open_new(r'M:\Documents\Ofimatica\Edicion de documentos\Envio temporal')

time.sleep(3)

pyto.moveTo(x = 1270,y = 623,duration= 2)
pyto.click(button="left")
pyto.hotkey("ctrl", "e")
pyto.moveTo(x = 622,y = 385,duration = 1)
pyto.dragTo(x = 158,y = 550,duration = 5,button="left")
pyto.dragTo(x = 1514,y = 169,duration= 3)
pyto.click(button="left")
pyto.moveTo(x =  36,y =  91,duration = 10)
pyto.click(button="left")

time.sleep(60)

wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Taskkill\tkt.bat')