import os
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls')
	
	print ("Procesos que se utilizan para el envio de tareas")
	print ("\t1 - Escaneo de tareas")
	print ("\t2 - segunda opción")
	print ("\t3 - tercera opción")
	print ("\t4 - tercera opción")
	print ("\t4 - tercera opción")
	print ("\t5 - salir")
while True:

	menu()
	opcionMenu = input(" ¿ Que necesita hacer ? >> ")
	if opcionMenu=="1":
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la pción 2...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")