## 🔹 ABSTRACCIÓN - "Ocultar la complejidad"
# La abstracción consiste en:
# 1. Ocultar detalles internos complejos
# 2. Mostrar solo lo esencial al usuario
# 3. Definir "contratos" que las clases deben cumplir

from abc import ABC, abstractmethod
import math

# 🔸 CLASE ABSTRACTA - No se puede instanciar directamente
class Figura(ABC):
    """Clase abstracta que define el 'contrato' para todas las figuras"""
    
    @abstractmethod
    def area(self):
        """Método abstracto: OBLIGATORIO implementar en clases hijas"""
        pass
    
    @abstractmethod
    def perimetro(self):
        """Método abstracto: OBLIGATORIO implementar en clases hijas"""
        pass
    
    # Método concreto (opcional, pero útil)
    def mostrar_info(self):
        """Método concreto: ya implementado, disponible para todas las figuras"""
        print(f"Área: {self.area()}")
        print(f"Perímetro: {self.perimetro()}")
        print()

# 🔸 IMPLEMENTACIONES CONCRETAS
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio

class Triangulo(Figura):
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

print("=== USANDO ABSTRACCIÓN ===")

# ❌ Esto daría ERROR - No puedes instanciar una clase abstracta
# figura = Figura()  # TypeError: Can't instantiate abstract class

# ✅ Esto SÍ funciona - Instanciar clases concretas
rectangulo = Rectangulo(4, 5)
circulo = Circulo(3)
triangulo = Triangulo(6, 4, 5, 5, 6)

print("Rectángulo 4x5:")
rectangulo.mostrar_info()

print("Círculo radio 3:")
circulo.mostrar_info()

print("Triángulo base 6, altura 4:")
triangulo.mostrar_info()

# 🔸 POLIMORFISMO + ABSTRACCIÓN
print("=== POLIMORFISMO CON ABSTRACCIÓN ===")
figuras = [rectangulo, circulo, triangulo]

for i, figura in enumerate(figuras, 1):
    print(f"Figura {i}:")
    figura.mostrar_info()  # ¡Mismo método, diferentes implementaciones!

# 🔸 EJEMPLO PRÁCTICO: Sistema de vehículos
print("=== EJEMPLO PRÁCTICO: VEHÍCULOS ===")

class Vehiculo(ABC):
    """Clase abstracta para todos los vehículos"""
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    @abstractmethod
    def acelerar(self):
        pass
    
    @abstractmethod
    def frenar(self):
        pass
    
    @abstractmethod
    def obtener_velocidad_maxima(self):
        pass
    
    # Método concreto compartido
    def mostrar_info(self):
        print(f"{self.marca} {self.modelo}")
        print(f"Velocidad máxima: {self.obtener_velocidad_maxima()} km/h")
        self.acelerar()
        self.frenar()
        print()

class Coche(Vehiculo):
    def acelerar(self):
        print("🚗 Acelerando con motor de gasolina")
    
    def frenar(self):
        print("🛑 Frenando con frenos de disco")
    
    def obtener_velocidad_maxima(self):
        return 180

class Bicicleta(Vehiculo):
    def acelerar(self):
        print("🚴 Pedaleando más fuerte")
    
    def frenar(self):
        print("🛑 Frenando con frenos de mano")
    
    def obtener_velocidad_maxima(self):
        return 40

class Avion(Vehiculo):
    def acelerar(self):
        print("✈️ Aumentando potencia de turbinas")
    
    def frenar(self):
        print("🛑 Activando reversa de motores")
    
    def obtener_velocidad_maxima(self):
        return 900

# Usar los vehículos
coche = Coche("Toyota", "Corolla")
bici = Bicicleta("Trek", "Mountain")
avion = Avion("Boeing", "747")

vehiculos = [coche, bici, avion]

for vehiculo in vehiculos:
    vehiculo.mostrar_info()

print("=== VENTAJAS DE LA ABSTRACCIÓN ===")
print("✅ Garantiza que las clases hijas implementen métodos obligatorios")
print("✅ Define un 'contrato' claro para todas las implementaciones")
print("✅ Permite polimorfismo seguro")
print("✅ Facilita el mantenimiento y extensión del código")
print("✅ Separa el QUÉ (interfaz) del CÓMO (implementación)")
