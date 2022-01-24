import webbrowser as wb
import pyautogui as pyto
import time

print("""
                    ####    #####   ######   ######   #######   #####
                  ##  ##  ##   ##   ##  ##   ##  ##   ##   #  ##    ##
                  ##      ##   ##   ##  ##   ##  ##   ## #    ##    ##
                  ##      ##   ##   #####    #####    ####    ##    ##
                  ##      ##   ##   ## ##    ## ##    ## #    ##    ##
                  ##  ##  ##   ##   ##  ##   ##  ##   ##   #  ##    ##
                    ####    #####   #### ##  #### ##  #######   #####


#######   ####     #######    ####   ######   ######    #####   ##   ##   ####      ####    #####
  ##   #   ##       ##   #   ##  ##  # ## #    ##  ##  ##   ##  ###  ##    ##      ##  ##  ##   ##
  ## #     ##       ## #    ##         ##      ##  ##  ##   ##  #### ##    ##     ##       ##   ##
  ####     ##       ####    ##         ##      #####   ##   ##  ## ####    ##     ##       ##   ##
  ## #     ##   #   ## #    ##         ##      ## ##   ##   ##  ##  ###    ##     ##       ##   ##
  ##   #   ##  ##   ##   #   ##  ##    ##      ##  ##  ##   ##  ##   ##    ##      ##  ##  ##   ##
#######   #######  #######    ####    ####    #### ##   #####   ##   ##   ####      ####    #####


        """)
print("""
          **********************************************************
        *****  Programas que se utilizan en envio de tareas CE    *****
          __________________________________________________________""")

def menu():
  print("\t1 - Thunderbird (Cliente de correo electronio)")
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
    on_1 = input("Has pulsado la opcion 1(Thunderbird (Cliente de correo electronio)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

    if on_1=="s":
      print("Se abrira el programa Thunderbird cliente de correo electronico")
      wb.open_new(r'C:\Program Files\Mozilla Thunderbird\thunderbird.exe')
    else:
      print("Se regresara al menu de envio de tareas por medio de correro electronico")

  else:

    if on=="2":
      on_2 = input("Has pulsado la opcion 2(Explorador de archivos en la carpeta combinados)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

      if on_2=="2":
        print("Se abrira el programa Thunderbird cliente de correo electronico")
        wb.open_new(r'M:\Documents\Ofimatica\Edicion de documentos\Combinados')
      else:
        print("Se regresara al menu de envio de tareas por medio de correro electronico")

    else:

      if on=="3":
        on_3 = input("Has pulsado la opcion 3(Abrir todos los programas)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

        if on_3=="s":
          idce = "ibeth.salto@estudiantes.edu.ec"

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
        else:
          print("Se regresara al menu de envio de tareas por medio de correro electronico")

      else:

        if on=="4":
          on_4 = input("Has pulsado la opcion 4(Volver al menu de envio)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

          if on_4=="s":
            print("Se regresara al menu principal de Envio de tareas")
            wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Code envio de tareas\endt.py')
            exit()
          else:
            print("Se regresara al menu de envio de tareas por medio de correro electronico")

        else:

          if on=="5":
            on_5 = input("Has pulsado la opcion 5(Volver al menu principal)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

            if on_5=="s":
              print("Se regresara al menu principal de Envio de tareas")
              wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\p_edtpp_M.py')
              exit()
            else:
              print("Se regresara al menu de envio de tareas por medio de correro electronico")

          else:
            if on=="6":
              on_6 = input("Has pulsado la opcion 6(Salir)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

              if on_6=="s":
                print("Se cerrar el menu de Envio de tareas por medio de correro electrnocio")
                exit()
              else:
                print("Se regresara al menu de envio de tareas por medio de correro electronico")

            else:

              input("No has pulsado ninguna opcion correcta>>> ")