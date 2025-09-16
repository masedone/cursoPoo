## 🔹 EJERCICIO PRÁCTICO: APLICANDO TODOS LOS PRINCIPIOS SOLID
# Sistema completo que demuestra todos los principios SOLID trabajando juntos

print("=== EJERCICIO PRÁCTICO: SISTEMA DE NOTIFICACIONES SOLID ===\n")

from abc import ABC, abstractmethod
from enum import Enum

# 📝 EJERCICIO: Crear un sistema de notificaciones que:
# 1. SRP: Cada clase tiene una sola responsabilidad
# 2. OCP: Fácil agregar nuevos tipos de notificación
# 3. LSP: Las implementaciones son intercambiables
# 4. ISP: Interfaces específicas y pequeñas
# 5. DIP: Dependencia de abstracciones, no implementaciones

print("🎯 OBJETIVO: Sistema de notificaciones que cumple todos los principios SOLID")
print("="*70)

# 🔸 APLICANDO ISP - Interfaces pequeñas y específicas
class INotificacion(ABC):
    """Interface específica para envío de notificaciones"""
    @abstractmethod
    def enviar(self, destinatario, mensaje):
        pass
    
    @abstractmethod
    def validar_destinatario(self, destinatario):
        pass

class IFormateador(ABC):
    """Interface específica para formateo de mensajes"""
    @abstractmethod
    def formatear(self, mensaje, datos_adicionales=None):
        pass

class ILogger(ABC):
    """Interface específica para logging"""
    @abstractmethod
    def log(self, nivel, mensaje):
        pass

class IValidador(ABC):
    """Interface específica para validación"""
    @abstractmethod
    def validar(self, datos):
        pass

# 🔸 APLICANDO SRP - Cada clase tiene una sola responsabilidad
class TipoNotificacion(Enum):
    """Enum para tipos de notificación - SRP: Solo define tipos"""
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"
    SLACK = "slack"

class ValidadorEmail:
    """SRP: Solo valida emails"""
    def validar(self, email):
        if not email or "@" not in email or "." not in email:
            return False, "Email inválido"
        if len(email) < 5:
            return False, "Email muy corto"
        return True, "Email válido"

class ValidadorTelefono:
    """SRP: Solo valida teléfonos"""
    def validar(self, telefono):
        # Remover espacios y caracteres especiales
        telefono_limpio = ''.join(filter(str.isdigit, telefono))
        if len(telefono_limpio) < 9:
            return False, "Teléfono muy corto"
        if len(telefono_limpio) > 15:
            return False, "Teléfono muy largo"
        return True, "Teléfono válido"

class FormateadorHTML:
    """SRP: Solo formatea mensajes en HTML"""
    def formatear(self, mensaje, datos_adicionales=None):
        html = f"<html><body><h2>Notificación</h2><p>{mensaje}</p>"
        if datos_adicionales:
            html += "<ul>"
            for clave, valor in datos_adicionales.items():
                html += f"<li><strong>{clave}:</strong> {valor}</li>"
            html += "</ul>"
        html += "</body></html>"
        return html

class FormateadorTextoPlano:
    """SRP: Solo formatea mensajes en texto plano"""
    def formatear(self, mensaje, datos_adicionales=None):
        texto = f"NOTIFICACIÓN\n{'-'*20}\n{mensaje}\n"
        if datos_adicionales:
            texto += "\nDetalles:\n"
            for clave, valor in datos_adicionales.items():
                texto += f"- {clave}: {valor}\n"
        return texto

class FormateadorMarkdown:
    """SRP: Solo formatea mensajes en Markdown"""
    def formatear(self, mensaje, datos_adicionales=None):
        markdown = f"## Notificación\n\n{mensaje}\n"
        if datos_adicionales:
            markdown += "\n### Detalles:\n"
            for clave, valor in datos_adicionales.items():
                markdown += f"- **{clave}**: {valor}\n"
        return markdown

class LoggerConsola:
    """SRP: Solo hace logging a consola"""
    def log(self, nivel, mensaje):
        print(f"🖥️ [{nivel}] {mensaje}")

# 🔸 APLICANDO OCP y LSP - Extensible y sustituible
class NotificacionEmail(INotificacion):
    """Implementación específica para email - cumple LSP"""
    
    def __init__(self, servidor_smtp="smtp.gmail.com"):
        self.servidor = servidor_smtp
        self.validador = ValidadorEmail()
    
    def validar_destinatario(self, destinatario):
        return self.validador.validar(destinatario)
    
    def enviar(self, destinatario, mensaje):
        es_valido, msg_validacion = self.validar_destinatario(destinatario)
        if not es_valido:
            raise ValueError(f"Email inválido: {msg_validacion}")
        
        print(f"📧 Enviando email via {self.servidor}")
        print(f"   Para: {destinatario}")
        print(f"   Mensaje: {mensaje[:50]}...")
        return {
            "status": "enviado",
            "tipo": "email",
            "destinatario": destinatario,
            "servidor": self.servidor
        }

class NotificacionSMS(INotificacion):
    """Implementación específica para SMS - cumple LSP"""
    
    def __init__(self, proveedor="Twilio"):
        self.proveedor = proveedor
        self.validador = ValidadorTelefono()
    
    def validar_destinatario(self, destinatario):
        return self.validador.validar(destinatario)
    
    def enviar(self, destinatario, mensaje):
        es_valido, msg_validacion = self.validar_destinatario(destinatario)
        if not es_valido:
            raise ValueError(f"Teléfono inválido: {msg_validacion}")
        
        # Truncar mensaje para SMS (160 caracteres)
        mensaje_truncado = mensaje[:160]
        print(f"📱 Enviando SMS via {self.proveedor}")
        print(f"   Para: {destinatario}")
        print(f"   Mensaje: {mensaje_truncado}")
        return {
            "status": "enviado",
            "tipo": "sms",
            "destinatario": destinatario,
            "proveedor": self.proveedor
        }

class NotificacionPush(INotificacion):
    """Implementación específica para notificaciones push - cumple LSP"""
    
    def __init__(self, plataforma="Firebase"):
        self.plataforma = plataforma
    
    def validar_destinatario(self, destinatario):
        # Para push, el destinatario es un token de dispositivo
        if not destinatario or len(destinatario) < 10:
            return False, "Token de dispositivo inválido"
        return True, "Token válido"
    
    def enviar(self, destinatario, mensaje):
        es_valido, msg_validacion = self.validar_destinatario(destinatario)
        if not es_valido:
            raise ValueError(f"Token inválido: {msg_validacion}")
        
        print(f"📲 Enviando push notification via {self.plataforma}")
        print(f"   Token: {destinatario[:20]}...")
        print(f"   Mensaje: {mensaje}")
        return {
            "status": "enviado",
            "tipo": "push",
            "destinatario": destinatario,
            "plataforma": self.plataforma
        }

# ✅ NUEVA IMPLEMENTACIÓN SIN MODIFICAR CÓDIGO EXISTENTE (OCP)
class NotificacionSlack(INotificacion):
    """Nueva implementación agregada sin modificar código existente"""
    
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
    
    def validar_destinatario(self, destinatario):
        # Para Slack, el destinatario es un canal
        if not destinatario.startswith("#") and not destinatario.startswith("@"):
            return False, "Canal de Slack debe empezar con # o @"
        return True, "Canal válido"
    
    def enviar(self, destinatario, mensaje):
        es_valido, msg_validacion = self.validar_destinatario(destinatario)
        if not es_valido:
            raise ValueError(f"Canal Slack inválido: {msg_validacion}")
        
        print(f"💬 Enviando mensaje a Slack")
        print(f"   Canal: {destinatario}")
        print(f"   Webhook: {self.webhook_url[:30]}...")
        print(f"   Mensaje: {mensaje}")
        return {
            "status": "enviado",
            "tipo": "slack",
            "destinatario": destinatario,
            "webhook": self.webhook_url
        }

# 🔸 APLICANDO DIP - Dependencia de abstracciones
class GestorNotificaciones:
    """Clase de alto nivel que cumple DIP - depende de abstracciones"""
    
    def __init__(self, logger: ILogger):
        self.notificadores = {}  # Registry de notificadores
        self.formateadores = {}  # Registry de formateadores
        self.logger = logger
    
    def registrar_notificador(self, tipo: TipoNotificacion, notificador: INotificacion):
        """Registra un notificador - cumple DIP"""
        self.notificadores[tipo] = notificador
        self.logger.log("INFO", f"Notificador {tipo.value} registrado")
    
    def registrar_formateador(self, nombre: str, formateador: IFormateador):
        """Registra un formateador - cumple DIP"""
        self.formateadores[nombre] = formateador
        self.logger.log("INFO", f"Formateador {nombre} registrado")
    
    def enviar_notificacion(self, tipo: TipoNotificacion, destinatario: str, 
                          mensaje: str, formato="texto", datos_adicionales=None):
        """Envía notificación usando abstracciones"""
        try:
            # Verificar que el notificador esté registrado
            if tipo not in self.notificadores:
                raise ValueError(f"Notificador {tipo.value} no registrado")
            
            # Obtener notificador y formateador
            notificador = self.notificadores[tipo]
            formateador = self.formateadores.get(formato)
            
            # Formatear mensaje si hay formateador
            mensaje_formateado = mensaje
            if formateador:
                mensaje_formateado = formateador.formatear(mensaje, datos_adicionales)
            
            # Enviar notificación
            self.logger.log("INFO", f"Enviando notificación {tipo.value} a {destinatario}")
            resultado = notificador.enviar(destinatario, mensaje_formateado)
            
            self.logger.log("INFO", f"Notificación enviada exitosamente: {resultado['status']}")
            return resultado
            
        except Exception as e:
            self.logger.log("ERROR", f"Error enviando notificación: {e}")
            return {"status": "error", "mensaje": str(e)}
    
    def enviar_multiple(self, configuraciones):
        """Envía múltiples notificaciones"""
        resultados = []
        for config in configuraciones:
            resultado = self.enviar_notificacion(**config)
            resultados.append(resultado)
        return resultados
    
    def listar_notificadores_disponibles(self):
        """Lista todos los notificadores registrados"""
        print("📋 Notificadores disponibles:")
        for tipo, notificador in self.notificadores.items():
            print(f"   - {tipo.value}: {notificador.__class__.__name__}")
    
    def listar_formateadores_disponibles(self):
        """Lista todos los formateadores registrados"""
        print("📋 Formateadores disponibles:")
        for nombre, formateador in self.formateadores.items():
            print(f"   - {nombre}: {formateador.__class__.__name__}")

# 🔸 FACTORY PARA CONFIGURACIONES (DIP)
class NotificacionesFactory:
    """Factory que crea gestores con diferentes configuraciones"""
    
    @staticmethod
    def crear_gestor_completo():
        """Crea gestor con todas las implementaciones"""
        logger = LoggerConsola()
        gestor = GestorNotificaciones(logger)
        
        # Registrar notificadores
        gestor.registrar_notificador(TipoNotificacion.EMAIL, NotificacionEmail())
        gestor.registrar_notificador(TipoNotificacion.SMS, NotificacionSMS())
        gestor.registrar_notificador(TipoNotificacion.PUSH, NotificacionPush())
        gestor.registrar_notificador(TipoNotificacion.SLACK, 
                                    NotificacionSlack("https://hooks.slack.com/webhook123"))
        
        # Registrar formateadores
        gestor.registrar_formateador("texto", FormateadorTextoPlano())
        gestor.registrar_formateador("html", FormateadorHTML())
        gestor.registrar_formateador("markdown", FormateadorMarkdown())
        
        return gestor
    
    @staticmethod
    def crear_gestor_basico():
        """Crea gestor solo con email y SMS"""
        logger = LoggerConsola()
        gestor = GestorNotificaciones(logger)
        
        gestor.registrar_notificador(TipoNotificacion.EMAIL, NotificacionEmail())
        gestor.registrar_notificador(TipoNotificacion.SMS, NotificacionSMS())
        gestor.registrar_formateador("texto", FormateadorTextoPlano())
        
        return gestor

# 🎯 DEMOSTRACIÓN DEL SISTEMA COMPLETO
print("\n🚀 DEMOSTRACIÓN: Sistema de notificaciones SOLID")

# Crear gestor completo
print("\n1️⃣ Creando gestor de notificaciones:")
gestor = NotificacionesFactory.crear_gestor_completo()

# Listar capacidades
print("\n2️⃣ Capacidades del sistema:")
gestor.listar_notificadores_disponibles()
print()
gestor.listar_formateadores_disponibles()

# Enviar notificaciones individuales
print("\n3️⃣ Enviando notificaciones individuales:")

# Email con formato HTML
resultado1 = gestor.enviar_notificacion(
    TipoNotificacion.EMAIL,
    "usuario@email.com",
    "Tu pedido ha sido procesado exitosamente",
    "html",
    {"pedido_id": "12345", "total": "99.99€"}
)

print()

# SMS con formato texto
resultado2 = gestor.enviar_notificacion(
    TipoNotificacion.SMS,
    "+34 666 777 888",
    "Tu código de verificación es: 123456",
    "texto"
)

print()

# Push notification
resultado3 = gestor.enviar_notificacion(
    TipoNotificacion.PUSH,
    "device_token_abc123xyz789",
    "Tienes una nueva notificación",
    "texto"
)

print()

# Slack con formato Markdown
resultado4 = gestor.enviar_notificacion(
    TipoNotificacion.SLACK,
    "#general",
    "El sistema ha sido actualizado correctamente",
    "markdown",
    {"version": "2.1.0", "fecha": "2024-01-15"}
)

# Enviar múltiples notificaciones
print("\n4️⃣ Enviando múltiples notificaciones:")
configuraciones_multiple = [
    {
        "tipo": TipoNotificacion.EMAIL,
        "destinatario": "admin@empresa.com",
        "mensaje": "Reporte diario generado",
        "formato": "html"
    },
    {
        "tipo": TipoNotificacion.SLACK,
        "destinatario": "#dev-team",
        "mensaje": "Deploy completado exitosamente",
        "formato": "markdown"
    }
]

resultados_multiple = gestor.enviar_multiple(configuraciones_multiple)

print("\n5️⃣ Resumen de resultados:")
todos_los_resultados = [resultado1, resultado2, resultado3, resultado4] + resultados_multiple
for i, resultado in enumerate(todos_los_resultados, 1):
    status = "✅" if resultado["status"] == "enviado" else "❌"
    print(f"   {i}. {status} {resultado.get('tipo', 'multiple')}: {resultado['status']}")

print("\n" + "="*70)
print("🎉 PRINCIPIOS SOLID APLICADOS EXITOSAMENTE:")
print("✅ SRP: Cada clase tiene una sola responsabilidad")
print("✅ OCP: Fácil agregar nuevos notificadores y formateadores")
print("✅ LSP: Todas las implementaciones son intercambiables")
print("✅ ISP: Interfaces pequeñas y específicas")
print("✅ DIP: Dependencia de abstracciones, no implementaciones")

print("\n🚀 BENEFICIOS OBTENIDOS:")
print("✅ Código flexible y extensible")
print("✅ Fácil testing con mocks")
print("✅ Mantenimiento simplificado")
print("✅ Bajo acoplamiento")
print("✅ Alta cohesión")
print("✅ Reutilización de componentes")
