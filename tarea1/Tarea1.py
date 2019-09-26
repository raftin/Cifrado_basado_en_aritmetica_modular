import math
import os.path


# region Variables y constantes


Elementos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z', '.', ' ']

N = 29
Switch = False
SwitchNumeroCero = False


# endregion


# region Función


def f(Clave):
    Resultado = ""
    for i in Clave:
        Resultado = Resultado+"".join(str(Elementos.index(i)))

    x, y = GenerarXY((int(Resultado) % N))
    if x == 0:
        x = 2
    if y == 0:
        y = 2

    return x, y


def GenerarXY(z):
    w = int(math.floor((math.sqrt(8 * z + 1) - 1)/2))
    t = (w**2 + w) / 2
    y = int(z - t)
    x = int(w - y)
    return x, y


def Cifrar(Ruta, x, y):
    TextoCifrado = []
    Archivo = open(Ruta, "r")
    for linea in Archivo.readlines():
        for i in linea:
            NuevaPosicion = int(((Elementos.index(i) * x) + y) % N)
            TextoCifrado.append(Elementos[NuevaPosicion])
    Archivo.close()
    return MostrarResultado(TextoCifrado)


def Descifrar(Ruta, x, y):
    TextoDescifrado = []
    Archivo = open(Ruta, "r")
    Inverso = euclides_extendido(x, N)
    for linea in Archivo.readlines():
        for i in linea:
            PosicionOriginal = int(((Elementos.index(i) - y) % N) * (Inverso) % N)
            TextoDescifrado.append(Elementos[PosicionOriginal])
    Archivo.close()
    return MostrarResultado(TextoDescifrado)


def MostrarResultado(Texto):
    Resultado = ""
    for i in Texto:
        Resultado = Resultado + "".join(i)
    return Resultado


def ModificarArchivo(Texto, Ruta):
    Archivo = open(Ruta, "w")
    Archivo.write(Texto)
    Archivo.close()


def euclides_extendido(Numero1, Numero2):
    x = 1
    y = 0
    u = 0
    v = 1
    while Numero2 != 0:
        Cociente = Numero1 // Numero2
        Residuo = Numero1 % Numero2
        m = x - u * Cociente
        n = y - v * Cociente
        x = u
        y = v
        u = m
        v = n
        Numero1 = Numero2
        Numero2 = Residuo
    return x


def ValidarArchivo(Archivo):
    try:
        Archivo = open(Ruta, "r")
        for linea in Archivo.readlines():
            for i in linea:
                if i not in Elementos:  # No imprime nada
                    Archivo.close()
                    Mensaje = "El elemento: " + i + " del archihvo " + Ruta + " no se encuentra dentro de los valores aceptados, revise su archivo."
                    ##Mensaje = "No existe en la lista el elemento : " +i+ " revise su archivo."
                    return False, Mensaje
        Archivo.close()
        return True, ""
    except: return False, "Archihvo no encontrado"


def ValidarClave(Clave):
        for i in Clave:
            if i not in Elementos:  # No imprime nada
                return False, i
        return True, ""


# endregion


while not (Switch):
    try:

        Ruta = str(input("Ingrese nombre de archivo: \n"))
        Validacion_archivo, extension = os.path.splitext(Ruta)

        Clave = str(input("Ingrese clave: \n")).upper()


        if Ruta == "" or Clave == "" or extension != ".txt":
            if Ruta == "" or Clave == "":
                print("Debe ingresar ruta de archivo y clave. \n")
            else:
                 print("Ingrese archivos con extensión txt. \n")
            Switch = False

        else:

            SwitchValidar, errorArchivo = ValidarArchivo(Ruta)
            SwtichValidarClave, errorClave = ValidarClave(Clave)


            if not SwitchValidar:
                print(errorArchivo)
                Switch = False
            elif not SwtichValidarClave:
                print("El elemento : ",errorClave, " no se encuentra dentro de los valores aceptados, favor intente con otra clave.")
                Switch = False
            else:
                x, y = f(Clave)
                SwitchCifrado = False

                while not (SwitchCifrado):
                    try:
                        print("\n MENÚ \n")
                        print("1. CIFRAR.")
                        print("2. DESCIFRAR.")
                        print("3. INGRESAR NUEVO ARCHIVO.")
                        print("4. SALIR DEL SISTEMA.")

                        OpcionCifrarDescifrar = int(input("Seleccione una opción: \n"))

                        if OpcionCifrarDescifrar == 1:

                            ResultadoCifrado = Cifrar(Ruta, x, y)
                            print("Cifrado es :", ResultadoCifrado)
                            ModificarArchivo(ResultadoCifrado, Ruta)

                        elif OpcionCifrarDescifrar == 2:

                            ResultadoDescifrado = Descifrar(Ruta, x, y)
                            print("Descifrado es :", ResultadoDescifrado)
                            ModificarArchivo(ResultadoDescifrado, Ruta)

                        elif OpcionCifrarDescifrar == 3:

                            SwitchCifrado = True

                        elif OpcionCifrarDescifrar == 4:

                            SwitchCifrado = True
                            Switch = True

                        else:

                            print("Ingrese sólo opciones válidas  1; 2; 3; 4 \n")

                    except:
                        print("Ha ocurrido una excepción en el sistema, intente nuevamente.")
                        SwitchCifrado = False
    except:
        print("Ha ocurrido una excepción")
        break
##explicar la probabilidad de obtener un numero dentro del mod 29
## al decifrar un txt crear uno nuevo

