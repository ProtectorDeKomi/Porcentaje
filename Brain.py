def brain(input,var):
    print(f"Resultado : {(input * var) / 100}")
def help():
    print("""
    Ejemplo De Uso
    
    Introduce La Cantidad Base : 4567

    Introduce Porcentaje Que Deseas Obtener : 23

    Resultado : 1050.41
     
    """)

if __name__ == "__main__":
    val = input("""
    Calculadora De Porcentaje 

    1)Obtener Valor
    2)Ayuda
    3)Salir
    Selecciona Una Opcion : """)

    if val == '1':
        var = input("Introduce La Cantidad Base : ")
        input = input("Introduce Porcentaje Que Deseas Obtener : ")
        brain(int(input),int(var))
    elif val == '2':
        help()
    elif val == '3':
        exit()
