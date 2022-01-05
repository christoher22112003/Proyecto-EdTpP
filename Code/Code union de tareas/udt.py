from ast import While
import os

print("""
      ##   ##  ##   ##   ####     #####   ##   ##
      ##   ##  ###  ##    ##     ##   ##  ###  ##
      ##   ##  #### ##    ##     ##   ##  #### ##
      ##   ##  ## ####    ##     ##   ##  ## ####
      ##   ##  ##  ###    ##     ##   ##  ##  ###
      ##   ##  ##   ##    ##     ##   ##  ##   ##
        #####   ##   ##   ####     #####   ##   ##

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
    udt_1 = input("Has pulsado la opcion 1...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

    if udt_1=="s":
      print("udt_1s")
      input("Precione una tecla>>>  ")
    else:
      print("udt_1n")

      input("Precione una tecla>>>  ")
  else:

    if udt=="2":
      udt_2 = input("Has pulsado la opcion 2...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

      if udt_2=="2":
        print("udt_2s")
        input("Precione una tecla>>>  ")
      else:
        print("udt_2n")
        input("Precione una tecla>>>  ")

    else:

      if udt=="3":
        udt_3 = input("Has pulsado la opcion 3...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

        if udt_3=="s":
          print("udt_3s")
          input("Precione una tecla>>>  ")
        else:
          print("udt_3n")
          input("Precione una tecla>>>  ")

      else:

        if udt=="4":
          udt_4 = input("Has pulsado la opcion 4...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

          if udt_4=="s":
            print("udt_4s")
            input("Precione una tecla>>>  ")
          else:
            print("udt_4n")
            input("Precione una tecla>>>  ")

        else:

          if udt=="5":
            udt_5 = input("Has pulsado la opcion 5...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

            if udt_5=="s":
              print("udt_5s")
              input("Precione una tecla>>>  ")
              break
            else:
              print("udt_5n")
              input("Precione una tecla>>>  ")

          else:
            input("No has pulsado ninguna opcion correcta>>> ")