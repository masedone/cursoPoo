## 🔹 PRINCIPIO SOLID 1: SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# "Una clase debe tener una sola razón para cambiar"

print("=== PRINCIPIO SRP - RESPONSABILIDAD ÚNICA ===\n")

# ❌ VIOLACIÓN DE SRP - Una clase con múltiples responsabilidades
print("❌ VIOLACIÓN DE SRP - Múltiples responsabilidades:")

class UsuarioCompleto:
    """VIOLA SRP: Esta clase tiene múltiples razones para cambiar"""
    
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password
    
    # RESPONSABILIDAD 1: Validación de datos
    def validar_email(self):
        if "@" not in self.email or "." not in self.email:
            return False, "Email inválido"
        return True, "Email válido"
    
    def validar_password(self):
        if len(self.password) < 8:
            return False, "Password debe tener al menos 8 caracteres"
        return True, "Password válido"
    
    # RESPONSABILIDAD 2: Encriptación
    def encriptar_password(self):
        # Simulación de encriptación
        return f"encrypted_{self.password}_hash"
    
    # RESPONSABILIDAD 3: Base de datos
    def guardar_en_bd(self):
        print(f"💾 Guardando usuario {self.nombre} en base de datos")
        print(f"   Email: {self.email}")
        print(f"   Password encriptado: {self.encriptar_password()}")
        return True
    
    # RESPONSABILIDAD 4: Envío de emails
    def enviar_email_bienvenida(self):
        print(f"📧 Enviando email de bienvenida a: {self.email}")
        mensaje = f"Bienvenido {self.nombre}!"
        print(f"   Mensaje: {mensaje}")
        return True
    
    # RESPONSABILIDAD 5: Logging
    def log_registro(self):
        print(f"📝 LOG: Usuario {self.nombre} registrado exitosamente")
        return True
    
    def registrar_usuario_completo(self):
        """Método que hace todo - VIOLA SRP"""
        print(f"🔄 Registrando usuario: {self.nombre}")
        
        # Validar
        email_valido, msg_email = self.validar_email()
        if not email_valido:
            print(f"❌ {msg_email}")
            return False
        
        pass_valido, msg_pass = self.validar_password()
        if not pass_valido:
            print(f"❌ {msg_pass}")
            return False
        
        # Guardar
        self.guardar_en_bd()
        
        # Notificar
        self.enviar_email_bienvenida()
        
        # Log
        self.log_registro()
        
        print("✅ Usuario registrado exitosamente")
        return True

# Uso problemático
print("Usando clase que viola SRP:")
usuario_malo = UsuarioCompleto("Juan Pérez", "juan@email.com", "password123")
usuario_malo.registrar_usuario_completo()

print("\n" + "="*70 + "\n")

# ✅ APLICANDO SRP - Cada clase tiene una sola responsabilidad
print("✅ APLICANDO SRP - Una responsabilidad por clase:")

class Usuario:
    """SOLO se encarga de representar los datos del usuario"""
    
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password
    
    def obtener_info(self):
        return {
            "nombre": self.nombre,
            "email": self.email,
            "password": self.password
        }
    
    def __str__(self):
        return f"Usuario: {self.nombre} ({self.email})"

class ValidadorUsuario:
    """SOLO se encarga de validar datos de usuario"""
    
    def validar_email(self, email):
        if not email or "@" not in email or "." not in email:
            return False, "Email inválido: debe contener @ y ."
        
        if len(email) < 5:
            return False, "Email muy corto"
        
        return True, "Email válido"
    
    def validar_password(self, password):
        if len(password) < 8:
            return False, "Password debe tener al menos 8 caracteres"
        
        if not any(c.isdigit() for c in password):
            return False, "Password debe contener al menos un número"
        
        return True, "Password válido"
    
    def validar_nombre(self, nombre):
        if not nombre or len(nombre) < 2:
            return False, "Nombre debe tener al menos 2 caracteres"
        
        return True, "Nombre válido"
    
    def validar_usuario_completo(self, usuario):
        """Valida todos los campos del usuario"""
        print("🔍 Validando datos del usuario...")
        
        # Validar nombre
        nombre_valido, msg_nombre = self.validar_nombre(usuario.nombre)
        if not nombre_valido:
            return False, msg_nombre
        
        # Validar email
        email_valido, msg_email = self.validar_email(usuario.email)
        if not email_valido:
            return False, msg_email
        
        # Validar password
        pass_valido, msg_pass = self.validar_password(usuario.password)
        if not pass_valido:
            return False, msg_pass
        
        print("✅ Todos los datos son válidos")
        return True, "Usuario válido"

class EncriptadorPassword:
    """SOLO se encarga de encriptar passwords"""
    
    def __init__(self, algoritmo="SHA256"):
        self.algoritmo = algoritmo
    
    def encriptar(self, password):
        """Simula encriptación de password"""
        print(f"🔐 Encriptando password con {self.algoritmo}")
        
        # Simulación de diferentes algoritmos
        if self.algoritmo == "SHA256":
            return f"sha256_{hash(password)}_encrypted"
        elif self.algoritmo == "MD5":
            return f"md5_{hash(password)}_encrypted"
        else:
            return f"basic_{password}_encrypted"
    
    def verificar_password(self, password, hash_encriptado):
        """Verifica si un password coincide con el hash"""
        hash_calculado = self.encriptar(password)
        return hash_calculado == hash_encriptado

class RepositorioUsuario:
    """SOLO se encarga de guardar/recuperar usuarios de la BD"""
    
    def __init__(self, conexion_bd="mysql://localhost"):
        self.conexion = conexion_bd
        self.tabla = "usuarios"
    
    def guardar(self, usuario, password_encriptado):
        """Guarda un usuario en la base de datos"""
        print(f"💾 Guardando en BD: {self.conexion}")
        print(f"   Tabla: {self.tabla}")
        print(f"   Usuario: {usuario.nombre}")
        print(f"   Email: {usuario.email}")
        print(f"   Password: {password_encriptado}")
        
        # Simulación de INSERT
        return {"id": 12345, "status": "guardado"}
    
    def buscar_por_email(self, email):
        """Busca un usuario por email"""
        print(f"🔍 Buscando usuario con email: {email}")
        # Simulación de búsqueda
        return None  # No encontrado
    
    def existe_usuario(self, email):
        """Verifica si ya existe un usuario con ese email"""
        usuario = self.buscar_por_email(email)
        return usuario is not None

class NotificadorEmail:
    """SOLO se encarga de enviar emails"""
    
    def __init__(self, servidor_smtp="smtp.empresa.com"):
        self.servidor = servidor_smtp
    
    def enviar_bienvenida(self, usuario):
        """Envía email de bienvenida"""
        print(f"📧 Enviando email de bienvenida")
        print(f"   Servidor: {self.servidor}")
        print(f"   Para: {usuario.email}")
        print(f"   Asunto: ¡Bienvenido {usuario.nombre}!")
        
        mensaje = f"""
        Hola {usuario.nombre},
        
        ¡Bienvenido a nuestra plataforma!
        Tu cuenta ha sido creada exitosamente.
        
        Saludos,
        El equipo
        """
        
        print(f"   Mensaje enviado ✅")
        return {"status": "enviado", "id": "email_12345"}
    
    def enviar_confirmacion(self, usuario, datos_registro):
        """Envía email de confirmación de registro"""
        print(f"📧 Enviando confirmación de registro a: {usuario.email}")
        return {"status": "enviado"}

class LoggerSistema:
    """SOLO se encarga del logging del sistema"""
    
    def __init__(self, archivo_log="sistema.log"):
        self.archivo = archivo_log
        self.nivel = "INFO"
    
    def log_registro_usuario(self, usuario, resultado):
        """Registra el evento de registro de usuario"""
        timestamp = "2024-01-15 10:30:00"
        status = "ÉXITO" if resultado else "ERROR"
        
        print(f"📝 LOG [{timestamp}] {self.nivel}: Registro de usuario")
        print(f"   Usuario: {usuario.nombre}")
        print(f"   Email: {usuario.email}")
        print(f"   Status: {status}")
        print(f"   Archivo: {self.archivo}")
    
    def log_error(self, mensaje, detalle=""):
        """Registra errores del sistema"""
        print(f"📝 LOG ERROR: {mensaje}")
        if detalle:
            print(f"   Detalle: {detalle}")

class ServicioRegistroUsuario:
    """COORDINADOR: Orquesta el proceso de registro usando las otras clases"""
    
    def __init__(self, validador, encriptador, repositorio, notificador, logger):
        self.validador = validador
        self.encriptador = encriptador
        self.repositorio = repositorio
        self.notificador = notificador
        self.logger = logger
    
    def registrar_usuario(self, usuario):
        """Proceso completo de registro usando SRP"""
        print(f"🔄 Iniciando registro de usuario: {usuario.nombre}")
        
        try:
            # 1. Validar datos
            es_valido, mensaje = self.validador.validar_usuario_completo(usuario)
            if not es_valido:
                print(f"❌ Validación falló: {mensaje}")
                self.logger.log_error("Validación falló", mensaje)
                return False
            
            # 2. Verificar que no existe
            if self.repositorio.existe_usuario(usuario.email):
                print(f"❌ Usuario ya existe: {usuario.email}")
                self.logger.log_error("Usuario duplicado", usuario.email)
                return False
            
            # 3. Encriptar password
            password_encriptado = self.encriptador.encriptar(usuario.password)
            
            # 4. Guardar en BD
            resultado_bd = self.repositorio.guardar(usuario, password_encriptado)
            
            # 5. Enviar email de bienvenida
            resultado_email = self.notificador.enviar_bienvenida(usuario)
            
            # 6. Registrar en log
            self.logger.log_registro_usuario(usuario, True)
            
            print("✅ Usuario registrado exitosamente")
            return True
            
        except Exception as e:
            print(f"❌ Error durante el registro: {e}")
            self.logger.log_error("Error en registro", str(e))
            return False

# Uso con SRP (mucho mejor):
print("Usando SRP - cada clase tiene una responsabilidad:")

# Crear instancias de cada servicio
validador = ValidadorUsuario()
encriptador = EncriptadorPassword("SHA256")
repositorio = RepositorioUsuario("postgresql://localhost")
notificador = NotificadorEmail("smtp.gmail.com")
logger = LoggerSistema("usuarios.log")

# Crear el servicio coordinador
servicio_registro = ServicioRegistroUsuario(
    validador, encriptador, repositorio, notificador, logger
)

# Crear usuario
usuario_bueno = Usuario("María García", "maria@email.com", "mipassword123")

# Registrar usando SRP
resultado = servicio_registro.registrar_usuario(usuario_bueno)

print(f"\n🎯 Resultado del registro: {'Éxito' if resultado else 'Fallo'}")

print("\n=== VENTAJAS DE APLICAR SRP ===")
print("✅ Cada clase tiene una responsabilidad clara")
print("✅ Fácil de testear cada componente por separado")
print("✅ Cambios en validación no afectan la BD")
print("✅ Fácil agregar nuevos tipos de notificación")
print("✅ Código más mantenible y extensible")

print("\n=== IDENTIFICAR VIOLACIONES DE SRP ===")
print("❌ La clase tiene muchos métodos no relacionados")
print("❌ Cambios en una funcionalidad afectan otras")
print("❌ Difícil de testear la clase completa")
print("❌ El nombre de la clase es muy genérico")
print("❌ La clase tiene múltiples imports diferentes")
