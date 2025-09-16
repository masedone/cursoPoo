Perfecto 🙌
Aquí tienes el **Módulo 2 completo** en formato **`README.md`**:

````markdown
# 📘 Módulo 2: Fundamentos de POO

Duración estimada: **45 minutos**

---

## 🎯 Objetivos del módulo
- Comprender los pilares de la POO: **constructores, herencia, polimorfismo, abstracción, interfaces**.  
- Diferenciar **composición vs herencia**.  
- Practicar con ejemplos en **Python**.  

---

## 1. Constructores
Los **constructores** son métodos especiales que inicializan un objeto al momento de su creación.  
En Python se utiliza `__init__()` y se ejecuta automáticamente al instanciar la clase.  

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"

p1 = Persona("Ana", 25)
print(p1.presentarse())
````

🔹 Resultado:

```
Hola, soy Ana y tengo 25 años
```

---

## 2. Herencia

La **herencia** permite que una clase hija reciba atributos y métodos de una clase padre.
Promueve la **reutilización** de código.

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        return "Hace un sonido"

class Perro(Animal):   # hereda de Animal
    def hablar(self):
        return "Guau!"

class Gato(Animal):    # hereda de Animal
    def hablar(self):
        return "Miau!"

animales = [Perro("Firulais"), Gato("Michi")]
for a in animales:
    print(f"{a.nombre}: {a.hablar()}")
```

---

## 3. Polimorfismo

El **polimorfismo** significa “muchas formas”.
Permite que **el mismo método** tenga diferentes comportamientos según el objeto.

```python
def hacer_hablar(animal):
    print(animal.hablar())

hacer_hablar(Perro("Rocky"))  # Guau!
hacer_hablar(Gato("Luna"))   # Miau!
```

---

## 4. Abstracción

La **abstracción** consiste en ocultar la complejidad y mostrar solo lo esencial.
En Python se implementa con **clases abstractas** (módulo `abc`).

```python
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto

r = Rectangulo(4, 5)
print(r.area())  # 20
```

---

## 5. Composición vs Herencia

* **Herencia**: relación “Es un” → un `Perro` **es un** `Animal`.
* **Composición**: relación “Tiene un” → un `Coche` **tiene un** `Motor`.

```python
class Motor:
    def encender(self):
        return "Motor encendido"

class Coche:
    def __init__(self):
        self.motor = Motor()  # Composición
    
    def arrancar(self):
        return self.motor.encender() + " y el coche arranca"
```

---

## 6. Interfaces y clases abstractas

* **Clases abstractas**: definen métodos que deben implementarse en clases hijas.
* **Interfaces**: en Python no existen como tal, pero se simulan con clases abstractas o `Protocol` (desde `typing`).

---

## 📝 Mini-ejercicio

1. Define una clase abstracta `Empleado` con un método `calcular_salario()`.
2. Implementa dos clases hijas:

   * `EmpleadoFijo` (sueldo fijo).
   * `EmpleadoPorHoras` (sueldo por horas trabajadas).
3. Crea una lista con ambos tipos de empleados y muestra sus salarios.

---

## ✅ Resumen del Módulo 2

* Los **constructores** inicializan objetos (`__init__` en Python).
* La **herencia** permite reutilizar código entre clases.
* El **polimorfismo** da distintos comportamientos a un mismo método.
* La **abstracción** define qué debe hacer una clase, pero no cómo.
* La **composición** se usa como alternativa a la herencia.
* Python maneja **interfaces** a través de clases abstractas o `Protocol`.

