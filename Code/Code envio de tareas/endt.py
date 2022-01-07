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
      wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Taskkill\tke.bat')
    else:
      print("endt_1n")


  else:

    if endt=="2":
      endt_2 = input("Has pulsado la opcion 2...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

      if endt_2=="s":
        wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Taskkill\tke.bat')
      else:
        print("endt_2n")

    else:

      if endt=="3":
        endt_3 = input("Has pulsado la opcion 3...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

        if endt_3=="s":
          print("endt_3s")
        else:
          print("endt_3n")

      else:

        if endt=="4":
          endt_4 = input("Has pulsado la opcion 4...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

          if endt_1=="s":
            print("endt_4s")
            exit()
          else:
            print("endt_4n")

        else:
          input("No has pulsado ninguna opcion correcta>>> ")