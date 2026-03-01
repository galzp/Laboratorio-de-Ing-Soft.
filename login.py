programa_activo = True
while programa_activo:
    intentos = 0
    
    while intentos < 3:
        usuario = input("Usuario: ")
        clave = input("Contraseña: ")

        if usuario == "":
            print("Error: Usuario vacío.")
        elif " " in usuario:
            print("Error: El usuario no puede tener espacios.")
        elif len(clave) < 8:
            print("Error: La contraseña es muy corta (mínimo 8).")
        else:
            if usuario == "admin" and clave == "Admin2026":
                print("¡Acceso concedido!")
               
                sesion_activa = True
                while sesion_activa:
                    print("1. Clasificar numero")
                    print("2. Categoria de edad y permisos")
                    print("3. Calcular tarifa final")
                    print("4. Cerrar sesion")
                    print("5. Salir")

                    opcion = input("Selecciona una opcion: ")
                    if opcion == "1":
                        print("Opcion 1 seleccionada")
                        if opcion == "1":
                            print("Ingresa el numero a clasificar")
                            numero = int(input())
                            if numero > 0:
                                print("El numero es positivo")
                            elif numero < 0:
                                print("El numero es negativo")
                            else: 
                                print("El numero es cero")
                            if numero != 0:    
                              if numero % 2 == 0:
                                print("El numero es par")
                            else:
                                print("El numero es impar")
                    elif opcion == "2":
                        print("Opcion 2 seleccionada")
                        print("Ingresa tu edad")
                        edad = int(input())
                        identificacion = input("¿Tienes identificacion? (S/N): ")
                        licencia = input("Tienes licencia de conducir? (S/N): ")
                        while edad == 0-12 == "Niño (no puede votar ni conducir)"
                         if edad == 13-17 == "Adolescente (puede votar pero no conducir)"
                        18-64 == "Adulto (puede votar y conducir)"
                        65-120 == "Adulto mayor (puede votar pero no conducir)"
                        if edad < 0 or edad > 120:
                            print("Edad invalida")
                        elif edad < 18:
                            print("Eres menor de edad y no puedes votar ni conducir")
                        elif edad < 65:
                            print("Eres adulto y puedes votar y conducir")
                        else:
                            print("Eres adulto mayor y puedes votar pero no puedes conducir")
                    if edad >= 13:
                        print("Puede registrarse")
                    elif opcion == "3":
                        print("Opcion 3 seleccionada")
                    elif opcion == "4":
                        print("Cerro sesion correctamente")
                        sesion_activa = False
                    elif opcion == "5":
                        print("Salio del programa")
                        programa_activo = False
                        sesion_activa = False
                    else:
                        print("Opcion invalida")
                break
            else:
                intentos += 1
                print("Datos incorrectos.")
                print("Te quedan", 3 - intentos, "intentos.")
    if intentos == 3:
        print("SISTEMA BLOQUEADO")
        programa_activo = False
