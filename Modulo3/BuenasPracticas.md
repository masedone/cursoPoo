
# 📘 Módulo 3: Buenas prácticas en POO

---

## 🎯 Objetivos del módulo
- Aplicar principios de **código limpio** en programación orientada a objetos.  
- Entender la importancia de la **cohesión** y el **acoplamiento bajo**.  
- Conocer el **principio de responsabilidad única (SRP)**.  
- Identificar **antipatrones comunes** y cómo evitarlos.  

---

## 1. Nombres claros y autoexplicativos
✅ Usar nombres significativos mejora la legibilidad y mantenimiento del código.

```python
# ❌ MALA PRÁCTICA - Nombres confusos
class P:                    # ¿Qué es P?
    def __init__(self, n, p):
        self.n = n          # ¿Qué es n?
        self.p = p          # ¿Qué es p?
    
    def f(self, x):         # ¿Qué hace f?
        return x * 1.21     # ¿Por qué 1.21?
    
    def g(self):            # ¿Qué hace g?
        if self.p < 10:
            return True
        return False

# Ejemplo de uso (confuso):
p = P("Laptop", 500)
print(p.f(100))  # ¿Qué está calculando?

# ✅ BUENA PRÁCTICA - Nombres descriptivos
class Producto:
    IVA_PORCENTAJE = 1.21   # Constante clara
    
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base
    
    def calcular_precio_con_iva(self, precio_sin_iva):
        """Calcula el precio final incluyendo el IVA del 21%"""
        return precio_sin_iva * self.IVA_PORCENTAJE
    
    def es_producto_barato(self):
        """Determina si el producto cuesta menos de 10€"""
        return self.precio_base < 10
    
    def obtener_resumen(self):
        """Devuelve un resumen completo del producto"""
        precio_final = self.calcular_precio_con_iva(self.precio_base)
        categoria = "Barato" if self.es_producto_barato() else "Caro"
        return f"{self.nombre}: {precio_final:.2f}€ ({categoria})"

# Ejemplo de uso (claro):
laptop = Producto("Laptop Gaming", 500)
print(laptop.obtener_resumen())  # Laptop Gaming: 605.00€ (Caro)
print(laptop.calcular_precio_con_iva(100))  # 121.0
```

**¿Por qué es mejor?**
- **Claro**: Sabes qué hace cada método sin leer el código
- **Mantenible**: Fácil de modificar y entender meses después
- **Documentado**: Los nombres son autodocumentación

---

## 2. Cohesión y acoplamiento

* **Cohesión alta**: cada clase hace una sola cosa bien y todas sus partes trabajan juntas.
* **Acoplamiento bajo**: las clases dependen lo mínimo posible unas de otras.

```python
# ❌ MALA PRÁCTICA - Baja cohesión y alto acoplamiento
class GestorTodoEnUno:
    """Clase que hace DEMASIADAS cosas diferentes"""
    
    def __init__(self):
        self.conexion_bd = "mysql://localhost"
        self.servidor_email = "smtp.gmail.com"
        self.empleados = []
    
    def conectar_bd(self):
        print(f"Conectando a {self.conexion_bd}")
        return "conectado"
    
    def calcular_nomina(self, empleado_id):
        # ¿Por qué una clase de BD calcula nóminas?
        salario_base = 1000
        print(f"Calculando nómina para empleado {empleado_id}: {salario_base}")
        return salario_base
    
    def enviar_email(self, destinatario, mensaje):
        # ¿Por qué una clase de nóminas envía emails?
        print(f"Enviando email a {destinatario}: {mensaje}")
        return "enviado"
    
    def generar_reporte_pdf(self):
        # ¿Por qué una clase de email genera PDFs?
        print("Generando PDF...")
        return "reporte.pdf"

# Usar esta clase es confuso y frágil:
gestor = GestorTodoEnUno()
gestor.conectar_bd()          # ¿Para qué se conecta?
gestor.calcular_nomina(123)   # ¿Necesita BD para esto?
gestor.enviar_email("juan@email.com", "Hola")  # ¿Y esto para qué?

# ✅ BUENA PRÁCTICA - Alta cohesión y bajo acoplamiento
class ConexionBD:
    """Solo se encarga de la conexión a base de datos"""
    
    def __init__(self, url_conexion):
        self.url_conexion = url_conexion
        self.conectado = False
    
    def conectar(self):
        print(f"Conectando a {self.url_conexion}")
        self.conectado = True
        return self
    
    def ejecutar_consulta(self, sql):
        if not self.conectado:
            raise Exception("Debe conectar primero")
        print(f"Ejecutando: {sql}")
        return ["resultado1", "resultado2"]

class CalculadoraNomina:
    """Solo se encarga de cálculos de nómina"""
    
    def __init__(self, bd):
        self.bd = bd  # Recibe la dependencia, no la crea
    
    def calcular_salario(self, empleado_id):
        # Obtiene datos de BD
        datos = self.bd.ejecutar_consulta(f"SELECT * FROM empleados WHERE id={empleado_id}")
        
        # Solo calcula, no hace otras cosas
        salario_base = 1000
        bonos = 200
        total = salario_base + bonos
        
        print(f"Salario calculado para {empleado_id}: {total}€")
        return total

class ServicioEmail:
    """Solo se encarga de enviar emails"""
    
    def __init__(self, servidor_smtp):
        self.servidor = servidor_smtp
    
    def enviar(self, destinatario, asunto, mensaje):
        print(f"📧 Enviando email a {destinatario}")
        print(f"   Asunto: {asunto}")
        print(f"   Mensaje: {mensaje}")
        return {"status": "enviado", "id": "12345"}

# Uso con buenas prácticas (más claro y mantenible):
print("=== USANDO CLASES COHESIONADAS ===")

# Cada clase tiene una responsabilidad clara
bd = ConexionBD("mysql://localhost").conectar()
calculadora = CalculadoraNomina(bd)
email_service = ServicioEmail("smtp.gmail.com")

# Cada operación es clara y específica
salario = calculadora.calcular_salario(123)
email_service.enviar(
    "empleado@empresa.com", 
    "Tu nómina", 
    f"Tu salario es: {salario}€"
)
```

**Ventajas de la buena práctica:**
- **Fácil de testear**: Cada clase se prueba independientemente
- **Fácil de mantener**: Cambios en BD no afectan email
- **Reutilizable**: Puedes usar `ServicioEmail` en otros lugares
- **Claro**: Cada clase tiene un propósito obvio

---

## 3. Principio de Responsabilidad Única (SRP)

**Una clase debe tener una sola razón para cambiar.** Si cambias la BD, el formato PDF o el email, no deberían afectarse entre sí.

```python
# ❌ VIOLACIÓN DE SRP - Una clase con múltiples responsabilidades
class ReporteVentasCompleto:
    """Esta clase hace DEMASIADAS cosas y tiene múltiples razones para cambiar"""
    
    def __init__(self, datos_ventas):
        self.datos = datos_ventas
        self.conexion_bd = "mysql://localhost"
        self.servidor_email = "smtp.empresa.com"
    
    def generar_pdf(self):
        """RESPONSABILIDAD 1: Generar PDF"""
        print("📄 Generando reporte PDF...")
        # Si cambia el formato PDF, hay que modificar esta clase
        contenido = f"Reporte de Ventas\n"
        for venta in self.datos:
            contenido += f"- {venta}\n"
        
        with open("reporte.pdf", "w") as f:
            f.write(contenido)
        print("✅ PDF generado: reporte.pdf")
        return "reporte.pdf"
    
    def guardar_en_bd(self):
        """RESPONSABILIDAD 2: Guardar en base de datos"""
        print("💾 Guardando en base de datos...")
        # Si cambia la BD, hay que modificar esta clase
        print(f"Conectando a {self.conexion_bd}")
        for venta in self.datos:
            print(f"INSERT INTO reportes VALUES ('{venta}')")
        print("✅ Guardado en BD")
        return "guardado"
    
    def enviar_email(self, destinatario):
        """RESPONSABILIDAD 3: Enviar por email"""
        print("📧 Enviando por email...")
        # Si cambia el servidor de email, hay que modificar esta clase
        print(f"Servidor: {self.servidor_email}")
        print(f"Para: {destinatario}")
        print(f"Asunto: Reporte de Ventas")
        print("✅ Email enviado")
        return "enviado"
    
    def procesar_completo(self, destinatario):
        """Hace todo junto - muy frágil"""
        pdf = self.generar_pdf()
        self.guardar_en_bd()
        self.enviar_email(destinatario)
        return pdf

# Problemas de usar esta clase:
print("=== PROBLEMAS DEL ENFOQUE MALO ===")
ventas = ["Venta 1: 100€", "Venta 2: 200€", "Venta 3: 150€"]
reporte_malo = ReporteVentasCompleto(ventas)

# Si cualquier cosa cambia, toda la clase se ve afectada
reporte_malo.procesar_completo("gerente@empresa.com")

print("\n" + "="*50 + "\n")

# ✅ APLICANDO SRP - Cada clase tiene una sola responsabilidad
class ReporteVentas:
    """SOLO se encarga de los datos del reporte"""
    
    def __init__(self, datos_ventas):
        self.datos = datos_ventas
    
    def obtener_resumen(self):
        total = len(self.datos)
        return f"Reporte de {total} ventas"
    
    def obtener_contenido(self):
        contenido = "=== REPORTE DE VENTAS ===\n"
        for i, venta in enumerate(self.datos, 1):
            contenido += f"{i}. {venta}\n"
        return contenido

class GeneradorPDF:
    """SOLO se encarga de generar PDFs"""
    
    def generar(self, contenido, nombre_archivo):
        print(f"📄 Generando PDF: {nombre_archivo}")
        with open(nombre_archivo, "w") as f:
            f.write(contenido)
        print(f"✅ PDF generado: {nombre_archivo}")
        return nombre_archivo

class RepositorioReportes:
    """SOLO se encarga de guardar reportes en BD"""
    
    def __init__(self, conexion_bd):
        self.conexion = conexion_bd
    
    def guardar(self, reporte):
        print(f"💾 Guardando en BD: {self.conexion}")
        print(f"Guardando: {reporte.obtener_resumen()}")
        print("✅ Guardado en BD")
        return "guardado"

class NotificadorEmail:
    """SOLO se encarga de enviar emails"""
    
    def __init__(self, servidor_smtp):
        self.servidor = servidor_smtp
    
    def enviar(self, destinatario, asunto, mensaje, archivo_adjunto=None):
        print(f"📧 Enviando email via {self.servidor}")
        print(f"Para: {destinatario}")
        print(f"Asunto: {asunto}")
        if archivo_adjunto:
            print(f"Adjunto: {archivo_adjunto}")
        print("✅ Email enviado")
        return "enviado"

# Uso con SRP (mucho mejor):
print("=== USANDO SRP (BUENA PRÁCTICA) ===")

# Cada clase tiene una sola responsabilidad
reporte = ReporteVentas(ventas)
generador_pdf = GeneradorPDF()
repositorio = RepositorioReportes("mysql://localhost")
notificador = NotificadorEmail("smtp.empresa.com")

# Proceso paso a paso, cada clase hace lo suyo
contenido = reporte.obtener_contenido()
archivo_pdf = generador_pdf.generar(contenido, "ventas_2024.pdf")
repositorio.guardar(reporte)
notificador.enviar(
    "gerente@empresa.com",
    "Reporte de Ventas",
    "Adjunto el reporte solicitado",
    archivo_pdf
)
```

**Ventajas de aplicar SRP:**
- **Fácil de cambiar**: Cambiar PDF no afecta email ni BD
- **Fácil de testear**: Cada clase se prueba independientemente  
- **Reutilizable**: Puedes usar `GeneradorPDF` para otros reportes
- **Mantenible**: Bugs en una funcionalidad no afectan otras

---

## 4. Métodos cortos y responsabilidades únicas

* Un método debe hacer **una sola cosa** y hacerlo bien.
* Evitar métodos largos y complejos.

```python
# ❌ Mala práctica
def procesar_pedido(pedido):
    # valida
    # calcula total
    # guarda en BD
    # envía correo
    pass

# ✅ Buena práctica
def validar_pedido(pedido): pass
def calcular_total(pedido): pass
def guardar_pedido(pedido): pass
def notificar_pedido(pedido): pass
```

---

## 5. Antipatrones comunes

### 🔹 Clase Dios

Clase que hace de todo → difícil de mantener.

```python
# ❌ Ejemplo clase dios
class Sistema:
    def login(self): pass
    def registrar_usuario(self): pass
    def calcular_nomina(self): pass
    def procesar_factura(self): pass
```

### 🔹 Getters/Setters innecesarios

En Python se prefieren **propiedades** en lugar de abusar de getters/setters.

```python
# ❌ Mala práctica
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre

# ✅ Buena práctica (Pythonic)
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
```

---

## 📝 Mini-ejercicio

Refactoriza esta clase aplicando SRP y buenas prácticas:

```python
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    
    def guardar_en_bd(self): pass
    def enviar_email_bienvenida(self): pass
```

---

## ✅ Resumen del Módulo 3

* Usa **nombres claros** y expresivos.
* Mantén clases con **alta cohesión** y **bajo acoplamiento**.
* Aplica el **principio de responsabilidad única (SRP)**.
* Métodos cortos y enfocados en una tarea.
* Evita antipatrones como **clases dios** y **getters/setters innecesarios**.


