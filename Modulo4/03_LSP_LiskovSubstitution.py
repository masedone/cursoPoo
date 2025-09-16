## 🔹 PRINCIPIO SOLID 3: LISKOV SUBSTITUTION PRINCIPLE (LSP)
# "Una subclase debe poder sustituir a su superclase sin alterar el comportamiento esperado"

print("=== PRINCIPIO LSP - SUSTITUCIÓN DE LISKOV ===\n")

# ❌ VIOLACIÓN DE LSP - Subclase que no puede sustituir a la superclase
print("❌ VIOLACIÓN DE LSP - Subclase incompatible:")

class Ave:
    """Clase base que define el comportamiento común de las aves"""
    
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
    
    def volar(self):
        return f"{self.nombre} está volando"
    
    def comer(self):
        return f"{self.nombre} está comiendo"
    
    def hacer_sonido(self):
        return f"{self.nombre} hace un sonido"

class Aguila(Ave):
    def volar(self):
        return f"🦅 {self.nombre} vuela alto en las montañas"
    
    def hacer_sonido(self):
        return f"🦅 {self.nombre} grita: ¡SCREECH!"

class Paloma(Ave):
    def volar(self):
        return f"🕊️ {self.nombre} vuela suavemente por la ciudad"
    
    def hacer_sonido(self):
        return f"🕊️ {self.nombre} arrulla: coo-coo"

class Pinguino(Ave):
    """VIOLA LSP: No puede volar pero hereda de Ave que sí puede"""
    
    def volar(self):
        # ❌ PROBLEMA: Lanza excepción en lugar de comportarse como Ave
        raise Exception("¡Los pingüinos no pueden volar!")
    
    def hacer_sonido(self):
        return f"🐧 {self.nombre} hace: ¡HONK HONK!"
    
    def nadar(self):
        return f"🐧 {self.nombre} nada graciosamente"

def hacer_volar_aves(aves):
    """Función que espera que todas las aves puedan volar"""
    print("🔄 Haciendo volar a todas las aves:")
    for ave in aves:
        try:
            print(f"   {ave.volar()}")
        except Exception as e:
            print(f"   ❌ Error con {ave.nombre}: {e}")

# Uso problemático que viola LSP
print("Usando jerarquía que viola LSP:")
aves_problemáticas = [
    Aguila("Águila Real", "Aquila chrysaetos"),
    Paloma("Paloma Común", "Columba livia"),
    Pinguino("Pingüino Emperador", "Aptenodytes forsteri")  # ¡Problema!
]

hacer_volar_aves(aves_problemáticas)

print("\n" + "="*70 + "\n")

# ✅ APLICANDO LSP - Jerarquía correcta que permite sustitución
print("✅ APLICANDO LSP - Jerarquía correcta:")

from abc import ABC, abstractmethod

class Animal(ABC):
    """Clase base más general para todos los animales"""
    
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
    
    @abstractmethod
    def moverse(self):
        """Todos los animales se mueven de alguna forma"""
        pass
    
    def comer(self):
        return f"{self.nombre} está comiendo"
    
    def hacer_sonido(self):
        return f"{self.nombre} hace un sonido"
    
    def dormir(self):
        return f"{self.nombre} está durmiendo"

class AveVoladora(Animal):
    """Clase específica para aves que SÍ pueden volar"""
    
    def moverse(self):
        return self.volar()
    
    def volar(self):
        return f"🕊️ {self.nombre} está volando"
    
    def aterrizar(self):
        return f"🕊️ {self.nombre} ha aterrizado"
    
    def construir_nido(self):
        return f"🪺 {self.nombre} está construyendo un nido"

class AveNoVoladora(Animal):
    """Clase específica para aves que NO pueden volar"""
    
    def moverse(self):
        return self.caminar()
    
    def caminar(self):
        return f"🚶 {self.nombre} está caminando"
    
    def correr(self):
        return f"🏃 {self.nombre} está corriendo"

class AveAcuatica(AveNoVoladora):
    """Clase para aves acuáticas que nadan"""
    
    def moverse(self):
        return self.nadar()
    
    def nadar(self):
        return f"🏊 {self.nombre} está nadando"
    
    def bucear(self):
        return f"🤿 {self.nombre} está buceando"

# Implementaciones específicas que CUMPLEN LSP
class AguilaReal(AveVoladora):
    def volar(self):
        return f"🦅 {self.nombre} vuela majestuosamente a gran altura"
    
    def hacer_sonido(self):
        return f"🦅 {self.nombre}: ¡SCREECH!"
    
    def cazar(self):
        return f"🦅 {self.nombre} está cazando desde las alturas"

class PalomaComun(AveVoladora):
    def volar(self):
        return f"🕊️ {self.nombre} vuela suavemente entre los edificios"
    
    def hacer_sonido(self):
        return f"🕊️ {self.nombre}: coo-coo"

class PinguinoEmperador(AveAcuatica):
    """Ahora SÍ cumple LSP - puede sustituir a AveAcuatica"""
    
    def nadar(self):
        return f"🐧 {self.nombre} nada elegantemente bajo el agua"
    
    def hacer_sonido(self):
        return f"🐧 {self.nombre}: ¡HONK HONK!"
    
    def deslizarse_sobre_hielo(self):
        return f"🐧 {self.nombre} se desliza sobre el hielo"

class Avestruz(AveNoVoladora):
    def correr(self):
        return f"🦓 {self.nombre} corre a 70 km/h"
    
    def hacer_sonido(self):
        return f"🦓 {self.nombre}: ¡BOOM BOOM!"

# Funciones que trabajan con las clases base - CUMPLEN LSP
def hacer_mover_animales(animales):
    """Función que funciona con cualquier Animal"""
    print("🔄 Haciendo mover a todos los animales:")
    for animal in animales:
        print(f"   {animal.moverse()}")

def hacer_volar_aves_voladoras(aves_voladoras):
    """Función específica para aves voladoras"""
    print("🔄 Haciendo volar a las aves voladoras:")
    for ave in aves_voladoras:
        print(f"   {ave.volar()}")
        print(f"   {ave.aterrizar()}")

def hacer_nadar_aves_acuaticas(aves_acuaticas):
    """Función específica para aves acuáticas"""
    print("🔄 Haciendo nadar a las aves acuáticas:")
    for ave in aves_acuaticas:
        print(f"   {ave.nadar()}")

# Uso correcto que CUMPLE LSP
print("Usando jerarquía que cumple LSP:")

# Crear diferentes tipos de aves
aguila = AguilaReal("Águila Dorada", "Aquila chrysaetos")
paloma = PalomaComun("Paloma de la Paz", "Columba livia")
pinguino = PinguinoEmperador("Pingu", "Aptenodytes forsteri")
avestruz = Avestruz("Speedy", "Struthio camelus")

# Todos pueden ser tratados como Animal - ✅ CUMPLE LSP
todos_los_animales = [aguila, paloma, pinguino, avestruz]
hacer_mover_animales(todos_los_animales)

print()

# Las aves voladoras pueden ser tratadas intercambiablemente - ✅ CUMPLE LSP
aves_voladoras = [aguila, paloma]
hacer_volar_aves_voladoras(aves_voladoras)

print()

# Las aves acuáticas pueden ser tratadas intercambiablemente - ✅ CUMPLE LSP
aves_acuaticas = [pinguino]
hacer_nadar_aves_acuaticas(aves_acuaticas)

print("\n" + "="*70 + "\n")

# 🔸 EJEMPLO AVANZADO: Sistema de formas geométricas
print("🔸 EJEMPLO AVANZADO: Formas geométricas que cumplen LSP")

class Forma(ABC):
    """Clase base para todas las formas geométricas"""
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass
    
    def obtener_info(self):
        return f"{self.nombre} - Área: {self.calcular_area():.2f}, Perímetro: {self.calcular_perimetro():.2f}"

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        super().__init__("Rectángulo")
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        return self.ancho * self.alto
    
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

class Cuadrado(Rectangulo):
    """CUMPLE LSP: Un cuadrado ES UN rectángulo especial"""
    
    def __init__(self, lado):
        super().__init__(lado, lado)  # ancho = alto = lado
        self.nombre = "Cuadrado"
        self.lado = lado
    
    # ✅ CUMPLE LSP: No modifica el comportamiento esperado
    # Los métodos heredados funcionan correctamente

class Circulo(Forma):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio
    
    def calcular_area(self):
        import math
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        import math
        return 2 * math.pi * self.radio

class Triangulo(Forma):
    def __init__(self, base, altura, lado1, lado2, lado3):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

def procesar_formas(formas):
    """Función que funciona con cualquier Forma - CUMPLE LSP"""
    print("📐 Procesando formas geométricas:")
    total_area = 0
    total_perimetro = 0
    
    for forma in formas:
        print(f"   {forma.obtener_info()}")
        total_area += forma.calcular_area()
        total_perimetro += forma.calcular_perimetro()
    
    print(f"\n📊 Totales:")
    print(f"   Área total: {total_area:.2f}")
    print(f"   Perímetro total: {total_perimetro:.2f}")

def calcular_area_total(formas):
    """Otra función que funciona con cualquier Forma"""
    return sum(forma.calcular_area() for forma in formas)

# Uso del sistema de formas - CUMPLE LSP
formas_geometricas = [
    Rectangulo(5, 3),
    Cuadrado(4),           # ✅ Puede sustituir a Rectangulo
    Circulo(2),
    Triangulo(6, 4, 5, 5, 6)
]

procesar_formas(formas_geometricas)

print(f"\n🔢 Área total calculada: {calcular_area_total(formas_geometricas):.2f}")

# ✅ El Cuadrado puede usarse donde se espera un Rectangulo
rectangulos = [Rectangulo(3, 4), Cuadrado(3)]  # LSP cumplido
print(f"\n📏 Área de rectángulos: {calcular_area_total(rectangulos):.2f}")

print("\n=== EJEMPLO DE VIOLACIÓN DE LSP (QUE NO HACER) ===")

class CuadradoMalo(Rectangulo):
    """VIOLA LSP: Modifica comportamiento esperado"""
    
    def __init__(self, lado):
        super().__init__(lado, lado)
        self.nombre = "Cuadrado Malo"
    
    def calcular_area(self):
        # ❌ VIOLA LSP: Comportamiento inesperado
        print("⚠️ ADVERTENCIA: Calculando área de cuadrado de forma especial")
        return super().calcular_area() + 1  # Comportamiento incorrecto

# Demostración de la violación
cuadrado_malo = CuadradoMalo(3)
print(f"Área esperada: 9, Área obtenida: {cuadrado_malo.calcular_area()}")

print("\n=== PRINCIPIOS PARA CUMPLIR LSP ===")
print("✅ Las subclases deben cumplir el contrato de la superclase")
print("✅ No deben lanzar excepciones inesperadas")
print("✅ No deben requerir precondiciones más estrictas")
print("✅ No deben debilitar las postcondiciones")
print("✅ Deben mantener las invariantes de la clase base")

print("\n=== CÓMO IDENTIFICAR VIOLACIONES DE LSP ===")
print("❌ Subclases que lanzan excepciones no esperadas")
print("❌ Métodos que no hacen nada (implementación vacía)")
print("❌ Comportamiento completamente diferente al esperado")
print("❌ Necesidad de verificar el tipo antes de usar el objeto")
print("❌ Subclases que requieren parámetros adicionales")
