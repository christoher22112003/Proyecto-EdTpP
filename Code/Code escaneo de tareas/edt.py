from ast import While
import os

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
print("""
  **********************************************************
*****  Programas que se utilizan en el scaneo de tareas  *****
  __________________________________________________________""")

def menu():
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
    edt_1 = input("Has pulsado la opcion 1...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

    if edt_1=="s":
      print("edt_1s")
      input("Precione una tecla>>>  ")
    else:
      print("edt_1n")

      input("Precione una tecla>>>  ")
  else:

    if edt=="2":
      edt_2 = input("Has pulsado la opcion 2...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

      if edt_2=="2":
        print("edt_2s")
        input("Precione una tecla>>>  ")
      else:
        print("edt_2n")
        input("Precione una tecla>>>  ")

    else:

      if edt=="3":
        edt_3 = input("Has pulsado la opcion 3...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

        if edt_3=="s":
          print("edt_3s")
          input("Precione una tecla>>>  ")
        else:
          print("edt_3n")
          input("Precione una tecla>>>  ")

      else:

        if edt=="4":
          edt_4 = input("Has pulsado la opcion 4...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

          if edt_4=="s":
            print("edt_4s")
            input("Precione una tecla>>>  ")
          else:
            print("edt_4n")
            input("Precione una tecla>>>  ")

        else:

          if edt=="5":
            edt_5 = input("Has pulsado la opcion 5...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

            if edt_5=="s":
              print("edt_5s")
              input("Precione una tecla>>>  ")
              break
            else:
              print("edt_5n")
              input("Precione una tecla>>>  ")

          else:
            input("No has pulsado ninguna opcion correcta>>> ")