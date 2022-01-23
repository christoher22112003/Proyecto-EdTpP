from ast import While
import os
import webbrowser as wb

print("""
 #######  ##   ##  ##   ##   ####     #####
  ##   #  ###  ##  ##   ##    ##     ##   ##
  ## #    #### ##   ## ##     ##     ##   ##
  ####    ## ####   ## ##     ##     ##   ##
  ## #    ##  ###    ###      ##     ##   ##
  ##   #  ##   ##    ###      ##     ##   ##
 #######  ##   ##     #      ####     #####

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
print("""
  **********************************************************
*****  Programas que se utilizan en la union  de tareas  *****
  __________________________________________________________""")

def menu():
  print("\t1 - One drive")
  print("\t2 - Correo Electronico")
  print("----------------------------------------------------------")
  print("\t3 - Volver al menu principal")
  print("\t4 - Salir")
  print("----------------------------------------------------------")
while True:
  menu()
  endt = input(" ¿Que proceso necesitas hacer ? >>>   ")

  if endt=="1":
    endt_1 = input("Has pulsado la opcion 1...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

    if endt_1=="s":
      print("Se abrira el Envio de tareas por medio de one drive")
      wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Taskkill\tke.bat')
      wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Code envio de tareas\endtod.py')
      exit()
    else:
      print("Se regresara al menu de envio de tareas")


  else:

    if endt=="2":
      endt_2 = input("Has pulsado la opcion 2(Envio por medio de correo electronico)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

      if endt_2=="s":
        print("Se abrira el envio de tareas por medio de correo electronico")
        wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Taskkill\tke.bat')
        wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Code envio de tareas\endtce.py')
        exit()
      else:
        print("Se regresara al menu de envio de tareas")

    else:

      if endt=="3":
        endt_3 = input("Has pulsado la opcion 3...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

        if endt_3=="s":
          print("Se regresara al menu principal de Envio de tareas")
          wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\p_edtpp_M.py')
          exit()
        else:
          print("Se regresara al menu de envio de tareas")

      else:

        if endt=="4":
          endt_4 = input("Has pulsado la opcion 4(Salir)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

          if endt_1=="s":
            print("Se cerrar el menu de Envio de tareas")
            exit()
          else:
            print("Se regresara al menu de envio de tareas")

        else:
          input("No has pulsado ninguna opcion correcta>>> ")