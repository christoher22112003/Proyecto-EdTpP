import pyautogui as pyto
import webbrowser as wb
import time

pasword = "MTDL3C20"

wb.open_new(r'https://educacionec-my.sharepoint.com/:f:/g/personal/martha_ashqui_educacion_gob_ec/Enp4DXltIGxOm4MMf7YVxn0BtBuYp9v-Bg-F_gF-PG1J1A?e=ii8uG3')

time.sleep(15)

pyto.moveTo(x = 708,y = 541,duration = 3)
pyto.click(button="left")
pyto.write(pasword)

time.sleep(5)

pyto.press("enter")

wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Taskkill\tke.bat')

time.sleep(3)

wb.open_new(r'M:\Documents\Ofimatica\Edicion de documentos\Envio temporal')

time.sleep(3)

pyto.moveTo(x = 1270,y = 623,duration= 2)
pyto.click(button="left")
pyto.hotkey("ctrl", "e")