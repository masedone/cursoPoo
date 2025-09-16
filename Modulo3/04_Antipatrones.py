## 🔹 EJEMPLO 4: ANTIPATRONES COMUNES
# Patrones de diseño que debes evitar

print("=== ANTIPATRONES COMUNES EN POO ===\n")

# 🔸 ANTIPATRÓN 1: CLASE DIOS
print("❌ ANTIPATRÓN 1: CLASE DIOS")
print("Una clase que hace de todo → difícil de mantener\n")

class SistemaDios:
    """ANTIPATRÓN: Clase que controla todo el sistema"""
    
    def __init__(self):
        self.usuarios = {}
        self.productos = {}
        self.pedidos = {}
        self.conexion_bd = "mysql://localhost"
        self.servidor_email = "smtp.empresa.com"
        self.configuracion = {}
    
    # Gestión de usuarios
    def registrar_usuario(self, nombre, email, password):
        print(f"👤 Registrando usuario: {nombre}")
        self.usuarios[email] = {"nombre": nombre, "password": password}
        return True
    
    def login(self, email, password):
        print(f"🔐 Login usuario: {email}")
        usuario = self.usuarios.get(email)
        return usuario and usuario["password"] == password
    
    def logout(self, email):
        print(f"👋 Logout usuario: {email}")
        return True
    
    # Gestión de productos
    def agregar_producto(self, id_producto, nombre, precio):
        print(f"📦 Agregando producto: {nombre}")
        self.productos[id_producto] = {"nombre": nombre, "precio": precio}
        return True
    
    def calcular_precio_con_iva(self, id_producto):
        producto = self.productos.get(id_producto)
        if producto:
            return producto["precio"] * 1.21
        return 0
    
    # Gestión de pedidos
    def crear_pedido(self, usuario_email, productos_ids):
        print(f"🛒 Creando pedido para: {usuario_email}")
        pedido_id = len(self.pedidos) + 1
        self.pedidos[pedido_id] = {
            "usuario": usuario_email,
            "productos": productos_ids,
            "estado": "pendiente"
        }
        return pedido_id
    
    def procesar_pago(self, pedido_id, tarjeta):
        print(f"💳 Procesando pago para pedido: {pedido_id}")
        # Lógica de pago
        return True
    
    # Base de datos
    def conectar_bd(self):
        print(f"🔌 Conectando a BD: {self.conexion_bd}")
        return True
    
    def guardar_en_bd(self, tabla, datos):
        print(f"💾 Guardando en tabla {tabla}: {datos}")
        return True
    
    # Emails
    def enviar_email_bienvenida(self, email):
        print(f"📧 Enviando email de bienvenida a: {email}")
        return True
    
    def enviar_confirmacion_pedido(self, email, pedido_id):
        print(f"📧 Enviando confirmación de pedido {pedido_id} a: {email}")
        return True
    
    # Reportes
    def generar_reporte_ventas(self):
        print("📊 Generando reporte de ventas")
        return "reporte_ventas.pdf"
    
    def generar_reporte_usuarios(self):
        print("📊 Generando reporte de usuarios")
        return "reporte_usuarios.pdf"
    
    # Configuración
    def configurar_sistema(self, clave, valor):
        print(f"⚙️ Configurando {clave}: {valor}")
        self.configuracion[clave] = valor

# Uso problemático de la clase dios
print("Usando la clase dios (problemático):")
sistema = SistemaDios()
sistema.registrar_usuario("Juan", "juan@email.com", "123")
sistema.agregar_producto(1, "Laptop", 500)
sistema.crear_pedido("juan@email.com", [1])
sistema.generar_reporte_ventas()

print("\n" + "="*60 + "\n")

# 🔸 ANTIPATRÓN 2: GETTERS/SETTERS INNECESARIOS
print("❌ ANTIPATRÓN 2: GETTERS/SETTERS INNECESARIOS")
print("Abusar de get/set en lugar de usar propiedades\n")

class PersonaMalasPracticas:
    """ANTIPATRÓN: Getters/setters innecesarios"""
    
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        self._email = ""
    
    # Getters innecesarios
    def get_nombre(self):
        return self._nombre
    
    def get_edad(self):
        return self._edad
    
    def get_email(self):
        return self._email
    
    # Setters innecesarios
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_edad(self, edad):
        self._edad = edad
    
    def set_email(self, email):
        self._email = email

# ✅ BUENA PRÁCTICA: Usar propiedades de Python
class PersonaBuenasPracticas:
    """BUENA PRÁCTICA: Propiedades pythónicas"""
    
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        self._email = ""
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor or len(valor) < 2:
            raise ValueError("Nombre debe tener al menos 2 caracteres")
        self._nombre = valor
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, valor):
        if valor < 0 or valor > 150:
            raise ValueError("Edad debe estar entre 0 y 150")
        self._edad = valor
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        if valor and "@" not in valor:
            raise ValueError("Email debe contener @")
        self._email = valor
    
    def es_mayor_de_edad(self):
        return self._edad >= 18

# Comparación
print("❌ Con getters/setters innecesarios:")
persona_mala = PersonaMalasPracticas("Ana", 25)
print(f"Nombre: {persona_mala.get_nombre()}")
persona_mala.set_edad(26)
print(f"Nueva edad: {persona_mala.get_edad()}")

print("\n✅ Con propiedades pythónicas:")
persona_buena = PersonaBuenasPracticas("Ana", 25)
print(f"Nombre: {persona_buena.nombre}")  # Como atributo
persona_buena.edad = 26  # Con validación automática
print(f"Nueva edad: {persona_buena.edad}")
print(f"¿Es mayor de edad? {persona_buena.es_mayor_de_edad()}")

print("\n" + "="*60 + "\n")

# 🔸 ANTIPATRÓN 3: CÓDIGO DUPLICADO
print("❌ ANTIPATRÓN 3: CÓDIGO DUPLICADO")
print("Repetir la misma lógica en múltiples lugares\n")

class CalculadoraImpuestosDuplicada:
    """ANTIPATRÓN: Código duplicado"""
    
    def calcular_precio_producto_a(self, precio):
        # Lógica duplicada
        iva = precio * 0.21
        descuento = precio * 0.10 if precio > 100 else 0
        precio_final = precio + iva - descuento
        print(f"Producto A: {precio_final}")
        return precio_final
    
    def calcular_precio_producto_b(self, precio):
        # Misma lógica duplicada
        iva = precio * 0.21
        descuento = precio * 0.10 if precio > 100 else 0
        precio_final = precio + iva - descuento
        print(f"Producto B: {precio_final}")
        return precio_final
    
    def calcular_precio_producto_c(self, precio):
        # Otra vez la misma lógica
        iva = precio * 0.21
        descuento = precio * 0.10 if precio > 100 else 0
        precio_final = precio + iva - descuento
        print(f"Producto C: {precio_final}")
        return precio_final

# ✅ BUENA PRÁCTICA: Eliminar duplicación
class CalculadoraImpuestosMejorada:
    """BUENA PRÁCTICA: Sin duplicación"""
    
    def __init__(self):
        self.iva_porcentaje = 0.21
        self.descuento_porcentaje = 0.10
        self.minimo_para_descuento = 100
    
    def calcular_iva(self, precio):
        return precio * self.iva_porcentaje
    
    def calcular_descuento(self, precio):
        return precio * self.descuento_porcentaje if precio > self.minimo_para_descuento else 0
    
    def calcular_precio_final(self, precio, nombre_producto):
        iva = self.calcular_iva(precio)
        descuento = self.calcular_descuento(precio)
        precio_final = precio + iva - descuento
        print(f"{nombre_producto}: {precio_final:.2f}€")
        return precio_final
    
    def calcular_precio_producto_a(self, precio):
        return self.calcular_precio_final(precio, "Producto A")
    
    def calcular_precio_producto_b(self, precio):
        return self.calcular_precio_final(precio, "Producto B")
    
    def calcular_precio_producto_c(self, precio):
        return self.calcular_precio_final(precio, "Producto C")

print("❌ Con código duplicado:")
calc_mala = CalculadoraImpuestosDuplicada()
calc_mala.calcular_precio_producto_a(150)
calc_mala.calcular_precio_producto_b(80)

print("\n✅ Sin duplicación:")
calc_buena = CalculadoraImpuestosMejorada()
calc_buena.calcular_precio_producto_a(150)
calc_buena.calcular_precio_producto_b(80)
calc_buena.calcular_precio_producto_c(200)

print("\n" + "="*60 + "\n")

# 🔸 ANTIPATRÓN 4: MÉTODOS DEMASIADO LARGOS
print("❌ ANTIPATRÓN 4: MÉTODOS DEMASIADO LARGOS")
print("Métodos que hacen demasiadas cosas\n")

class ProcesadorPedidoMalo:
    """ANTIPATRÓN: Método muy largo"""
    
    def procesar_pedido_completo(self, pedido_data):
        """Método que hace DEMASIADAS cosas"""
        print("🔄 Procesando pedido completo...")
        
        # Validación (debería ser método separado)
        if not pedido_data.get("usuario"):
            print("❌ Error: falta usuario")
            return False
        if not pedido_data.get("productos"):
            print("❌ Error: falta productos")
            return False
        
        # Cálculo de precios (debería ser método separado)
        total = 0
        for producto in pedido_data["productos"]:
            precio = producto.get("precio", 0)
            cantidad = producto.get("cantidad", 1)
            iva = precio * 0.21
            subtotal = (precio + iva) * cantidad
            total += subtotal
            print(f"  {producto['nombre']}: {subtotal}€")
        
        # Aplicar descuentos (debería ser método separado)
        if total > 100:
            descuento = total * 0.10
            total -= descuento
            print(f"  Descuento aplicado: -{descuento}€")
        
        # Procesar pago (debería ser método separado)
        tarjeta = pedido_data.get("tarjeta")
        if not tarjeta:
            print("❌ Error: falta información de tarjeta")
            return False
        print(f"💳 Procesando pago: {total}€")
        
        # Guardar en BD (debería ser método separado)
        print("💾 Guardando pedido en base de datos...")
        
        # Enviar confirmación (debería ser método separado)
        email = pedido_data["usuario"]["email"]
        print(f"📧 Enviando confirmación a: {email}")
        
        # Actualizar inventario (debería ser método separado)
        for producto in pedido_data["productos"]:
            print(f"📦 Actualizando inventario: {producto['nombre']}")
        
        print("✅ Pedido procesado exitosamente")
        return True

# ✅ BUENA PRÁCTICA: Métodos cortos y específicos
class ProcesadorPedidoBueno:
    """BUENA PRÁCTICA: Métodos cortos y específicos"""
    
    def validar_pedido(self, pedido_data):
        if not pedido_data.get("usuario"):
            return False, "Falta usuario"
        if not pedido_data.get("productos"):
            return False, "Falta productos"
        if not pedido_data.get("tarjeta"):
            return False, "Falta información de tarjeta"
        return True, "Válido"
    
    def calcular_subtotal_producto(self, producto):
        precio = producto.get("precio", 0)
        cantidad = producto.get("cantidad", 1)
        iva = precio * 0.21
        return (precio + iva) * cantidad
    
    def calcular_total(self, productos):
        total = 0
        for producto in productos:
            subtotal = self.calcular_subtotal_producto(producto)
            total += subtotal
            print(f"  {producto['nombre']}: {subtotal}€")
        return total
    
    def aplicar_descuentos(self, total):
        if total > 100:
            descuento = total * 0.10
            total_con_descuento = total - descuento
            print(f"  Descuento aplicado: -{descuento}€")
            return total_con_descuento
        return total
    
    def procesar_pago(self, total, tarjeta):
        print(f"💳 Procesando pago: {total}€")
        # Lógica de pago
        return True
    
    def guardar_pedido(self, pedido_data, total):
        print("💾 Guardando pedido en base de datos...")
        return {"id": 12345, "total": total}
    
    def enviar_confirmacion(self, email, pedido_id):
        print(f"📧 Enviando confirmación a: {email}")
        return True
    
    def actualizar_inventario(self, productos):
        for producto in productos:
            print(f"📦 Actualizando inventario: {producto['nombre']}")
        return True
    
    def procesar_pedido_completo(self, pedido_data):
        """Método coordinador que usa métodos específicos"""
        print("🔄 Procesando pedido completo...")
        
        # 1. Validar
        es_valido, mensaje = self.validar_pedido(pedido_data)
        if not es_valido:
            print(f"❌ Error: {mensaje}")
            return False
        
        # 2. Calcular total
        total = self.calcular_total(pedido_data["productos"])
        total = self.aplicar_descuentos(total)
        
        # 3. Procesar pago
        if not self.procesar_pago(total, pedido_data["tarjeta"]):
            return False
        
        # 4. Guardar
        pedido = self.guardar_pedido(pedido_data, total)
        
        # 5. Notificar
        self.enviar_confirmacion(pedido_data["usuario"]["email"], pedido["id"])
        
        # 6. Actualizar inventario
        self.actualizar_inventario(pedido_data["productos"])
        
        print("✅ Pedido procesado exitosamente")
        return True

# Datos de ejemplo
pedido_ejemplo = {
    "usuario": {"email": "cliente@email.com"},
    "productos": [
        {"nombre": "Laptop", "precio": 500, "cantidad": 1},
        {"nombre": "Mouse", "precio": 25, "cantidad": 2}
    ],
    "tarjeta": {"numero": "1234-5678-9012-3456"}
}

print("❌ Con método muy largo:")
procesador_malo = ProcesadorPedidoMalo()
procesador_malo.procesar_pedido_completo(pedido_ejemplo)

print("\n✅ Con métodos cortos y específicos:")
procesador_bueno = ProcesadorPedidoBueno()
procesador_bueno.procesar_pedido_completo(pedido_ejemplo)

print("\n=== RESUMEN DE ANTIPATRONES ===")
print("❌ Clase Dios: Una clase que hace de todo")
print("❌ Getters/Setters innecesarios: Abusar de get/set")
print("❌ Código duplicado: Repetir la misma lógica")
print("❌ Métodos largos: Métodos que hacen demasiado")

print("\n=== CÓMO EVITAR ANTIPATRONES ===")
print("✅ Aplicar SRP: Una responsabilidad por clase")
print("✅ Usar propiedades de Python en lugar de get/set")
print("✅ Extraer lógica común a métodos reutilizables")
print("✅ Dividir métodos largos en métodos específicos")
print("✅ Refactorizar regularmente el código")
