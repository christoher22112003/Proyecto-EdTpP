from ast import While
import os
import webbrowser as wb

print("""
 #######   #####     ####     ##     ##   ##  #######   #####
  ##   #  ##   ##   ##  ##   ####    ###  ##   ##   #  ##   ##
  ## #    #        ##       ##  ##   #### ##   ## #    ##   ##
  ####     #####   ##       ##  ##   ## ####   ####    ##   ##
  ## #         ##  ##       ######   ##  ###   ## #    ##   ##
  ##   #  ##   ##   ##  ##  ##  ##   ##   ##   ##   #  ##   ##
 #######   #####     ####   ##  ##   ##   ##  #######   #####

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
*****  Programas que se utilizan en el scaneo de tareas  *****
  __________________________________________________________""")

  print("\t1 - Epson Scanner")
  print("\t2 - Explorar de archivos en la carpeta escaneados")
  print("----------------------------------------------------------")
  print("\t3 - Abrir todos los programas")
  print("----------------------------------------------------------")
  print("\t4 - Volver al menu principal")
  print("\t5 - Salir")
  print("----------------------------------------------------------")
while True:
  menu()
  edt = input(" ¿Que proceso necesitas hacer ? >>>   ")

  if edt=="1":
    edt_1 = input("Has pulsado la opcion 1(Epson Scanner)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

    if edt_1=="s":
      print("Se abrira el programa Epson Scanner")
      wb.open_new(r'C:\Program Files (x86)\epson\Epson Scan 2\Core\es2launcher.exe')
    else:
      print("Se regresara al menu de Escaneo de tareas")

  else:

    if edt=="2":
      edt_2 = input("Has pulsado la opcion 2(Explorador de archivos en la carpeta escaneados)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

      if edt_2=="s":
        print("Se abrira el programa Explorador de archivos en la carpeta escaneados")
        wb.open_new(r'M:\Documents\Ofimatica\Edicion de documentos\Escaneados\Escaneados')
      else:
        print("Se regresara al menu de Escaneo de tareas")

    else:

      if edt=="3":
        edt_3 = input("Has pulsado la opcion 3 (Abrir todos los programas)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

        if edt_3=="s":
          print("Se abrira los programas... \nEpson Scanner \nExplorador de archivos en la carpeta escaneados")
          wb.open_new(r'C:\Program Files (x86)\epson\Epson Scan 2\Core\es2launcher.exe')
          wb.open_new(r'M:\Documents\Ofimatica\Edicion de documentos\Escaneados\Escaneados')
        else:
          print("Se regresara al menu de Escaneo de tareas")

      else:

        if edt=="4":
          edt_4 = input("Has pulsado la opcion 4(Volver al menu principal de envio de tareas)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

          if edt_4=="s":
            print("Se regresara al menu principal de Envio de tareas")
            wb.open_new('M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\p_edtpp_M.py')
            exit()
          else:
            print("Se regresara al menu de Escaneo de tareas")

        else:

          if edt=="5":
            edt_5 = input("Has pulsado la opcion 5(Salir)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

            if edt_5=="s":
              print("Se cerrar el menu de Escaneo de tareas")
              exit()
            else:
              print("Se regresara al menu de Escaneo de tareas")

          else:
            input("No has pulsado ninguna opcion correcta>>>  ")