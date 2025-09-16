
# 📘 Módulo 6: Introducción a Domain-Driven Design (DDD)

Duración estimada: **45 minutos**

---

## 🎯 Objetivos del módulo
- Comprender qué es el **Domain-Driven Design (DDD)**.  
- Entender el uso del **lenguaje ubicuo** y la **importancia del dominio**.  
- Conocer los conceptos clave: **Entidades, Value Objects, Aggregates, Repositories, Bounded Contexts**.  
- Ver ejemplos simples de cómo aplicar DDD en Python.  

---

## 1. ¿Qué es DDD?
- Metodología propuesta por **Eric Evans**.  
- Enfocada en **resolver problemas complejos alineando software con el dominio del negocio**.  
- Usa un **lenguaje común (ubícuo)** entre desarrolladores y expertos del negocio.  

---

## 2. Lenguaje Ubicuo y Modelo de Dominio
- El **lenguaje ubicuo** es un vocabulario compartido por negocio y tecnología.  
- El **modelo de dominio** representa las reglas y conceptos del negocio.  

Ejemplo:  
- Dominio: **E-commerce**.  
- Términos del negocio: Cliente, Pedido, Producto.  
- Estos mismos nombres deben usarse en el código.  

---

## 3. Entidades
- Objetos con **identidad única** (generalmente un ID).  
- Su ciclo de vida importa.  

```python
class Cliente:
    def __init__(self, cliente_id, nombre):
        self.cliente_id = cliente_id
        self.nombre = nombre
````

---

## 4. Value Objects

* Objetos definidos por sus **atributos**, no por identidad.
* Son **inmutables**.

```python
class Direccion:
    def __init__(self, calle, ciudad):
        self.calle = calle
        self.ciudad = ciudad

    def __eq__(self, other):
        return self.calle == other.calle and self.ciudad == other.ciudad
```

---

## 5. Aggregates y Repositories

* **Aggregate**: conjunto de entidades y value objects que se tratan como una unidad.
* **Repository**: capa que abstrae el acceso a datos del dominio.

```python
class Pedido:
    def __init__(self, pedido_id, cliente, productos):
        self.pedido_id = pedido_id
        self.cliente = cliente
        self.productos = productos

class PedidoRepository:
    def __init__(self):
        self._pedidos = {}

    def guardar(self, pedido):
        self._pedidos[pedido.pedido_id] = pedido

    def obtener(self, pedido_id):
        return self._pedidos.get(pedido_id)
```

---

## 6. Anti-Corruption Layer y Bounded Contexts

* **Bounded Context**: límite que separa un modelo del dominio de otro.
* Evita confusión entre términos que pueden tener distinto significado en distintos contextos.
* **Anti-Corruption Layer (ACL)**: capa que traduce entre dos contextos diferentes.

Ejemplo:

* En un sistema de logística, “Cliente” puede significar **usuario que compra**.
* En un sistema de facturación, “Cliente” puede significar **razón social registrada**.

La ACL permite que ambos convivan sin conflictos.

---

## 📝 Mini-ejercicio

1. Define una **Entidad** `Libro` con atributos: `id`, `titulo`, `autor`.
2. Define un **Value Object** `Precio` con `cantidad` y `moneda`.
3. Crea un **Aggregate** `Carrito` que contenga varios libros.
4. Implementa un **Repository** que guarde y recupere carritos en memoria.

---

## ✅ Resumen del Módulo 6

* DDD alinea software con el dominio del negocio.
* Usa un **lenguaje ubicuo** compartido por todos los involucrados.
* **Entidades**: tienen identidad.
* **Value Objects**: definidos solo por sus atributos.
* **Aggregates y Repositories**: organizan y abstraen el acceso a datos.
* **Bounded Contexts** y **Anti-Corruption Layer** evitan conflictos entre modelos distintos.
