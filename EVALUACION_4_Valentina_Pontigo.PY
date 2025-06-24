#Crear un programa que permita generar un menú de gestión de entradas para el Concierto de Trap con el “Conejo Simpático” Concierto de Trap con el “Conejo Simpático”

# Opciones del menu principal: 
#("/n***MENU PRINCIPAL***")
#("1.- Comprar entrada.")
#("2.- Consultar comprador.")
#("3.- Cancelar compra.")
#("4.- Salir."") 


print("-"*100)
print("Bienvenido a el menú de gestión de entradas para el Concierto de Trap con el 'Conejo Simpá-tico' ")
print("-"*100)


compradores = {}

def validar_codigo(codigo):
    Tiene_letra = False
    Tiene_Numero = False

    if " " in codigo or len(codigo) < 6:
        return False
    
    for caracter in codigo:
        if caracter.isalpha():
            Tiene_letra = True
        elif caracter.isdigit():
            Tiene_Numero = True
    return Tiene_letra and Tiene_Numero

def comprar_entrada():
    while True:
        nombre = input("Ingrese el nombre del comprador: ").lower()

        if nombre in compradores:
            print("Este comprador ya tiene una entrada comprada")
            return
        
        tipo=input("Ingrese el tipo de entrada (G/V): ").upper()
        if tipo not in ["G", "V"]:
            print("Debe de ingresar solo G o V, vuelva a intentarlo")
            continue
        break

    while True:
        codigo = input("Ingrese código de confirmación: ")
        if validar_codigo(codigo):
            print("Código validado. ¡Entrada registrada con éxito!")
            
            compradores[nombre] = [tipo, codigo]
            return
        else:
            print("Código no válido. Intente otra vez.")

def consultar_comprador():
    nombre = input("Ingrese nombre de comprador a buscar: ").lower()
    if nombre in compradores:
        print("Tipo de entrada:", compradores[nombre][0])
        print("Codigo:", compradores[nombre][1])
    else:
        print("El comprador no se encuentra.")


def cancelar_compra():
    nombre = input("Ingrese nombre de comprador a cancelar: ").lower()
    if nombre in compradores:
        del compradores[nombre]
        print("¡Compra cancelada!")
    else:
        print("No se pudo cancelar la entrada")

def main():
    while True:
        print("\n***MENU PRINCIPAL***")
        print("1.- Comprar entrada.")
        print("2.- Consultar comprador.")
        print("3.- Cancelar compra.")
        print("4.- Salir.")

        opcion=input("Ingrese una opcion: ")
        
        match opcion:

            case "1":
                comprar_entrada()
            case "2":
                consultar_comprador()
            case "3":
                cancelar_compra()
            case "4":
                print("Programa terminado...")
                break
            case default:
                print("Debe de selecionar una opcion valida (1/4).")

main()








        
    








        

        





