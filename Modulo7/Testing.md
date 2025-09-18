
# 📘 Módulo 7: Testing y Calidad del Software

## 🎯 Objetivos del módulo
- Comprender los diferentes **tipos de testing**.  
- Introducir el enfoque de **Test-Driven Development (TDD)**.  
- Conocer herramientas de testing en Python (`pytest`).  
- Usar **mocks, fakes y stubs** para aislar pruebas.  
- Practicar con ejemplos de tests sobre clases de dominio.  

---

## 1. Tipos de Testing
- **Unitario** → Prueba funciones o clases de manera aislada.  
- **Integración** → Comprueba cómo interactúan varios módulos.  
- **Funcional / End-to-End** → Valida el sistema completo desde el punto de vista del usuario.  

Ejemplo gráfico:
- 🧩 Unit → ¿Funciona este método?  
- 🔗 Integración → ¿Funciona el flujo entre módulos?  
- 🌍 End-to-End → ¿Funciona todo como lo espera el usuario?  

---

## 2. Introducción a Pytest
Instalación:
```bash
pip install pytest
````

Ejemplo de test unitario:

```python
# calculadora.py
def sumar(a, b):
    return a + b

# test_calculadora.py
from calculadora import sumar

def test_sumar():
    assert sumar(2, 3) == 5
```

Ejecutar:

```bash
pytest
```

---

## 3. Test-Driven Development (TDD)

Enfoque: **Escribir primero el test, luego el código.**

Flujo:

1. Escribir una prueba (fallará).
2. Implementar el código mínimo para pasar la prueba.
3. Refactorizar.

Ejemplo:

```python
# Paso 1: test (rojo)
def test_es_par():
    assert es_par(4) == True
    assert es_par(5) == False

# Paso 2: implementación
def es_par(n):
    return n % 2 == 0
```

---

## 4. Mocks, Fakes y Stubs

* **Stub** → Devuelve valores predefinidos.
* **Fake** → Implementación simple usada solo en tests.
* **Mock** → Simula objetos y verifica llamadas.

Ejemplo con `unittest.mock`:

```python
from unittest.mock import Mock

class ServicioEmail:
    def enviar(self, destinatario, mensaje):
        pass

def notificar(servicio, usuario):
    servicio.enviar(usuario.email, "Hola!")

def test_notificar():
    servicio_mock = Mock()
    usuario = Mock()
    usuario.email = "test@mail.com"

    notificar(servicio_mock, usuario)

    servicio_mock.enviar.assert_called_once_with("test@mail.com", "Hola!")
```

---

## 5. Pruebas para Clases de Dominio

Ejemplo clase de dominio:

```python
class Pedido:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def total(self):
        return sum(self.productos)
```

Test unitario:

```python
def test_total_pedido():
    pedido = Pedido()
    pedido.agregar_producto(10)
    pedido.agregar_producto(20)
    assert pedido.total() == 30
```

---

## 📝 Mini-ejercicio

1. Crea una clase `CuentaBancaria` con métodos: `depositar()`, `retirar()` y `saldo()`.
2. Escribe pruebas unitarias para validar:

   * Depositar aumenta el saldo.
   * Retirar reduce el saldo.
   * No se puede retirar más de lo disponible.

---

## ✅ Resumen del Módulo 7

* El testing mejora la **calidad y mantenibilidad** del software.
* **Pytest** facilita pruebas rápidas y legibles.
* **TDD** ayuda a diseñar código orientado a pruebas.
* **Mocks, fakes y stubs** permiten aislar dependencias externas.
* Siempre probar la **lógica de dominio** de manera independiente.
