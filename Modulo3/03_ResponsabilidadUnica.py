## 🔹 EJEMPLO 3: PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)
# Una clase debe tener una sola razón para cambiar

print("=== PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP) ===\n")

# ❌ VIOLACIÓN DE SRP - Una clase con múltiples responsabilidades
print("❌ VIOLACIÓN DE SRP - Múltiples responsabilidades:")

class ReporteVentasCompleto:
    """Esta clase tiene MÚLTIPLES razones para cambiar - VIOLA SRP"""
    
    def __init__(self, datos_ventas):
        self.datos = datos_ventas
        self.conexion_bd = "mysql://localhost"
        self.servidor_email = "smtp.empresa.com"
        self.formato_pdf = "A4"
    
    def generar_pdf(self):
        """RESPONSABILIDAD 1: Generar PDF"""
        print("📄 Generando reporte PDF...")
        # Si cambia el formato PDF → hay que modificar ESTA clase
        contenido = f"=== REPORTE DE VENTAS ===\n"
        for i, venta in enumerate(self.datos, 1):
            contenido += f"{i}. {venta}\n"
        
        # Simulamos escribir archivo
        nombre_archivo = "reporte.pdf"
        print(f"✅ PDF generado: {nombre_archivo}")
        return nombre_archivo
    
    def guardar_en_bd(self):
        """RESPONSABILIDAD 2: Guardar en base de datos"""
        print("💾 Guardando en base de datos...")
        # Si cambia la BD → hay que modificar ESTA clase
        print(f"Conectando a {self.conexion_bd}")
        for venta in self.datos:
            print(f"INSERT INTO reportes VALUES ('{venta}')")
        print("✅ Guardado en BD")
        return "guardado"
    
    def enviar_email(self, destinatario):
        """RESPONSABILIDAD 3: Enviar por email"""
        print("📧 Enviando por email...")
        # Si cambia el servidor de email → hay que modificar ESTA clase
        print(f"Servidor: {self.servidor_email}")
        print(f"Para: {destinatario}")
        print(f"Asunto: Reporte de Ventas")
        print("✅ Email enviado")
        return "enviado"
    
    def validar_datos(self):
        """RESPONSABILIDAD 4: Validar datos"""
        print("🔍 Validando datos...")
        # Si cambian las reglas de validación → hay que modificar ESTA clase
        for venta in self.datos:
            if not venta or len(venta) < 5:
                print(f"❌ Venta inválida: {venta}")
                return False
        print("✅ Datos válidos")
        return True
    
    def procesar_completo(self, destinatario):
        """Hace todo junto - MUY FRÁGIL"""
        if not self.validar_datos():
            return None
        
        pdf = self.generar_pdf()
        self.guardar_en_bd()
        self.enviar_email(destinatario)
        return pdf

# Problemas de usar esta clase:
print("Problemas del enfoque que viola SRP:")
ventas = ["Venta 1: 100€", "Venta 2: 200€", "Venta 3: 150€"]
reporte_malo = ReporteVentasCompleto(ventas)

# Si cualquier cosa cambia, toda la clase se ve afectada
resultado = reporte_malo.procesar_completo("gerente@empresa.com")
print(f"Resultado: {resultado}")

print("\n" + "="*60 + "\n")

# ✅ APLICANDO SRP - Cada clase tiene una sola responsabilidad
print("✅ APLICANDO SRP - Una responsabilidad por clase:")

class ReporteVentas:
    """SOLO se encarga de los datos del reporte"""
    
    def __init__(self, datos_ventas):
        self.datos = datos_ventas
        self.fecha_creacion = "2024-01-15"
    
    def obtener_resumen(self):
        total_ventas = len(self.datos)
        return f"Reporte de {total_ventas} ventas del {self.fecha_creacion}"
    
    def obtener_contenido(self):
        contenido = "=== REPORTE DE VENTAS ===\n"
        contenido += f"Fecha: {self.fecha_creacion}\n\n"
        for i, venta in enumerate(self.datos, 1):
            contenido += f"{i}. {venta}\n"
        return contenido
    
    def obtener_datos(self):
        return self.datos.copy()

class ValidadorReportes:
    """SOLO se encarga de validar datos de reportes"""
    
    def __init__(self):
        self.reglas_validacion = {
            "longitud_minima": 5,
            "campos_obligatorios": ["€"]
        }
    
    def validar_venta(self, venta):
        if not venta or len(venta) < self.reglas_validacion["longitud_minima"]:
            return False, f"Venta muy corta: {venta}"
        
        if "€" not in venta:
            return False, f"Falta símbolo de moneda: {venta}"
        
        return True, "Válida"
    
    def validar_reporte(self, reporte):
        print("🔍 Validando datos del reporte...")
        datos = reporte.obtener_datos()
        
        for venta in datos:
            es_valida, mensaje = self.validar_venta(venta)
            if not es_valida:
                print(f"❌ {mensaje}")
                return False
        
        print("✅ Todos los datos son válidos")
        return True

class GeneradorPDF:
    """SOLO se encarga de generar PDFs"""
    
    def __init__(self, formato="A4"):
        self.formato = formato
        self.configuracion = {
            "fuente": "Arial",
            "tamaño": 12,
            "margenes": "2cm"
        }
    
    def configurar(self, **opciones):
        self.configuracion.update(opciones)
    
    def generar(self, contenido, nombre_archivo):
        print(f"📄 Generando PDF: {nombre_archivo}")
        print(f"   Formato: {self.formato}")
        print(f"   Configuración: {self.configuracion}")
        
        # Simulamos la generación del PDF
        print(f"✅ PDF generado: {nombre_archivo}")
        return nombre_archivo

class RepositorioReportes:
    """SOLO se encarga de guardar reportes en BD"""
    
    def __init__(self, conexion_bd):
        self.conexion = conexion_bd
        self.tabla = "reportes"
    
    def guardar(self, reporte):
        print(f"💾 Guardando en BD: {self.conexion}")
        print(f"   Tabla: {self.tabla}")
        print(f"   Datos: {reporte.obtener_resumen()}")
        
        # Simulamos la inserción en BD
        datos = reporte.obtener_datos()
        for venta in datos:
            print(f"   INSERT INTO {self.tabla} VALUES ('{venta}')")
        
        print("✅ Guardado en BD")
        return {"id": "12345", "status": "guardado"}
    
    def existe_reporte(self, fecha):
        print(f"🔍 Verificando si existe reporte del {fecha}")
        return False  # Simulado

class NotificadorEmail:
    """SOLO se encarga de enviar emails"""
    
    def __init__(self, servidor_smtp):
        self.servidor = servidor_smtp
        self.configuracion = {
            "puerto": 587,
            "ssl": True
        }
    
    def configurar_servidor(self, puerto=587, ssl=True):
        self.configuracion["puerto"] = puerto
        self.configuracion["ssl"] = ssl
    
    def enviar(self, destinatario, asunto, mensaje, archivo_adjunto=None):
        print(f"📧 Enviando email via {self.servidor}")
        print(f"   Puerto: {self.configuracion['puerto']}")
        print(f"   SSL: {self.configuracion['ssl']}")
        print(f"   Para: {destinatario}")
        print(f"   Asunto: {asunto}")
        if archivo_adjunto:
            print(f"   Adjunto: {archivo_adjunto}")
        print("✅ Email enviado")
        return {"status": "enviado", "id": "email_12345"}
    
    def enviar_reporte(self, destinatario, reporte, archivo_pdf):
        return self.enviar(
            destinatario,
            f"Reporte: {reporte.obtener_resumen()}",
            "Se adjunta el reporte solicitado.",
            archivo_pdf
        )

# Uso con SRP (mucho mejor):
print("Usando SRP - cada clase tiene una responsabilidad:")

# Crear instancias - cada una con su responsabilidad específica
reporte = ReporteVentas(ventas)
validador = ValidadorReportes()
generador_pdf = GeneradorPDF()
repositorio = RepositorioReportes("mysql://localhost")
notificador = NotificadorEmail("smtp.empresa.com")

# Configuraciones específicas
generador_pdf.configurar(fuente="Times New Roman", tamaño=14)
notificador.configurar_servidor(puerto=465, ssl=True)

# Proceso paso a paso - cada clase hace lo suyo
print("\n🔄 Ejecutando proceso paso a paso:")

# 1. Validar
if validador.validar_reporte(reporte):
    # 2. Generar PDF
    contenido = reporte.obtener_contenido()
    archivo_pdf = generador_pdf.generar(contenido, "ventas_2024.pdf")
    
    # 3. Guardar en BD
    resultado_bd = repositorio.guardar(reporte)
    
    # 4. Enviar email
    resultado_email = notificador.enviar_reporte(
        "gerente@empresa.com",
        reporte,
        archivo_pdf
    )
    
    print(f"\n✅ Proceso completado exitosamente")
    print(f"   BD: {resultado_bd['status']}")
    print(f"   Email: {resultado_email['status']}")

print("\n=== VENTAJAS DE APLICAR SRP ===")
print("✅ Fácil de cambiar: Cambiar PDF no afecta email ni BD")
print("✅ Fácil de testear: Cada clase se prueba independientemente")
print("✅ Reutilizable: GeneradorPDF sirve para otros reportes")
print("✅ Mantenible: Bugs en una parte no afectan otras")
print("✅ Extensible: Fácil agregar nuevas funcionalidades")

print("\n=== CÓMO IDENTIFICAR VIOLACIONES DE SRP ===")
print("❌ La clase tiene muchos métodos diferentes")
print("❌ Los métodos no están relacionados entre sí")
print("❌ Cambios en una funcionalidad afectan otras")
print("❌ La clase es difícil de testear")
print("❌ El nombre de la clase es vago o muy general")
