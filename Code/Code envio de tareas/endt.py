from ast import While
import os

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
      print("""
                #####   ##   ##  #######
              ##    ##  ###  ##   ##   #
              ##    ##  #### ##   ## #
              ##    ##  ## ####   ####
              ##    ##  ##  ###   ## #
              ##    ##  ##   ##   ##   #
                #####   ##   ##  #######

      #####    ######    ####    ##   ##  #######
        ## ##    ##  ##    ##     ##   ##   ##   #
        ##  ##   ##  ##    ##      ## ##    ## #
        ##  ##   #####     ##      ## ##    ####
        ##  ##   ## ##     ##       ###     ## #
        ## ##    ##  ##    ##       ###     ##   #
      #####    #### ##   ####       #     #######

      """)
      print("""
        **********************************************************
      *****  Programas que se utilizan en la union  de tareas  *****
        __________________________________________________________""")

      def menu():
        print("\t1 - Share point")
        print("\t2 - Correo Electronico")
        print("----------------------------------------------------------")
        print("\t3 - Volver al menu de envio")
        print("\t4 - Volver al menu principal")
        print("\t5 - Salir")
        print("----------------------------------------------------------")
      while True:
        menu()
        on = input(" ¿Que proceso necesitas hacer ? >>>   ")

        if on=="1":
          on_1 = input("Has pulsado la opcion 1...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

          if on_1=="s":
            print("on_1s")
            input("Precione una tecla>>>  ")
          else:
            print("on_1n")

            input("Precione una tecla>>>  ")
        else:

          if on=="2":
            on_2 = input("Has pulsado la opcion 2...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

            if on_2=="2":
              print("on_2s")
              input("Precione una tecla>>>  ")
            else:
              print("on_2n")
              input("Precione una tecla>>>  ")

          else:

            if on=="3":
              on_3 = input("Has pulsado la opcion 3...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

              if on_3=="s":
                print("on_3s")
                input("Precione una tecla>>>  ")
              else:
                print("on_3n")
                input("Precione una tecla>>>  ")

            else:

              if on=="4":
                on_4 = input("Has pulsado la opcion 4...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

                if on_4=="s":
                  print("on_4s")
                  input("Precione una tecla>>>  ")
                else:
                  print("on_4n")
                  input("Precione una tecla>>>  ")

              else:

                if on=="5":
                  on_5 = input("Has pulsado la opcion 5...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

                  if on_5=="s":
                    print("on_5s")
                    input("Precione una tecla>>>  ")
                    break
                  else:
                    print("on_5n")
                    input("Precione una tecla>>>  ")

                else:
                  input("No has pulsado ninguna opcion correcta>>> ")
    else:
      print("endt_1n")
      input("Precione una tecla>>>  ")

  else:

    if endt=="2":
      endt_2 = input("Has pulsado la opcion 2...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

      if endt_2=="s":
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
        *****  Programas que se utilizan en la union  de tareas  *****
          __________________________________________________________""")

        def menu():
          print("\t1 - Share point")
          print("\t2 - Correo Electronico")
          print("----------------------------------------------------------")
          print("\t3 - Volver al menu de envio")
          print("\t4 - Volver al menu principal")
          print("\t5 - Salir")
          print("----------------------------------------------------------")
        while True:
          menu()
          on = input(" ¿Que proceso necesitas hacer ? >>>   ")

          if on=="1":
            on_1 = input("Has pulsado la opcion 1...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

            if on_1=="s":
              print("on_1s")
              input("Precione una tecla>>>  ")
            else:
              print("on_1n")

              input("Precione una tecla>>>  ")
          else:

            if on=="2":
              on_2 = input("Has pulsado la opcion 2...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

              if on_2=="2":
                print("on_2s")
                input("Precione una tecla>>>  ")
              else:
                print("on_2n")
                input("Precione una tecla>>>  ")

            else:

              if on=="3":
                on_3 = input("Has pulsado la opcion 3...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

                if on_3=="s":
                  print("on_3s")
                  input("Precione una tecla>>>  ")
                else:
                  print("on_3n")
                  input("Precione una tecla>>>  ")

              else:

                if on=="4":
                  on_4 = input("Has pulsado la opcion 4...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

                  if on_4=="s":
                    print("on_4s")
                    input("Precione una tecla>>>  ")
                  else:
                    print("on_4n")
                    input("Precione una tecla>>>  ")

                else:

                  if on=="5":
                    on_5 = input("Has pulsado la opcion 5...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

                    if on_5=="s":
                      print("on_5sñ")
                      input("Precione una tecla>>>  ")
                      break
                    else:
                      print("on_5n")
                      input("Precione una tecla>>>  ")

                  else:
                    input("No has pulsado ninguna opcion correcta>>> ")
      else:
        print("endt_2n")
        input("Precione una tecla>>>  ")

    else:

      if endt=="3":
        endt_3 = input("Has pulsado la opcion 3...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

        if endt_3=="s":
          print("endt_3s")
          input("Precione una tecla>>>  ")
        else:
          print("endt_3n")
          input("Precione una tecla>>>  ")

      else:

        if endt=="4":
          endt_4 = input("Has pulsado la opcion 4...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

          if endt_1=="s":
            print("endt_4s")
            input("Precione una tecla>>>  ")
            break
          else:
            print("endt_4n")
            input("Precione una tecla>>>  ")

        else:
          input("No has pulsado ninguna opcion correcta>>> ")