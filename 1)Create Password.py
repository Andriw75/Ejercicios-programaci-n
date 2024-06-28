"""
Reto semanal #1

Descripción:
Crear un generador de contraseñas seguras que permita al usuario especificar la longitud de la contraseña y opcionalmente incluir caracteres especiales, números, letras mayúsculas y minúsculas.

Requisitos:
- Solicitar la longitud de la contraseña al usuario.
- Permitir al usuario elegir si desea incluir caracteres especiales, números, letras mayúsculas y minúsculas.
- Generar la contraseña basada en las opciones seleccionadas.
- Mostrar la contraseña generada al usuario.

En este caso utilizare python
"""
import random as r

def select_option(men:str,allowed:list=['s','n']) -> str:
    """Solamente permitiremos caracteres que esten en una lista

    Args:
        men (str): Mensaje a mostrar
        allowed (list, optional): Caracteres permitidos. Por defecto es ['s','n'].

    Returns:
        str: Caracter dentro de la lista seleccionada
    """
    while True:
        opcion = input(men).lower()
        if opcion in allowed:
            return opcion == 's' #Lo retornaremos de esta forma para que sea un boleano y validarlo de mejor manera
        else:
            print(f"Por favor, ingrese alguno de los caracteres correspondientes: {allowed} .")

def select_number(n:int=0)->int:
    """Funcion para seleccionar un numero mayor a otro.

    Args:
        n (int): Numero al cual debe ser mayor, por defecto 0.

    Returns:
        int: numero seleccionado
    """
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña: "))
            if longitud > n:
                return longitud
            else:
                print("La longitud debe ser un número positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


class Create_Password:
    
    def __init__(self, long:int, in_mayus:str, in_minus:str, in_number:str, in_especial:str):
        """Inicializamos la clase con los requisitos a tener en cuenta para crear el password

        Args:
            long (int): Longitud del password.
            in_mayus (str): Si debemos incluir mayusculas
            in_minus (str): Si debemos incluir minusculas
            in_number (str): Si debemos incluir digitos
            in_especial (str): Si queremos caracteres especiales
        """
        self.long = long
        self.in_mayus = in_mayus
        self.in_minus = in_minus
        self.in_number = in_number
        self.in_especial = in_especial

    def generar(self):
        """
        A base de los datos brindados crearemos una sola cadena de texto con todos los caracteres disponibles,
        posteriormente utilizando choice del modulo random seleccionaremos un caracter de esta cadena 
        """
        caracteres = ''
        if self.in_mayus:
            caracteres += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if self.in_minus:
            caracteres += 'abcdefghijklmnopqrstuvwxyz'
        if self.in_number:
            caracteres += '0123456789'
        if self.in_especial:
            #Utilizamos r al inicio del string para que tome literal todos los caracteres
            caracteres += r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""" 
        
        # En caso de no seleccionar alguna opcion no retornaremos nada junto a un mensaje vacio
        if not caracteres:
            print("No se ha selecionado alguna opcion.")
            return ''
        
        password = ''.join(r.choice(caracteres) for _ in range(self.long))
        return password

if __name__ == "__main__":
    print("Genera tu password totalemente segura:\n")
    long = select_number()

    in_mayus = select_option("¿Incluir mayusculas? (s/n): ")
    in_minus = select_option("¿Incluir minusculas? (s/n): ")
    in_number = select_option("¿Incluir numeros? (s/n): ")
    in_especial = select_option("¿Incluir caracteres especiales? (s/n): ")
    
    generador = Create_Password(long, in_mayus, in_minus, in_number, in_especial)
    password = generador.generar()
    
    print("Tu password es:", password)
