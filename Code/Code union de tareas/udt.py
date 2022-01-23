import os
import webbrowser as wb
import time
import pyautogui as pyto

print("""
      ##   ##  ##   ##   ####     #####   ##   ##
      ##   ##  ###  ##    ##     ##   ##  ###  ##
      ##   ##  #### ##    ##     ##   ##  #### ##
      ##   ##  ## ####    ##     ##   ##  ## ####
      ##   ##  ##  ###    ##     ##   ##  ##  ###
      ##   ##  ##   ##    ##     ##   ##  ##   ##
      #####    ##   ##   ####     #####   ##   ##

                    #####    #######
                    ## ##    ##   #
                    ##  ##   ## #
                    ##  ##   ####
                    ##  ##   ## #
                    ## ##    ##   #
                    #####    #######

 ######     ##     ######   #######    ##      #####
 # ## #    ####     ##  ##   ##   #   ####    ##   ##
   ##     ##  ##    ##  ##   ## #    ##  ##   #
   ##     ##  ##    #####    ####    ##  ##    #####
   ##     ######    ## ##    ## #    ######        ##
   ##     ##  ##    ##  ##   ##   #  ##  ##   ##   ##
  ####    ##  ##   #### ##  #######  ##  ##    #####
""")

def menu():
  print("""
  **********************************************************
*****  Programas que se utilizan en el union de tareas  *****
  __________________________________________________________""")
  print("\t1 - Nitro pdf")
  print("\t2 - Explorar de archivos en la carpeta escaneados y combinados")
  print("----------------------------------------------------------")
  print("\t3 - Abrir todos los programas")
  print("----------------------------------------------------------")
  print("\t4 - Volver al menu principal")
  print("\t5 - Salir")
  print("----------------------------------------------------------")
while True:
  menu()
  udt = input(" ¿Que proceso necesitas hacer ? >>>   ")

  if udt=="1":
    udt_1 = input("Has pulsado la opcion 1(Nitro pdf)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

    if udt_1=="s":
      print("Se abrira el programa Nitro pdf")
      wb.open_new(r'C:\Program Files\Nitro\Pro\13\NitroPDF.exe')
    else:
      print("Se regresara al menu de Union de tareas")

  else:

    if udt=="2":
      udt_2 = input("Has pulsado la opcion 2(Explorar de archivos en la carpeta escaneados y combinados)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

      if udt_2=="s":
        print("Se abrira el programa Explorar de archivos en la carpeta escaneados y combinados")
        wb.open_new(r'M:\Documents\Ofimatica\Edicion de documentos\Escaneados\Escaneados')
        wb.open_new(r'M:\Documents\Ofimatica\Edicion de documentos\Combinados')
      else:
        print("Se regresara al menu de Union de tareas")

    else:

      if udt=="3":
        udt_3 = input("Has pulsado la opcion 3(Abrir todos los programas)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

        if udt_3=="s":
          print("Se abrira los programas... \nNitro pdf(Manejo de para unir) \nExplorar de archivos en la carpeta escaneados y combinados")
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

        else:
          print("Se regresara al menu de Union de tareas")

      else:

        if udt=="4":
          udt_4 = input("Has pulsado la opcion 4(Volver al menu principal)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

          if udt_4=="s":
            print("Se regresara al menu principal de Envio de tareas")
            wb.open_new('M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\p_edtpp_M.py')
            exit()
          else:
            print("Se regresara al menu de Union de tareas")

        else:

          if udt=="5":
            udt_5 = input("Has pulsado la opcion 5(Salir)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

            if udt_5=="s":
              print("Se cerrar el menu de Union de tareas")
              exit()
            else:
              print("Se regresara al menu de Union de tareas")

          else:
            input("No has pulsado ninguna opcion correcta>>>  ")