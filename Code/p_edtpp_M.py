from ast import While
import os
import webbrowser as wb

print("""

                          =                          
                          %                          
                          %                          
                       .*++++.                       
                       -#=++#:                       
                       #.   :*                       
                       *----=*                       
                       .*::-+:                       
                       :*++++:                       
                       -*: :*-                       
                       ==+++==                       
                       =*: -*-                       
                       *:=+=:+                       
                       *=: :*+                       
                       #.=++.#                       
                       #=   =*                       
                       #.=++.#                       
                      .#-. .-#                       
                      :+--.--*.                      
                      -=-=--:+:                      
                      =+.   .*-                      
                      *:-----:*                      
                      #.--:--.#                      
                      #-     -#.                     
                     :+---.---=-                     
                     -= .===. :+                     
                     *=-:   :--#                     
                  .+=#=*+*+*+*+%=*.                  
                  .#+%+%+%+%+%+%+*.                  
                   +*+*=#=#=#=#+*-                   
                   ++=+*+:--=%==+=                   
                  .#--===    #==-#:                  
                  +==-**.    ++=-*+                  
                 :*-=+.*     =-++:+-                 
                 *==-=#-     :#=:-*#                 
                -=-++-+.      *:-=--=                
             ...%+-.-=#.......*--:-=%:..             
             %=#=#=#=#-*=#=#=#=#=#=#=#=#.            
            -%*%*###+%##+%***%*##%*##%*#-            
             *-*- *+:.#= =+- *+.:*= ++:+             
             #-=++-=+==-+--=+=-=+=-++=-#.            
           .*:++..++.--=.-=- :+-.+=..-=:*.           
          .#-====+-===-===-+:+-*==+:-+==-#.          
         :*+*=+**+*-=-=+==+=-:-=-=#+**==*=+.         
        -*----=: -:.======-===++=::= :===-:#.        
       :#+----=##=+-.           .-+*#+----=#+:       
      :* .==--:==.                 .+=:-:==. *:      
     :*---:.--+-                     -+--.--::#:     
    :#*----=**-                       =*+=----#+:    
   :+  -++=: #                         # .-=++. *:   
  :*---:  --:#                         #:--: :---*:  
  %---------=#                         #---------+*  
  *===++++++++                         ++==+++++++*  

    #######  ##   ##  ##   ##   ####     #####
    ##   #   ###  ##  ##   ##    ##     ##   ##
    ## #     #### ##   ## ##     ##     ##   ##
    ####     ## ####   ## ##     ##     ##   ##
    ## #     ##  ###    ###      ##     ##   ##
    ##   #   ##   ##    ###      ##     ##   ##
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

def menu():
  print("""
  *************************************************
*****  Bienvenido al script de envio de tareas  *****
  _________________________________________________""")
  print("Procesos que se utilizan para el envio de tareas")
  print("\t1 - Escaneo de tareas")
  print("\t2 - Unir las tareas")
  print("\t3 - Envio de tareas")
  print("\t4 - Realizar todo el proceso")
  print("\t5 - Salir")
while True:
  menu()

  edt = input(" ¿ Que proceso necesita hacer ? >>>   ")

  if edt=="1":
    edt_1 = input("Has pulsado la opcion 1 (Escaneo de tareas)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

    if edt_1=="s":
      print("Se abrirar el menu de Escaneo de tareas")
      wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Code escaneo de tareas\edt.py')
      exit()
    else:
      print("Se regresara al menu de Envio de tareas principal")

  else:

    if edt=="2":
      edt_2 = input("Has pulsado la opcion 2 (Unir las tareas)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

      if edt_2=="s":
        print("Se abrirar el menu de Unir las tareas")
        wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Code union de tareas\udt.py')
        exit()
      else:
        print("Se regresara al menu de Envio de tareas principal")

    else:

      if edt=="3":
        edt_3 = input("Has pulsado la opcion 3(Envio de tareas)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

        if edt_3=="s":
          print("Se abrirar el menu de Envio de tareas")
          wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Code envio de tareas\endt.py')
          exit()
        else:
          print("Se regresara al menu de Envio de tareas principal")

      else:

        if edt=="4":
          edt_4 = input("Has pulsado la opcion 4(Realizar todo el proceso de envio de tareas)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

          if edt_4=="s":
            print("Se abrirar el menu de Realizar todo el proceso de envio de tareas")
            wb.open_new(r'M:\Documents\Pasatiempos\Programacion\Proyecto-EdTpP\Code\Code todo el proceso de envio de tareas\tepdedt.py')
            exit()
          else:
            print("Se regresara al menu de Envio de tareas principal")

        else:

          if edt=="5":
            edt_5 = input("Has pulsado la opcion 5 (Salir)...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")

            if edt_5=="s":
              print("Se cerrar el menu de Envio de tareas")
              exit()
            else:
              print("Se regresara al menu de Envio de tareas principal")

          else:
            input("No has pulsado ninguna opcion correcta>>> ")