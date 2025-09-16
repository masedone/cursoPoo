
# 📘 Módulo 4: Principios SOLID

## 🎯 Objetivos del módulo
- Comprender los **5 principios SOLID**.  
- Aplicar refactorizaciones en Python para mejorar el diseño del software.  
- Evitar código rígido, frágil o difícil de mantener.  

---

## 1. S – Single Responsibility Principle (SRP)
**Una clase debe tener una sola razón para cambiar.**

```python
# ❌ Violación de SRP
class Reporte:
    def generar_pdf(self): pass
    def guardar_en_bd(self): pass
    def enviar_email(self): pass

# ✅ Aplicando SRP
class Reporte: pass
class ReporteRepositorio: pass
class ReporteNotificador: pass
````

---

## 2. O – Open/Closed Principle (OCP)

**Las clases deben estar abiertas a extensión pero cerradas a modificación.**

```python
# ❌ Violación de OCP
class Calculadora:
    def calcular(self, tipo, a, b):
        if tipo == "suma": return a + b
        elif tipo == "resta": return a - b

# ✅ Aplicando OCP con polimorfismo
class Operacion:
    def calcular(self, a, b): pass

class Suma(Operacion):
    def calcular(self, a, b): return a + b

class Resta(Operacion):
    def calcular(self, a, b): return a - b

operaciones = [Suma(), Resta()]
for op in operaciones:
    print(op.calcular(5, 3))
```

---

## 3. L – Liskov Substitution Principle (LSP)

**Una subclase debe poder sustituir a su superclase sin alterar el comportamiento esperado.**

```python
# ❌ Violación de LSP
class Ave:
    def volar(self): return "Volando"

class Pinguino(Ave):
    def volar(self): raise Exception("No puede volar")

# ✅ Cumpliendo LSP
class Ave: pass
class AveVoladora(Ave):
    def volar(self): return "Volando"
class AveNoVoladora(Ave):
    def caminar(self): return "Caminando"
```

---

## 4. I – Interface Segregation Principle (ISP)

**Una clase no debe implementar interfaces que no necesita.**

En Python no existen interfaces explícitas, pero se aplican con clases abstractas o `Protocol`.

```python
from abc import ABC, abstractmethod

# ❌ Mala práctica: interfaz demasiado grande
class Trabajador(ABC):
    @abstractmethod
    def programar(self): pass
    @abstractmethod
    def diseñar(self): pass
    @abstractmethod
    def testear(self): pass

# ✅ Interfaz segregada
class Programador(ABC):
    @abstractmethod
    def programar(self): pass

class Diseñador(ABC):
    @abstractmethod
    def diseñar(self): pass
```

---

## 5. D – Dependency Inversion Principle (DIP)

**Los módulos de alto nivel no deben depender de módulos de bajo nivel, ambos deben depender de abstracciones.**

```python
# ❌ Violación de DIP
class MotorGasolina:
    def encender(self): return "Motor gasolina encendido"

class Coche:
    def __init__(self):
        self.motor = MotorGasolina()  # depende de implementación concreta
    def arrancar(self):
        return self.motor.encender()

# ✅ Cumpliendo DIP
class Motor:
    def encender(self): pass

class MotorGasolina(Motor):
    def encender(self): return "Motor gasolina encendido"

class MotorElectrico(Motor):
    def encender(self): return "Motor eléctrico encendido"

class Coche:
    def __init__(self, motor: Motor):
        self.motor = motor
    def arrancar(self):
        return self.motor.encender()

coche1 = Coche(MotorGasolina())
coche2 = Coche(MotorElectrico())
print(coche1.arrancar())
print(coche2.arrancar())
```

---

## 📝 Ejercicio práctico

1. Implementa una clase `Notificador` que envíe mensajes.
2. Inicialmente solo enviará **email**, pero debe cumplir OCP para poder extender a **SMS** o **Push Notification** sin modificar la clase original.
3. Aplica DIP para que el `GestorDeMensajes` dependa de una **abstracción** y no de una implementación concreta.

---

## ✅ Resumen del Módulo 4

* **S**: Cada clase con una sola responsabilidad.
* **O**: Abierto a extensión, cerrado a modificación.
* **L**: Subclases deben ser sustituibles por superclases.
* **I**: Interfaces pequeñas y específicas.
* **D**: Dependencia de abstracciones, no de implementaciones.

Aplicar **SOLID** da como resultado un código:

* Flexible.
* Escalable.
* Fácil de mantener.
