
# 🏗️ Módulo 5: Arquitectura básica de software

## 1. ¿Qué es la arquitectura de software?

La **arquitectura de software** define la organización fundamental de un sistema, sus componentes y cómo se relacionan entre sí.
Su objetivo principal es proporcionar una **base sólida, escalable y mantenible** para el desarrollo.

🔑 Beneficios:

* Mejora la **comprensión** del sistema.
* Facilita la **mantenibilidad** y evolución.
* Permite **detectar errores de diseño** de forma temprana.
* Fomenta la **reutilización** de componentes.

---

## 2. Patrones comunes de arquitectura

* **Monolito**:
  Toda la aplicación se desarrolla como una sola unidad.

  * ✅ Ventaja: simple de desplegar y probar.
  * ❌ Desventaja: difícil de escalar y mantener a largo plazo.

* **MVC (Modelo–Vista–Controlador)**:
  Separa responsabilidades en tres capas:

  * **Modelo** → lógica de negocio y datos.
  * **Vista** → interfaz con el usuario.
  * **Controlador** → coordina las interacciones.

* **Arquitectura en capas**:

  * Capa de presentación
  * Capa de lógica de negocio
  * Capa de acceso a datos

---

## 3. Patrón MVC en detalle

* **Modelo**:
  Representa los datos y reglas de negocio.
  Ejemplo: `Usuario`, `Producto`, `Pedido`.

* **Vista**:
  Encargada de mostrar información al usuario.
  Ejemplo: plantillas HTML, componentes gráficos.

* **Controlador**:
  Gestiona las solicitudes y coordina la comunicación entre Vista y Modelo.
  Ejemplo: `UsuarioController`, `PedidoController`.

📌 Este patrón es muy usado en frameworks como **Laravel, Spring MVC, Django, Ruby on Rails**.

---

## 4. Separación de capas

Una aplicación bien estructurada suele dividirse en capas:

* **Presentación** → interfaces, páginas web, API públicas.
* **Lógica de negocio** → reglas del dominio, validaciones.
* **Persistencia** → gestión de base de datos.

🎯 Objetivo: cada capa debe estar **lo más desacoplada posible** de las demás.

---

## 5. Inversión de dependencias y contenedores (DI/IoC)

* **Inversión de dependencias**:
  En lugar de que una clase cree directamente sus dependencias, las recibe desde fuera.
  Esto permite:

  * Reemplazar dependencias fácilmente.
  * Mejorar las pruebas unitarias.

* **Contenedores de inversión de control (IoC)**:
  Herramientas que gestionan automáticamente las dependencias.
  Ejemplos:

  * **Spring** (Java)
  * **Laravel Service Container** (PHP)
  * **Unity / Autofac** (.NET)

---

## ✅ Resumen

* La arquitectura de software organiza los componentes de una aplicación.
* Patrones como **Monolito, MVC y por capas** son muy comunes.
* El patrón **MVC** separa presentación, negocio y datos.
* La **separación de capas** mejora la mantenibilidad.
* La **inversión de dependencias (DI/IoC)** es clave para lograr aplicaciones flexibles y testeables.

