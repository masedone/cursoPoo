## 🔹 INTERFACES vs CLASES ABSTRACTAS
# ¿Cuál es la diferencia entre una interfaz y una clase abstracta?

from abc import ABC, abstractmethod

print("=== DIFERENCIA: INTERFACES vs CLASES ABSTRACTAS ===\n")

# 🔸 INTERFACE (en Python simulada con ABC)
# - Solo define métodos (sin implementación)
# - No tiene atributos/estado
# - Define un "contrato" puro

class IVolador(ABC):
    """INTERFACE: Solo define QUÉ debe hacer un objeto volador"""
    
    @abstractmethod
    def volar(self):
        pass
    
    @abstractmethod
    def aterrizar(self):
        pass

class INadador(ABC):
    """INTERFACE: Solo define QUÉ debe hacer un objeto nadador"""
    
    @abstractmethod
    def nadar(self):
        pass

# 🔸 CLASE ABSTRACTA
# - Puede tener métodos abstractos Y concretos
# - Puede tener atributos/estado
# - Define comportamiento común + contrato

class Animal(ABC):
    """CLASE ABSTRACTA: Tiene estado Y comportamiento común"""
    
    def __init__(self, nombre, peso):
        self.nombre = nombre  # ESTADO/ATRIBUTOS
        self.peso = peso
    
    # Método concreto (ya implementado)
    def mostrar_info(self):
        print(f"Animal: {self.nombre}, Peso: {self.peso}kg")
    
    # Método abstracto (debe implementarse)
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    @abstractmethod
    def moverse(self):
        pass

print("=== COMPARACIÓN PRÁCTICA ===")

# 🔸 IMPLEMENTACIONES QUE USAN AMBOS CONCEPTOS

class Pato(Animal, IVolador, INadador):
    """Pato: Hereda de Animal E implementa interfaces IVolador e INadador"""
    
    def __init__(self, nombre, peso):
        super().__init__(nombre, peso)
    
    # Métodos abstractos de Animal (OBLIGATORIOS)
    def hacer_sonido(self):
        return "Cuac!"
    
    def moverse(self):
        return "Caminando con patas palmeadas"
    
    # Métodos de IVolador (OBLIGATORIOS)
    def volar(self):
        return "Volando con alas"
    
    def aterrizar(self):
        return "Aterrizando en el agua"
    
    # Métodos de INadador (OBLIGATORIOS)
    def nadar(self):
        return "Nadando en el agua"

class Perro(Animal):
    """Perro: Solo hereda de Animal (no vuela ni nada especial)"""
    
    def __init__(self, nombre, peso):
        super().__init__(nombre, peso)
    
    def hacer_sonido(self):
        return "Guau!"
    
    def moverse(self):
        return "Corriendo con patas"

class Avion(IVolador):
    """Avión: NO es Animal, pero SÍ implementa IVolador"""
    
    def __init__(self, modelo):
        self.modelo = modelo
    
    def volar(self):
        return f"Avión {self.modelo} volando con motores"
    
    def aterrizar(self):
        return f"Avión {self.modelo} aterrizando en pista"

# 🔸 USANDO LAS IMPLEMENTACIONES

print("=== ANIMAL CON MÚLTIPLES HABILIDADES ===")
pato = Pato("Donald", 2.5)
pato.mostrar_info()  # Método de la clase abstracta Animal
print(f"Sonido: {pato.hacer_sonido()}")
print(f"Movimiento: {pato.moverse()}")
print(f"Volando: {pato.volar()}")
print(f"Nadando: {pato.nadar()}")
print(f"Aterrizando: {pato.aterrizar()}")
print()

print("=== ANIMAL SIMPLE ===")
perro = Perro("Firulais", 15)
perro.mostrar_info()
print(f"Sonido: {perro.hacer_sonido()}")
print(f"Movimiento: {perro.moverse()}")
print()

print("=== OBJETO NO-ANIMAL QUE VUELA ===")
avion = Avion("Boeing 747")
print(f"Volando: {avion.volar()}")
print(f"Aterrizando: {avion.aterrizar()}")
print()

# 🔸 POLIMORFISMO CON INTERFACES
print("=== POLIMORFISMO CON INTERFACES ===")
print("Todos los objetos que pueden volar:")

voladores = [pato, avion]  # Pato y Avión implementan IVolador
for volador in voladores:
    print(f"- {volador.volar()}")

print("\nTodos los animales:")
animales = [pato, perro]  # Ambos heredan de Animal
for animal in animales:
    animal.mostrar_info()
    print(f"  Sonido: {animal.hacer_sonido()}")

print("\n=== TABLA COMPARATIVA ===")
print("| Aspecto              | INTERFACE           | CLASE ABSTRACTA     |")
print("|----------------------|---------------------|---------------------|")
print("| Métodos concretos    | ❌ No               | ✅ Sí               |")
print("| Métodos abstractos   | ✅ Solo abstractos  | ✅ Ambos tipos      |")
print("| Atributos/Estado     | ❌ No               | ✅ Sí               |")
print("| Herencia múltiple    | ✅ Sí (interfaces)  | ❌ No (solo una)    |")
print("| Constructor          | ❌ No               | ✅ Sí               |")
print("| Propósito            | Contrato puro       | Comportamiento base |")

print("\n=== CUÁNDO USAR CADA UNO ===")
print("🔸 USA INTERFACE cuando:")
print("  ✅ Solo defines QUÉ debe hacer (contrato)")
print("  ✅ No hay comportamiento común")
print("  ✅ Quieres múltiples 'habilidades'")
print("  ✅ Ejemplo: IVolador, INadador, IConducible")

print("\n🔸 USA CLASE ABSTRACTA cuando:")
print("  ✅ Tienes comportamiento común Y métodos obligatorios")
print("  ✅ Quieres compartir estado/atributos")
print("  ✅ Hay una relación 'es-un'")
print("  ✅ Ejemplo: Animal, Vehiculo, Forma")

print("\n🎯 EN RESUMEN:")
print("INTERFACE = 'puede hacer' (habilidades)")
print("CLASE ABSTRACTA = 'es un tipo de' (herencia)")
