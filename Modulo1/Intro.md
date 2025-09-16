Perfecto 🙌
Aquí tienes el **Módulo 1 completo** en formato **`README.md`**, listo para usar como material del curso:

````markdown
# 📘 Módulo 1: Introducción a la Programación Orientada a Objetos (POO)

Duración estimada: **45 minutos**

---

## 🎯 Objetivos del módulo
- Comprender qué es la POO y por qué se usa.
- Conocer los principales paradigmas de programación.
- Entender los conceptos básicos: **clase, objeto, atributos, métodos, encapsulamiento**.
- Realizar un primer ejemplo práctico en **Python**.

---

## 1. ¿Qué es la Programación Orientada a Objetos?
La **POO** es un paradigma que organiza el código en **objetos** que combinan:
- **Atributos** → datos (estado).
- **Métodos** → funciones (comportamiento).

✅ Ventajas:
- Reutilización de código.
- Mantenimiento más sencillo.
- Escalabilidad en proyectos grandes.

Ejemplo del mundo real:
- Clase = `Coche`
- Objeto = `MiCoche (Toyota, rojo)`

---

## 2. Paradigmas de programación

### 🔹 Programación Imperativa
- Basada en dar instrucciones paso a paso.
- El foco está en **cómo** se hace la tarea.
- Ejemplos: C, Pascal, Python (en estilo imperativo).

```python
# Calcular la suma de una lista (imperativo)
numeros = [1, 2, 3, 4]
suma = 0
for n in numeros:
    suma += n
print(suma)
````

---

### 🔹 Programación Declarativa

* Se centra en **qué queremos lograr**, no en los pasos.
* Ejemplo: SQL, HTML.

```sql
SELECT SUM(valor) FROM numeros;
```

---

### 🔹 Programación Funcional

* Basada en **funciones puras** y evitar estados mutables.
* Ventajas: código más predecible y fácil de testear.
* Ejemplos: Haskell, Scala, Python (funcional).

```python
# Calcular suma (funcional)
numeros = [1, 2, 3, 4]
print(sum(numeros))
```

---

### 🔹 Programación Orientada a Objetos

* Organiza el código en **objetos** que representan entidades del mundo real.
* Cada objeto tiene:

  * **Atributos** (estado).
  * **Métodos** (comportamiento).
* Ejemplos: Java, C#, Python, C++.

```python
class Coche:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def arrancar(self):
        print(f"El {self.marca} arranca!")

mi_coche = Coche("Toyota", "Rojo")
mi_coche.arrancar()
```

---

### 📊 Comparativa rápida

| Paradigma        | Ejemplo Lenguajes | Foco principal                      |
| ---------------- | ----------------- | ----------------------------------- |
| Imperativo       | C, Python         | Secuencia de instrucciones          |
| Declarativo      | SQL, HTML         | Qué quiero, no cómo                 |
| Funcional        | Haskell, Python   | Funciones puras, sin estado         |
| Orientado a Obj. | Java, C#, Python  | Objetos con estado y comportamiento |

---

## 3. Clases y objetos en Python

```python
# Definición de una clase
class Coche:
    def __init__(self, marca, color):
        self.marca = marca      # atributo
        self.color = color      # atributo
    
    def arrancar(self):         # método
        return f"El {self.marca} de color {self.color} está arrancando"

# Crear objetos
coche1 = Coche("Toyota", "rojo")
coche2 = Coche("Ford", "azul")

print(coche1.arrancar())
print(coche2.arrancar())
```

✅ Resultado:

```
El Toyota de color rojo está arrancando
El Ford de color azul está arrancando
```

---

## 4. Atributos y métodos

* **Atributos** → variables dentro de la clase (estado del objeto).
* **Métodos** → funciones dentro de la clase (comportamiento del objeto).

---

## 5. Encapsulamiento

El **encapsulamiento** consiste en ocultar detalles internos de una clase y exponer solo lo necesario.

En Python no existe `private` como en Java, pero se simula con `_` y `__`.

```python
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo   # atributo "privado"

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def mostrar_saldo(self):
        return f"Saldo de {self.titular}: {self.__saldo}€"

cuenta = CuentaBancaria("Ana", 1000)
cuenta.depositar(500)
print(cuenta.mostrar_saldo())
# print(cuenta.__saldo)  # ❌ dará error
```

---

## 📝 Mini-ejercicio

Define una clase **Alumno** con:

* Atributos: `nombre`, `edad`.
* Método: `presentarse()` que imprima
  `"Hola, soy <nombre> y tengo <edad> años"`.
* Crea 2 objetos y llama al método.

---

## ✅ Resumen del Módulo 1

* La POO organiza el código en **objetos** con atributos y métodos.
* Existen varios paradigmas: imperativo, declarativo, funcional y orientado a objetos.
* Python permite aplicar POO de manera sencilla.
* Conceptos básicos: **clases, objetos, atributos, métodos, encapsulamiento**.

---

```

---

¿Quieres que haga lo mismo con los siguientes módulos (2, 3, 4, …) para que al final tengas un **repositorio completo de curso en Markdown**, o prefieres que avancemos módulo por módulo en detalle como este y luego unimos todo en un solo `README.md` grande?
```
