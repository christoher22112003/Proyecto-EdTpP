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
    else:
      print("on_1n")

  else:

    if on=="2":
      on_2 = input("Has pulsado la opcion 2...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

      if on_2=="2":
        print("on_2s")
      else:
        print("on_2n")

    else:

      if on=="3":
        on_3 = input("Has pulsado la opcion 3...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

        if on_3=="s":
          print("on_3s")
        else:
          print("on_3n")

      else:

        if on=="4":
          on_4 = input("Has pulsado la opcion 4...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

          if on_4=="s":
            print("on_4s")
          else:
            print("on_4n")

        else:

          if on=="5":
            on_5 = input("Has pulsado la opcion 5...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

            if on_5=="s":
              print("on_5sñ")
              exit()
            else:
              print("on_5n")

          else:
            input("No has pulsado ninguna opcion correcta>>> ")