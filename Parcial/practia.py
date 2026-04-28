cartelera = ["Avengers", "Mario Bros", "Avatar"]
precios = {"Avengers": 18000, "Mario Bros": 15000, "Avatar": 22000}

def compra_boletas():
    try:
        print("Películas hoy:", cartelera)
        eleccion = input("¿Qué película desea ver? escribala tal cual aparece en cartelera: ")

        if eleccion in precios:
            cantidad = int(input("Escriba la cantidad de boletas "))
            
            precio_por_boleta = precios[eleccion]
            total= precio_por_boleta*cantidad
            resumen = (eleccion, 1, total)
            
            print(f"Pelicula: {resumen[0]}")
            print(f"Total a pagar: {resumen[2]}")
        else:
            print("Esa película no existe en nuestra cartelera.")
            
    except ValueError:
        print("Error: Hubo un problema con el valor ingresado.")

compra_boletas()
