### 🔹 Programación Imperativa
# Basada en dar instrucciones paso a paso.
# El foco está en **cómo** se hace la tarea.
# Ejemplos: C, Pascal, Python (en estilo imperativo).

#Se centra en qué queremos lograr, no en los pasos.
#Ejemplo: SQL, HTML.


# Calcular la suma de una lista (imperativo)
numeros = [1, 2, 3, 4]
suma = 0
for n in numeros:
    suma += n
print(suma)

### 🔹 Programación Declarativa
# Se centra en QUÉ queremos lograr, no en los pasos.
# Ejemplos: SQL, HTML, CSS
# En Python, equivalente declarativo simple:
numeros = [1, 2, 3, 4]
suma_declarativa = sum(numeros)  # Declaramos QUÉ queremos: la suma
print(f"Suma declarativa: {suma_declarativa}")

### 🔹 Programación Funcional
# Basada en funciones puras y evitar estados mutables.
# Ventajas: código más predecible y fácil de testear.
# Ejemplos: Haskell, Scala, Python (funcional).

# Calcular suma (funcional)
numeros = [1, 2, 3, 4]
print(sum(numeros))

### 🔹 Programación Orientada a Objetos
# Organiza el código en objetos que representan entidades del mundo real.
# Cada objeto tiene:
# - Atributos (estado).
# - Métodos (comportamiento).
# Ejemplos: Java, C#, Python, C++.

# Definición de una clase
class Coche:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def arrancar(self):
        print(f"El {self.marca} arranca!")

mi_coche = Coche("Toyota", "Rojo")
mi_coche.arrancar()

###Clases y objetos en Python
# Definición de una clase
class Coche:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def arrancar(self):
        print(f"El {self.marca} arranca!") 
        
# Crear objetos
coche1 = Coche("Toyota", "Rojo")
coche2 = Coche("Ford", "Azul")

# Llamar a los métodos
coche1.arrancar()
coche2.arrancar()

###Atributos y métodos
# Atributos: variables dentro de la clase (estado del objeto).
# Métodos: funciones dentro de la clase (comportamiento del objeto).

###Encapsulamiento
# El encapsulamiento consiste en ocultar detalles internos de una clase y exponer solo lo necesario.
# En Python no existe private como en Java, pero se simula con _ y __.

#creamos la clase CuentaBancaria
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo   # atributo "privado"

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def mostrar_saldo(self):
        return f"Saldo de {self.titular}: {self.__saldo}€"

cuenta = CuentaBancaria("Ana", 1000)
#error
#print(cuenta.__saldo)
#print(cuenta._CuentaBancaria__saldo)
print(cuenta.titular)
cuenta.depositar(500)
print(cuenta.mostrar_saldo())

### 🔹 GETTERS Y SETTERS 
# Método 1: Funciones get/set tradicionales
class CuentaConGetSet:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo   # privado
    
    # GETTER - para obtener el valor
    def get_saldo(self):
        return self.__saldo
    
    # SETTER - para establecer el valor (con validación)
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            print("❌ El saldo no puede ser negativo")
    
    def depositar(self, cantidad):
        self.__saldo += cantidad

# Método 2: Usando @property (más pythónico)
class CuentaConProperty:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo   # privado
    
    @property
    def saldo(self):  # GETTER - se usa como: cuenta.saldo
        return self.__saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):  # SETTER - se usa como: cuenta.saldo = 1000
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            print("❌ El saldo no puede ser negativo")
    
    def depositar(self, cantidad):
        self.__saldo += cantidad

print("\n=== EJEMPLO CON GET/SET TRADICIONAL ===")
cuenta1 = CuentaConGetSet("María", 500)
print(f"Saldo inicial: {cuenta1.get_saldo()}")
cuenta1.set_saldo(1000)  # Usar setter
print(f"Saldo después del setter: {cuenta1.get_saldo()}")
cuenta1.set_saldo(-100)  # Validación

print("\n=== EJEMPLO CON @PROPERTY (más pythónico) ===")
cuenta2 = CuentaConProperty("Juan", 800)
print(f"Saldo inicial: {cuenta2.saldo}")  # Como si fuera público
cuenta2.saldo = 1200  # Como si fuera público, pero usa el setter
print(f"Saldo después de modificar: {cuenta2.saldo}")
cuenta2.saldo = -50  # Validación automática

###Resumen del Módulo 1

#La POO organiza el código en objetos con atributos y métodos.
#Existen varios paradigmas: imperativo, declarativo, funcional y orientado a objetos.
#Python permite aplicar POO de manera sencilla.
#Conceptos básicos: clases, objetos, atributos, métodos, encapsulamiento.