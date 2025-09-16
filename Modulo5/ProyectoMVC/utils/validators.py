"""
🔧 UTILIDADES: Validadores
Funciones de validación reutilizables
"""

import re
import datetime
from typing import Tuple, Optional

class TareaValidator:
    """Validadores específicos para tareas"""
    
    @staticmethod
    def validar_titulo(titulo: str) -> Tuple[bool, str]:
        """Valida el título de una tarea"""
        if not titulo:
            return False, "El título no puede estar vacío"
        
        titulo = titulo.strip()
        
        if len(titulo) < 3:
            return False, "El título debe tener al menos 3 caracteres"
        
        if len(titulo) > 100:
            return False, "El título no puede exceder 100 caracteres"
        
        # Verificar caracteres válidos
        if not re.match(r'^[a-zA-Z0-9\s\-_.,!?áéíóúñÁÉÍÓÚÑ]+$', titulo):
            return False, "El título contiene caracteres no válidos"
        
        return True, "Título válido"
    
    @staticmethod
    def validar_descripcion(descripcion: str) -> Tuple[bool, str]:
        """Valida la descripción de una tarea"""
        if not descripcion:
            return True, "Descripción válida"  # Descripción es opcional
        
        descripcion = descripcion.strip()
        
        if len(descripcion) > 500:
            return False, "La descripción no puede exceder 500 caracteres"
        
        return True, "Descripción válida"
    
    @staticmethod
    def validar_usuario(usuario: str) -> Tuple[bool, str]:
        """Valida un nombre de usuario"""
        if not usuario:
            return False, "El usuario no puede estar vacío"
        
        usuario = usuario.strip()
        
        if len(usuario) < 2:
            return False, "El usuario debe tener al menos 2 caracteres"
        
        if len(usuario) > 50:
            return False, "El usuario no puede exceder 50 caracteres"
        
        # Solo letras, números y guiones bajos
        if not re.match(r'^[a-zA-Z0-9_]+$', usuario):
            return False, "El usuario solo puede contener letras, números y guiones bajos"
        
        return True, "Usuario válido"
    
    @staticmethod
    def validar_etiqueta(etiqueta: str) -> Tuple[bool, str]:
        """Valida una etiqueta"""
        if not etiqueta:
            return False, "La etiqueta no puede estar vacía"
        
        etiqueta = etiqueta.strip().lower()
        
        if len(etiqueta) < 2:
            return False, "La etiqueta debe tener al menos 2 caracteres"
        
        if len(etiqueta) > 20:
            return False, "La etiqueta no puede exceder 20 caracteres"
        
        # Solo letras, números y guiones
        if not re.match(r'^[a-z0-9\-]+$', etiqueta):
            return False, "La etiqueta solo puede contener letras, números y guiones"
        
        return True, "Etiqueta válida"
    
    @staticmethod
    def validar_comentario(comentario: str) -> Tuple[bool, str]:
        """Valida un comentario"""
        if not comentario:
            return False, "El comentario no puede estar vacío"
        
        comentario = comentario.strip()
        
        if len(comentario) < 5:
            return False, "El comentario debe tener al menos 5 caracteres"
        
        if len(comentario) > 300:
            return False, "El comentario no puede exceder 300 caracteres"
        
        return True, "Comentario válido"
    
    @staticmethod
    def validar_tiempo_horas(horas: float) -> Tuple[bool, str]:
        """Valida tiempo en horas"""
        if horas <= 0:
            return False, "El tiempo debe ser mayor a 0"
        
        if horas > 1000:  # Límite razonable
            return False, "El tiempo no puede exceder 1000 horas"
        
        return True, "Tiempo válido"

class DateValidator:
    """Validadores para fechas"""
    
    @staticmethod
    def validar_fecha_futura(fecha: datetime.datetime) -> Tuple[bool, str]:
        """Valida que una fecha sea futura"""
        if fecha <= datetime.datetime.now():
            return False, "La fecha debe ser futura"
        
        # No más de 10 años en el futuro
        max_fecha = datetime.datetime.now() + datetime.timedelta(days=3650)
        if fecha > max_fecha:
            return False, "La fecha no puede ser más de 10 años en el futuro"
        
        return True, "Fecha válida"
    
    @staticmethod
    def parsear_fecha(fecha_str: str) -> Optional[datetime.datetime]:
        """Parsea una fecha desde string con múltiples formatos"""
        if not fecha_str:
            return None
        
        formatos = [
            "%Y-%m-%d %H:%M",
            "%Y-%m-%d",
            "%d/%m/%Y %H:%M",
            "%d/%m/%Y",
            "%d-%m-%Y %H:%M",
            "%d-%m-%Y"
        ]
        
        for formato in formatos:
            try:
                fecha = datetime.datetime.strptime(fecha_str, formato)
                
                # Si no tiene hora, establecer al final del día
                if formato in ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"]:
                    fecha = fecha.replace(hour=23, minute=59, second=59)
                
                return fecha
            except ValueError:
                continue
        
        return None

class GeneralValidator:
    """Validadores generales"""
    
    @staticmethod
    def validar_id(id_valor: int) -> Tuple[bool, str]:
        """Valida un ID"""
        if not isinstance(id_valor, int):
            return False, "El ID debe ser un número entero"
        
        if id_valor <= 0:
            return False, "El ID debe ser mayor a 0"
        
        return True, "ID válido"
    
    @staticmethod
    def validar_opcion_menu(opcion: int, min_opcion: int, max_opcion: int) -> Tuple[bool, str]:
        """Valida una opción de menú"""
        if not isinstance(opcion, int):
            return False, "La opción debe ser un número"
        
        if opcion < min_opcion or opcion > max_opcion:
            return False, f"La opción debe estar entre {min_opcion} y {max_opcion}"
        
        return True, "Opción válida"
    
    @staticmethod
    def limpiar_texto(texto: str) -> str:
        """Limpia un texto eliminando espacios extras y caracteres especiales"""
        if not texto:
            return ""
        
        # Eliminar espacios al inicio y final
        texto = texto.strip()
        
        # Reemplazar múltiples espacios con uno solo
        texto = re.sub(r'\s+', ' ', texto)
        
        return texto
    
    @staticmethod
    def es_email_valido(email: str) -> bool:
        """Valida formato básico de email"""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(patron, email))
    
    @staticmethod
    def es_numero_valido(valor: str) -> Tuple[bool, float]:
        """Valida y convierte un número"""
        try:
            numero = float(valor.replace(',', '.'))  # Permitir comas como decimales
            return True, numero
        except (ValueError, AttributeError):
            return False, 0.0
