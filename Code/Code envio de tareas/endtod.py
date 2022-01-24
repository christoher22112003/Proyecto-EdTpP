import pyautogui as pyto
import webbrowser as wb
import time

print("""
                #####   ##   ##  #######
              ##    ##  ###  ##   ##   #
              ##    ##  #### ##   ## #
              ##    ##  ## ####   ####
              ##    ##  ##  ###   ## #
              ##    ##  ##   ##   ##   #
                #####   ##   ##  #######

      #####    ######   ####    ##   ##  #######
      ## ##    ##  ##    ##     ##   ##   ##   #
      ##  ##   ##  ##    ##      ## ##    ## #
      ##  ##   #####     ##      ## ##    ####
      ##  ##   ## ##     ##       ###     ## #
      ## ##    ##  ##    ##       ###     ##   #
      #####    #### ##  ####       #     #######

""")
print("""
        **********************************************************
      ***** Programas que se utilizan en el envio de tareas on *****
        __________________________________________________________""")

def menu():
  print("\t1 - One drive")
  print("\t2 - Explorador de archivos en la carpeta combinados")
  print("----------------------------------------------------------")
  print("\t3 - Abrir todos los programas")
  print("----------------------------------------------------------")
  print("\t4 - Volver al menu de envio")
  print("\t5 - Volver al menu principal")
  print("\t6 - Salir")
  print("----------------------------------------------------------")
while True:
  menu()
  on = input(" ¿Que proceso necesitas hacer ? >>>   ")

  if on=="1":
    on_1 = input("Has pulsado la opcion 1(One drive)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

    if on_1=="s":
      print("Se abrira el programa Thunderbird cliente de correo electronico")
      wb.open_new(r'https://educacionec-my.sharepoint.com/:f:/g/personal/martha_ashqui_educacion_gob_ec/Enp4DXltIGxOm4MMf7YVxn0BtBuYp9v-Bg-F_gF-PG1J1A?e=ii8uG3')
    else:
      print("Se regresara al menu de envio de tareas por medio de one drive")

  else:

    if on=="2":
      on_2 = input("Has pulsado la opcion 2(Explorador de archivos en la carpeta combinados)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

      if on_2=="2":
        print("Se abrira el programa Thunderbird cliente de correo electronico")
        wb.open_new(r'M:\Documents\Ofimatica\Edicion de documentos\Combinados')
      else:
        print("Se regresara al menu de envio de tareas por medio de one drive")

    else:

      if on=="3":
        on_3 = input("Has pulsado la opcion 3(Abrir todos los programas)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

        if on_3=="s":
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
        else:
          print("Se regresara al menu de envio de tareas por medio de one drive")

      else:

        if on=="4":
          on_4 = input("Has pulsado la opcion 4(Volver al menu de envio)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

          if on_4=="s":
            print("Se regresara al menu principal de Envio de tareas")
            wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Code envio de tareas\endt.py')
            exit()
          else:
            print("Se regresara al menu de envio de tareas por medio de one drive")

        else:

          if on=="5":
            on_5 = input("Has pulsado la opcion 5(Volver al menu principal)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

            if on_5=="s":
              print("Se regresara al menu principal de Envio de tareas")
              wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\p_edtpp_M.py')
              exit()
            else:
              print("Se regresara al menu de envio de tareas por medio de one drive")

          else:
            if on=="6":
              on_6 = input("Has pulsado la opcion 6(Salir)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

              if on_6=="s":
                print("Se cerrar el menu de Envio de tareas por medio de correro electrnocio")
                exit()
              else:
                print("Se regresara al menu de envio de tareas por medio de one drive")

            else:

              input("No has pulsado ninguna opcion correcta>>> ")