## 🔹 PRINCIPIO SOLID 5: DEPENDENCY INVERSION PRINCIPLE (DIP)
# "Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones"

print("=== PRINCIPIO DIP - INVERSIÓN DE DEPENDENCIAS ===\n")

from abc import ABC, abstractmethod

# ❌ VIOLACIÓN DE DIP - Dependencia directa de implementaciones concretas
print("❌ VIOLACIÓN DE DIP - Dependencias directas:")

class BaseDatosMySQL:
    """Implementación concreta de base de datos"""
    
    def __init__(self):
        self.conexion = "mysql://localhost:3306/tienda"
    
    def conectar(self):
        print(f"🔌 Conectando a MySQL: {self.conexion}")
        return True
    
    def guardar_usuario(self, usuario):
        print(f"💾 MySQL: Guardando usuario {usuario['nombre']} en tabla usuarios")
        return {"id": 123, "status": "guardado"}
    
    def buscar_usuario(self, email):
        print(f"🔍 MySQL: Buscando usuario con email {email}")
        return {"id": 123, "nombre": "Juan", "email": email}

class ServicioEmailGmail:
    """Implementación concreta de servicio de email"""
    
    def __init__(self):
        self.servidor = "smtp.gmail.com"
        self.puerto = 587
    
    def configurar(self, usuario, password):
        print(f"⚙️ Configurando Gmail: {usuario}@gmail.com")
        return True
    
    def enviar(self, destinatario, asunto, mensaje):
        print(f"📧 Gmail: Enviando email a {destinatario}")
        print(f"   Asunto: {asunto}")
        return {"status": "enviado", "id": "gmail_123"}

class LoggerArchivo:
    """Implementación concreta de logging"""
    
    def __init__(self):
        self.archivo = "app.log"
    
    def log(self, nivel, mensaje):
        print(f"📝 Archivo: [{nivel}] {mensaje} → {self.archivo}")

class GestorUsuariosMalo:
    """VIOLA DIP: Depende directamente de implementaciones concretas"""
    
    def __init__(self):
        # ❌ PROBLEMA: Crea dependencias concretas directamente
        self.bd = BaseDatosMySQL()          # Dependencia directa
        self.email = ServicioEmailGmail()   # Dependencia directa
        self.logger = LoggerArchivo()       # Dependencia directa
    
    def registrar_usuario(self, nombre, email, password):
        """Método que está fuertemente acoplado a implementaciones específicas"""
        print(f"🔄 Registrando usuario: {nombre}")
        
        # Configurar servicios (acoplamiento fuerte)
        self.bd.conectar()
        self.email.configurar("app", "password123")
        
        # Usar servicios específicos
        usuario = {"nombre": nombre, "email": email, "password": password}
        
        try:
            # Guardar en BD específica
            resultado = self.bd.guardar_usuario(usuario)
            self.logger.log("INFO", f"Usuario {nombre} guardado con ID {resultado['id']}")
            
            # Enviar email con servicio específico
            email_resultado = self.email.enviar(
                email, 
                "Bienvenido", 
                f"Hola {nombre}, bienvenido a nuestra plataforma"
            )
            self.logger.log("INFO", f"Email enviado: {email_resultado['id']}")
            
            return True
            
        except Exception as e:
            self.logger.log("ERROR", f"Error registrando usuario: {e}")
            return False

# Uso problemático que viola DIP
print("Usando gestor que viola DIP:")
gestor_malo = GestorUsuariosMalo()
gestor_malo.registrar_usuario("Ana García", "ana@email.com", "password123")

# PROBLEMAS:
# 1. Si queremos cambiar de MySQL a PostgreSQL → hay que modificar GestorUsuariosMalo
# 2. Si queremos cambiar de Gmail a SendGrid → hay que modificar GestorUsuariosMalo
# 3. Si queremos logging a consola → hay que modificar GestorUsuariosMalo
# 4. Difícil de testear porque depende de servicios reales
# 5. Código rígido y poco flexible

print("\n" + "="*70 + "\n")

# ✅ APLICANDO DIP - Dependencia de abstracciones
print("✅ APLICANDO DIP - Dependencia de abstracciones:")

# 1. Definir abstracciones (interfaces)
class IBaseDatos(ABC):
    """Abstracción para base de datos"""
    
    @abstractmethod
    def conectar(self):
        pass
    
    @abstractmethod
    def guardar_usuario(self, usuario):
        pass
    
    @abstractmethod
    def buscar_usuario(self, email):
        pass
    
    @abstractmethod
    def desconectar(self):
        pass

class IServicioEmail(ABC):
    """Abstracción para servicio de email"""
    
    @abstractmethod
    def configurar(self, configuracion):
        pass
    
    @abstractmethod
    def enviar(self, destinatario, asunto, mensaje):
        pass

class ILogger(ABC):
    """Abstracción para logging"""
    
    @abstractmethod
    def log(self, nivel, mensaje):
        pass
    
    @abstractmethod
    def log_error(self, mensaje, excepcion=None):
        pass

# 2. Implementaciones concretas que implementan las abstracciones
class BaseDatosMySQLDIP(IBaseDatos):
    """Implementación MySQL que cumple DIP"""
    
    def __init__(self, host="localhost", puerto=3306, bd="tienda"):
        self.host = host
        self.puerto = puerto
        self.bd = bd
        self.conectado = False
    
    def conectar(self):
        print(f"🔌 MySQL: Conectando a {self.host}:{self.puerto}/{self.bd}")
        self.conectado = True
        return True
    
    def guardar_usuario(self, usuario):
        if not self.conectado:
            raise Exception("Base de datos no conectada")
        print(f"💾 MySQL: INSERT INTO usuarios VALUES ('{usuario['nombre']}', '{usuario['email']}')")
        return {"id": 456, "status": "guardado", "bd": "mysql"}
    
    def buscar_usuario(self, email):
        print(f"🔍 MySQL: SELECT * FROM usuarios WHERE email = '{email}'")
        return {"id": 456, "nombre": "Usuario", "email": email}
    
    def desconectar(self):
        print("🔌 MySQL: Desconectando")
        self.conectado = False

class BaseDatosPostgreSQL(IBaseDatos):
    """Implementación PostgreSQL - NUEVA sin modificar código existente"""
    
    def __init__(self, host="localhost", puerto=5432, bd="tienda"):
        self.host = host
        self.puerto = puerto
        self.bd = bd
        self.conectado = False
    
    def conectar(self):
        print(f"🔌 PostgreSQL: Conectando a {self.host}:{self.puerto}/{self.bd}")
        self.conectado = True
        return True
    
    def guardar_usuario(self, usuario):
        if not self.conectado:
            raise Exception("Base de datos no conectada")
        print(f"💾 PostgreSQL: INSERT INTO usuarios (nombre, email) VALUES ('{usuario['nombre']}', '{usuario['email']}')")
        return {"id": 789, "status": "guardado", "bd": "postgresql"}
    
    def buscar_usuario(self, email):
        print(f"🔍 PostgreSQL: SELECT * FROM usuarios WHERE email = '{email}'")
        return {"id": 789, "nombre": "Usuario", "email": email}
    
    def desconectar(self):
        print("🔌 PostgreSQL: Desconectando")
        self.conectado = False

class ServicioEmailSendGrid(IServicioEmail):
    """Implementación SendGrid que cumple DIP"""
    
    def __init__(self):
        self.api_key = None
        self.configurado = False
    
    def configurar(self, configuracion):
        self.api_key = configuracion.get("api_key")
        print(f"⚙️ SendGrid: Configurado con API key: {self.api_key[:10]}...")
        self.configurado = True
    
    def enviar(self, destinatario, asunto, mensaje):
        if not self.configurado:
            raise Exception("Servicio de email no configurado")
        print(f"📧 SendGrid: Enviando email a {destinatario}")
        print(f"   API: {self.api_key[:10]}...")
        return {"status": "enviado", "id": "sendgrid_456", "servicio": "sendgrid"}

class ServicioEmailGmailDIP(IServicioEmail):
    """Implementación Gmail mejorada que cumple DIP"""
    
    def __init__(self):
        self.usuario = None
        self.password = None
        self.configurado = False
    
    def configurar(self, configuracion):
        self.usuario = configuracion.get("usuario")
        self.password = configuracion.get("password")
        print(f"⚙️ Gmail: Configurado para {self.usuario}")
        self.configurado = True
    
    def enviar(self, destinatario, asunto, mensaje):
        if not self.configurado:
            raise Exception("Servicio de email no configurado")
        print(f"📧 Gmail: Enviando desde {self.usuario} a {destinatario}")
        return {"status": "enviado", "id": "gmail_789", "servicio": "gmail"}

class LoggerConsola(ILogger):
    """Logger que escribe a consola"""
    
    def __init__(self, nivel="INFO"):
        self.nivel = nivel
    
    def log(self, nivel, mensaje):
        print(f"🖥️ CONSOLA [{nivel}]: {mensaje}")
    
    def log_error(self, mensaje, excepcion=None):
        print(f"🖥️ CONSOLA [ERROR]: {mensaje}")
        if excepcion:
            print(f"🖥️ CONSOLA [ERROR]: Excepción: {excepcion}")

class LoggerArchivoDIP(ILogger):
    """Logger que escribe a archivo - cumple DIP"""
    
    def __init__(self, archivo="app.log"):
        self.archivo = archivo
    
    def log(self, nivel, mensaje):
        print(f"📄 ARCHIVO [{nivel}]: {mensaje} → {self.archivo}")
    
    def log_error(self, mensaje, excepcion=None):
        print(f"📄 ARCHIVO [ERROR]: {mensaje} → {self.archivo}")
        if excepcion:
            print(f"📄 ARCHIVO [ERROR]: {excepcion} → {self.archivo}")

# 3. Clase de alto nivel que CUMPLE DIP
class GestorUsuariosBueno:
    """CUMPLE DIP: Depende de abstracciones, no de implementaciones"""
    
    def __init__(self, bd: IBaseDatos, email: IServicioEmail, logger: ILogger):
        # ✅ INYECCIÓN DE DEPENDENCIAS: Recibe abstracciones
        self.bd = bd
        self.email = email
        self.logger = logger
    
    def configurar_servicios(self, config_bd=None, config_email=None):
        """Configura los servicios inyectados"""
        try:
            self.bd.conectar()
            
            if config_email:
                self.email.configurar(config_email)
            
            self.logger.log("INFO", "Servicios configurados exitosamente")
            return True
            
        except Exception as e:
            self.logger.log_error("Error configurando servicios", e)
            return False
    
    def registrar_usuario(self, nombre, email, password):
        """Método que usa abstracciones - flexible y testeable"""
        self.logger.log("INFO", f"Iniciando registro de usuario: {nombre}")
        
        try:
            # Verificar si usuario existe
            usuario_existente = self.bd.buscar_usuario(email)
            if usuario_existente and usuario_existente.get("id"):
                self.logger.log("WARNING", f"Usuario {email} ya existe")
                return False
            
            # Crear usuario
            usuario = {"nombre": nombre, "email": email, "password": password}
            
            # Guardar en BD (abstracción)
            resultado_bd = self.bd.guardar_usuario(usuario)
            self.logger.log("INFO", f"Usuario guardado con ID: {resultado_bd['id']}")
            
            # Enviar email de bienvenida (abstracción)
            resultado_email = self.email.enviar(
                email,
                "¡Bienvenido!",
                f"Hola {nombre}, tu cuenta ha sido creada exitosamente."
            )
            self.logger.log("INFO", f"Email de bienvenida enviado: {resultado_email['id']}")
            
            self.logger.log("INFO", f"Usuario {nombre} registrado exitosamente")
            return True
            
        except Exception as e:
            self.logger.log_error(f"Error registrando usuario {nombre}", e)
            return False
    
    def finalizar(self):
        """Limpieza de recursos"""
        try:
            self.bd.desconectar()
            self.logger.log("INFO", "Servicios desconectados")
        except Exception as e:
            self.logger.log_error("Error desconectando servicios", e)

# 4. Factory para crear configuraciones específicas
class GestorUsuariosFactory:
    """Factory que crea gestores con diferentes configuraciones"""
    
    @staticmethod
    def crear_gestor_mysql_gmail():
        """Gestor con MySQL + Gmail"""
        bd = BaseDatosMySQLDIP()
        email = ServicioEmailGmailDIP()
        logger = LoggerConsola()
        return GestorUsuariosBueno(bd, email, logger)
    
    @staticmethod
    def crear_gestor_postgresql_sendgrid():
        """Gestor con PostgreSQL + SendGrid"""
        bd = BaseDatosPostgreSQL()
        email = ServicioEmailSendGrid()
        logger = LoggerArchivoDIP("usuarios.log")
        return GestorUsuariosBueno(bd, email, logger)
    
    @staticmethod
    def crear_gestor_testing():
        """Gestor para testing con mocks"""
        bd = MockBaseDatos()
        email = MockEmail()
        logger = LoggerConsola("DEBUG")
        return GestorUsuariosBueno(bd, email, logger)

# 5. Mocks para testing (implementan las mismas abstracciones)
class MockBaseDatos(IBaseDatos):
    """Mock de base de datos para testing"""
    
    def __init__(self):
        self.usuarios = {}
        self.conectado = False
    
    def conectar(self):
        print("🧪 MOCK BD: Conexión simulada")
        self.conectado = True
        return True
    
    def guardar_usuario(self, usuario):
        user_id = len(self.usuarios) + 1
        self.usuarios[user_id] = usuario
        print(f"🧪 MOCK BD: Usuario {usuario['nombre']} guardado con ID {user_id}")
        return {"id": user_id, "status": "guardado", "bd": "mock"}
    
    def buscar_usuario(self, email):
        print(f"🧪 MOCK BD: Buscando {email}")
        for user_id, usuario in self.usuarios.items():
            if usuario["email"] == email:
                return {"id": user_id, **usuario}
        return None
    
    def desconectar(self):
        print("🧪 MOCK BD: Desconexión simulada")
        self.conectado = False

class MockEmail(IServicioEmail):
    """Mock de email para testing"""
    
    def __init__(self):
        self.emails_enviados = []
        self.configurado = True
    
    def configurar(self, configuracion):
        print("🧪 MOCK EMAIL: Configuración simulada")
    
    def enviar(self, destinatario, asunto, mensaje):
        email = {
            "destinatario": destinatario,
            "asunto": asunto,
            "mensaje": mensaje,
            "id": f"mock_{len(self.emails_enviados) + 1}"
        }
        self.emails_enviados.append(email)
        print(f"🧪 MOCK EMAIL: Email simulado enviado a {destinatario}")
        return {"status": "enviado", "id": email["id"], "servicio": "mock"}

# Uso correcto que CUMPLE DIP
print("Usando gestor que cumple DIP:")

print("\n🔧 Configuración 1: MySQL + Gmail")
gestor1 = GestorUsuariosFactory.crear_gestor_mysql_gmail()
gestor1.configurar_servicios(config_email={"usuario": "app@empresa.com", "password": "secret"})
gestor1.registrar_usuario("Carlos Ruiz", "carlos@email.com", "password456")
gestor1.finalizar()

print("\n🔧 Configuración 2: PostgreSQL + SendGrid")
gestor2 = GestorUsuariosFactory.crear_gestor_postgresql_sendgrid()
gestor2.configurar_servicios(config_email={"api_key": "SG.abcd1234567890xyz"})
gestor2.registrar_usuario("María López", "maria@email.com", "password789")
gestor2.finalizar()

print("\n🧪 Configuración 3: Testing con Mocks")
gestor_test = GestorUsuariosFactory.crear_gestor_testing()
gestor_test.configurar_servicios()
gestor_test.registrar_usuario("Usuario Test", "test@email.com", "testpass")
gestor_test.finalizar()

print("\n=== VENTAJAS DE APLICAR DIP ===")
print("✅ Flexibilidad: Fácil cambiar implementaciones")
print("✅ Testabilidad: Se pueden usar mocks fácilmente")
print("✅ Mantenibilidad: Cambios en bajo nivel no afectan alto nivel")
print("✅ Extensibilidad: Agregar nuevas implementaciones sin modificar código")
print("✅ Desacoplamiento: Módulos independientes")

print("\n=== CÓMO IDENTIFICAR VIOLACIONES DE DIP ===")
print("❌ Clases que crean sus propias dependencias con 'new'")
print("❌ Imports directos de implementaciones concretas")
print("❌ Código difícil de testear por dependencias externas")
print("❌ Cambios en módulos de bajo nivel requieren cambios en alto nivel")
print("❌ Imposibilidad de sustituir implementaciones")

print("\n=== TÉCNICAS PARA APLICAR DIP ===")
print("🔧 Inyección de dependencias por constructor")
print("🔧 Uso de interfaces/abstracciones")
print("🔧 Factory pattern para crear configuraciones")
print("🔧 Inversión de control (IoC) containers")
print("🔧 Configuración externa de dependencias")
