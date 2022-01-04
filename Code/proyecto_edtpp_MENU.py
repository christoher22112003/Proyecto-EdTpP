from ast import While
import os

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
  *************************************************
*****  Bienvenido al script de envio de tareas  *****
  _________________________________________________
""")

def menu():
  print("Procesos que se utilizan para el envio de tareas")
  print("\t1 - Escaneo de tareas")
  print("\t2 - Unir los archivos escaneados")
  print("\t3 - Envio de tareas")
  print("\t4 - Realizar todo el proceso")
  print("\t5 - Salir")
while True:
  menu()
  rm1 = input(" ¿ Que proceso necesita hacer ? >>>   ")
  if rm1=="1":
    print(" ")
    rm1_1 = input("Has pulsado la opcion 1...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")
    if rm1_1=="s":
      print("rm1_1s")
      input("Precione una tecla")
    else:
      print("rm1_1n")
      input("Precione una tecla")
  else:
    if rm1=="2":
      print("")
      rm1_2 = input("Has pulsado la opcion 2...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")
      if rm1_2=="s":
        print("rm1_2s")
        input("Precione una tecla>>>  ")
      else:
        print("rm1_2n")
        input("Precione una tecla>>>  ")
    else:
      if rm1=="3":
        print("")
        rm1_3 = input("Has pulsado la opcion 3...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")
        if rm1_3=="s":
          print("rm1_3s")
          input("Precione una tecla>>>  ")
        else:
          print("rm1_3n")
          input("Precione una tecla>>>  ")
      else:
        if rm1=="4":
          print("")
          rm1_4 = input("Has pulsado la opcion 4...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")
          if rm1_4=="s":
            print("rm1_4s")
            input("Precione una tecla>>>  ")
          else:
            print("rm1_4n")
            input("Precione una tecla>>>  ")
        else:
          if rm1=="2":
            print("")
            rm1_5 = input("Has pulsado la opcion 5...  \nPreciona <S> si deseas continuar o <N> si deseas seleccionar de nuevo el proceso a realizar>>>  ")
            if rm1_5=="s":
              print("rm1_5s")
              input("Precione una tecla>>>  ")
              break
            else:
              print("rm1_5n")
              input("Precione una tecla>>>  ")
          else:
            print(" ")
            input("No has pulsado ninguna opcion correcta>>> ")