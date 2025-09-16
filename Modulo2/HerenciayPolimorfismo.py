##Herencia
#La herencia permite que una clase hija herede atributos y métodos de una clase padre.
#Ejemplo:
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        return "Hace un sonido"

class Perro(Animal):
    def hablar(self):
        return "Guau!"
    
class Gato(Animal):
    def hablar(self):
        return "Miau!"
    
animales = [Perro("Firulais"), Gato("Michi")]
for a in animales:
    print(f"{a.nombre}: {a.hablar()}")

## 🔹 POLIMORFISMO - "Muchas formas"
# El polimorfismo permite que el MISMO método tenga DIFERENTES comportamientos 
# según el tipo de objeto que lo ejecute.

print("\n=== POLIMORFISMO BÁSICO ===")
def hacer_hablar(animal):
    print(f"{animal.nombre} dice: {animal.hablar()}")

hacer_hablar(Perro("Rocky"))  # Rocky dice: Guau!
hacer_hablar(Gato("Luna"))    # Luna dice: Miau!

# 🔸 Ejemplo más avanzado: Diferentes tipos de vehículos
print("\n=== POLIMORFISMO CON VEHÍCULOS ===")
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
    
    def acelerar(self):
        return "El vehículo acelera"
    
    def frenar(self):
        return "El vehículo frena"

class Coche(Vehiculo):
    def acelerar(self):
        return f"El coche {self.marca} acelera con motor de gasolina 🚗"
    
    def frenar(self):
        return f"El coche {self.marca} frena con frenos de disco"

class Bicicleta(Vehiculo):
    def acelerar(self):
        return f"La bicicleta {self.marca} acelera pedaleando 🚴"
    
    def frenar(self):
        return f"La bicicleta {self.marca} frena con frenos de mano"

class Avion(Vehiculo):
    def acelerar(self):
        return f"El avión {self.marca} acelera con turbinas ✈️"
    
    def frenar(self):
        return f"El avión {self.marca} frena con reversa de motores"

# 🔸 POLIMORFISMO EN ACCIÓN: Misma función, diferentes comportamientos
def probar_vehiculo(vehiculo):
    print(f"--- Probando {vehiculo.marca} ---")
    print(vehiculo.acelerar())
    print(vehiculo.frenar())
    print()

# Creamos diferentes vehículos
vehiculos = [
    Coche("Toyota"),
    Bicicleta("Trek"), 
    Avion("Boeing")
]

# ¡POLIMORFISMO! La misma función funciona con diferentes tipos
for vehiculo in vehiculos:
    probar_vehiculo(vehiculo)

print("=== VENTAJAS DEL POLIMORFISMO ===")
print("✅ Mismo código funciona con diferentes tipos")
print("✅ Fácil agregar nuevos tipos sin cambiar código existente")
print("✅ Código más flexible y mantenible")
print("✅ Principio: 'Programar contra interfaces, no implementaciones'")

# 🔸 Ejemplo práctico: Sistema de formas geométricas
print("\n=== POLIMORFISMO CON FORMAS GEOMÉTRICAS ===")
import math

class Forma:
    def area(self):
        pass
    
    def perimetro(self):
        pass

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio

class Triangulo(Forma):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# Función polimórfica que funciona con cualquier forma
def calcular_propiedades(forma, nombre):
    print(f"{nombre}:")
    print(f"  Área: {forma.area():.2f}")
    print(f"  Perímetro: {forma.perimetro():.2f}")
    print()

# Creamos diferentes formas
formas = [
    (Rectangulo(5, 3), "Rectángulo 5x3"),
    (Circulo(4), "Círculo radio 4"),
    (Triangulo(6, 4, 5, 5, 6), "Triángulo")
]

# ¡POLIMORFISMO! Misma función, diferentes cálculos
for forma, nombre in formas:
    calcular_propiedades(forma, nombre)
