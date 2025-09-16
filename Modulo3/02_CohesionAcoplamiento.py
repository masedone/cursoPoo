## 🔹 EJEMPLO 2: COHESIÓN Y ACOPLAMIENTO
# Comparación entre alta/baja cohesión y alto/bajo acoplamiento

print("=== COHESIÓN Y ACOPLAMIENTO ===\n")

# ❌ MALA PRÁCTICA - Baja cohesión y alto acoplamiento
print("❌ MALA PRÁCTICA - Baja cohesión y alto acoplamiento:")

class GestorTodoEnUno:
    """Clase que hace DEMASIADAS cosas diferentes (baja cohesión)"""
    
    def __init__(self):
        self.conexion_bd = "mysql://localhost"
        self.servidor_email = "smtp.gmail.com"
        self.empleados = []
        self.reportes = []
    
    def conectar_bd(self):
        """Responsabilidad 1: Base de datos"""
        print(f"🔌 Conectando a {self.conexion_bd}")
        return "conectado"
    
    def calcular_nomina(self, empleado_id):
        """Responsabilidad 2: Cálculos de nómina"""
        # ¿Por qué una clase de BD calcula nóminas?
        salario_base = 1000
        bonos = 200
        total = salario_base + bonos
        print(f"💰 Calculando nómina para empleado {empleado_id}: {total}€")
        return total
    
    def enviar_email(self, destinatario, mensaje):
        """Responsabilidad 3: Comunicaciones"""
        # ¿Por qué una clase de nóminas envía emails?
        print(f"📧 Enviando email a {destinatario}: {mensaje}")
        return "enviado"
    
    def generar_reporte_pdf(self, tipo):
        """Responsabilidad 4: Generación de documentos"""
        # ¿Por qué una clase de email genera PDFs?
        print(f"📄 Generando reporte PDF: {tipo}")
        return f"reporte_{tipo}.pdf"
    
    def validar_usuario(self, usuario, password):
        """Responsabilidad 5: Autenticación"""
        # ¿Por qué una clase de reportes valida usuarios?
        print(f"🔐 Validando usuario: {usuario}")
        return usuario == "admin" and password == "123"

# Usar esta clase es confuso y frágil:
print("Usando GestorTodoEnUno (problemático):")
gestor = GestorTodoEnUno()
gestor.conectar_bd()                    # ¿Para qué se conecta?
gestor.calcular_nomina(123)             # ¿Necesita BD para esto?
gestor.enviar_email("juan@email.com", "Hola")  # ¿Y esto para qué?
gestor.generar_reporte_pdf("ventas")    # ¿Cómo se relaciona con lo anterior?
gestor.validar_usuario("admin", "123") # ¿Por qué aquí?

print("\n" + "="*60 + "\n")

# ✅ BUENA PRÁCTICA - Alta cohesión y bajo acoplamiento
print("✅ BUENA PRÁCTICA - Alta cohesión y bajo acoplamiento:")

class ConexionBD:
    """ALTA COHESIÓN: Solo se encarga de la conexión a base de datos"""
    
    def __init__(self, url_conexion):
        self.url_conexion = url_conexion
        self.conectado = False
    
    def conectar(self):
        print(f"🔌 Conectando a {self.url_conexion}")
        self.conectado = True
        return self
    
    def desconectar(self):
        print("🔌 Desconectando de la base de datos")
        self.conectado = False
    
    def ejecutar_consulta(self, sql):
        if not self.conectado:
            raise Exception("Debe conectar primero")
        print(f"🔍 Ejecutando: {sql}")
        return ["resultado1", "resultado2"]
    
    def esta_conectado(self):
        return self.conectado

class CalculadoraNomina:
    """ALTA COHESIÓN: Solo se encarga de cálculos de nómina"""
    
    def __init__(self, bd):
        self.bd = bd  # BAJO ACOPLAMIENTO: Recibe la dependencia, no la crea
    
    def calcular_salario_base(self, empleado_id):
        datos = self.bd.ejecutar_consulta(f"SELECT salario FROM empleados WHERE id={empleado_id}")
        return 1000  # Simulado
    
    def calcular_bonos(self, empleado_id):
        datos = self.bd.ejecutar_consulta(f"SELECT bonos FROM empleados WHERE id={empleado_id}")
        return 200   # Simulado
    
    def calcular_salario_total(self, empleado_id):
        salario_base = self.calcular_salario_base(empleado_id)
        bonos = self.calcular_bonos(empleado_id)
        total = salario_base + bonos
        print(f"💰 Salario total para {empleado_id}: {total}€")
        return total

class ServicioEmail:
    """ALTA COHESIÓN: Solo se encarga de enviar emails"""
    
    def __init__(self, servidor_smtp):
        self.servidor = servidor_smtp
        self.configurado = False
    
    def configurar(self, usuario, password):
        print(f"⚙️ Configurando email con servidor: {self.servidor}")
        self.configurado = True
    
    def enviar(self, destinatario, asunto, mensaje):
        if not self.configurado:
            raise Exception("Email no configurado")
        print(f"📧 Enviando email a {destinatario}")
        print(f"   📋 Asunto: {asunto}")
        print(f"   💬 Mensaje: {mensaje}")
        return {"status": "enviado", "id": "12345"}
    
    def enviar_nomina(self, empleado_email, salario):
        return self.enviar(
            empleado_email,
            "Tu nómina mensual",
            f"Tu salario este mes es: {salario}€"
        )

class GeneradorReportes:
    """ALTA COHESIÓN: Solo se encarga de generar reportes"""
    
    def __init__(self):
        self.formato_default = "PDF"
    
    def generar_pdf(self, titulo, contenido):
        print(f"📄 Generando PDF: {titulo}")
        nombre_archivo = f"{titulo.lower().replace(' ', '_')}.pdf"
        print(f"✅ PDF generado: {nombre_archivo}")
        return nombre_archivo
    
    def generar_excel(self, titulo, datos):
        print(f"📊 Generando Excel: {titulo}")
        nombre_archivo = f"{titulo.lower().replace(' ', '_')}.xlsx"
        print(f"✅ Excel generado: {nombre_archivo}")
        return nombre_archivo

class ValidadorUsuarios:
    """ALTA COHESIÓN: Solo se encarga de autenticación"""
    
    def __init__(self, bd):
        self.bd = bd  # BAJO ACOPLAMIENTO: Inyección de dependencia
    
    def validar_credenciales(self, usuario, password):
        print(f"🔐 Validando usuario: {usuario}")
        # Consulta a BD para verificar credenciales
        datos = self.bd.ejecutar_consulta(f"SELECT * FROM usuarios WHERE user='{usuario}'")
        # Simulación de validación
        return usuario == "admin" and password == "123"
    
    def usuario_tiene_permisos(self, usuario, permiso):
        print(f"🛡️ Verificando permisos de {usuario} para: {permiso}")
        return True  # Simulado

# Uso con buenas prácticas (más claro y mantenible):
print("Usando clases cohesionadas y bajo acoplamiento:")

# BAJO ACOPLAMIENTO: Cada clase se crea independientemente
bd = ConexionBD("mysql://localhost").conectar()
calculadora = CalculadoraNomina(bd)  # Recibe BD como dependencia
email_service = ServicioEmail("smtp.empresa.com")
generador = GeneradorReportes()
validador = ValidadorUsuarios(bd)  # Recibe BD como dependencia

# Configuración
email_service.configurar("admin", "password123")

# Uso coordinado pero independiente
if validador.validar_credenciales("admin", "123"):
    salario = calculadora.calcular_salario_total(123)
    email_service.enviar_nomina("empleado@empresa.com", salario)
    reporte = generador.generar_pdf("Reporte Nominas", "Contenido del reporte")
    print(f"✅ Proceso completado. Reporte: {reporte}")

# Limpieza
bd.desconectar()

print("\n=== VENTAJAS DE ALTA COHESIÓN Y BAJO ACOPLAMIENTO ===")
print("✅ Fácil de testear: Cada clase se prueba independientemente")
print("✅ Fácil de mantener: Cambios en BD no afectan email")
print("✅ Reutilizable: ServicioEmail se puede usar en otros lugares")
print("✅ Flexible: Fácil cambiar implementaciones")
print("✅ Claro: Cada clase tiene un propósito obvio")

print("\n=== DEFINICIONES ===")
print("🔸 COHESIÓN ALTA: Todo en la clase está relacionado")
print("🔸 ACOPLAMIENTO BAJO: Pocas dependencias entre clases")
print("🔸 INYECCIÓN DE DEPENDENCIAS: Recibir lo que necesitas, no crearlo")
