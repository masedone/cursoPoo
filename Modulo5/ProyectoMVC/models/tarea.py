"""
📦 MODELO: Tarea
Representa una tarea individual con su lógica de negocio
"""

import datetime
from enum import Enum
from typing import Optional

class EstadoTarea(Enum):
    """Estados posibles de una tarea"""
    PENDIENTE = "pendiente"
    EN_PROGRESO = "en_progreso"
    COMPLETADA = "completada"
    CANCELADA = "cancelada"

class PrioridadTarea(Enum):
    """Prioridades posibles de una tarea"""
    BAJA = "baja"
    MEDIA = "media"
    ALTA = "alta"
    CRITICA = "critica"

class Tarea:
    """
    Modelo de Tarea - Solo contiene datos y lógica de negocio
    No maneja presentación ni coordinación
    """
    
    def __init__(self, id: int, titulo: str, descripcion: str, 
                 usuario_asignado: str, prioridad: PrioridadTarea = PrioridadTarea.MEDIA):
        # Datos básicos
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.usuario_asignado = usuario_asignado
        self.prioridad = prioridad
        
        # Estado y fechas
        self.estado = EstadoTarea.PENDIENTE
        self.fecha_creacion = datetime.datetime.now()
        self.fecha_inicio: Optional[datetime.datetime] = None
        self.fecha_completado: Optional[datetime.datetime] = None
        self.fecha_vencimiento: Optional[datetime.datetime] = None
        
        # Metadatos
        self.usuario_creador = usuario_asignado  # Por simplicidad
        self.etiquetas = []
        self.comentarios = []
        self.tiempo_estimado_horas: Optional[float] = None
        self.tiempo_real_horas: Optional[float] = None
    
    # ========== LÓGICA DE NEGOCIO ==========
    
    def cambiar_estado(self, nuevo_estado: EstadoTarea) -> bool:
        """
        Lógica de negocio: Cambiar estado de la tarea
        Valida transiciones permitidas
        """
        # Validar transiciones permitidas
        transiciones_validas = {
            EstadoTarea.PENDIENTE: [EstadoTarea.EN_PROGRESO, EstadoTarea.CANCELADA],
            EstadoTarea.EN_PROGRESO: [EstadoTarea.COMPLETADA, EstadoTarea.PENDIENTE, EstadoTarea.CANCELADA],
            EstadoTarea.COMPLETADA: [EstadoTarea.EN_PROGRESO],  # Reabrir tarea
            EstadoTarea.CANCELADA: [EstadoTarea.PENDIENTE]  # Reactivar tarea
        }
        
        if nuevo_estado not in transiciones_validas[self.estado]:
            return False
        
        # Actualizar estado y fechas
        estado_anterior = self.estado
        self.estado = nuevo_estado
        
        if nuevo_estado == EstadoTarea.EN_PROGRESO and estado_anterior == EstadoTarea.PENDIENTE:
            self.fecha_inicio = datetime.datetime.now()
        elif nuevo_estado == EstadoTarea.COMPLETADA:
            self.fecha_completado = datetime.datetime.now()
        elif nuevo_estado == EstadoTarea.PENDIENTE and estado_anterior in [EstadoTarea.COMPLETADA, EstadoTarea.CANCELADA]:
            # Reactivar tarea
            self.fecha_completado = None
            if estado_anterior == EstadoTarea.COMPLETADA:
                self.fecha_inicio = None
        
        return True
    
    def asignar_usuario(self, nuevo_usuario: str) -> bool:
        """Lógica de negocio: Asignar tarea a otro usuario"""
        if not nuevo_usuario.strip():
            return False
        
        if self.estado == EstadoTarea.COMPLETADA:
            return False  # No se puede reasignar tarea completada
        
        self.usuario_asignado = nuevo_usuario
        return True
    
    def cambiar_prioridad(self, nueva_prioridad: PrioridadTarea) -> bool:
        """Lógica de negocio: Cambiar prioridad de la tarea"""
        if self.estado == EstadoTarea.COMPLETADA:
            return False  # No se puede cambiar prioridad de tarea completada
        
        self.prioridad = nueva_prioridad
        return True
    
    def establecer_fecha_vencimiento(self, fecha_vencimiento: datetime.datetime) -> bool:
        """Lógica de negocio: Establecer fecha de vencimiento"""
        if fecha_vencimiento <= datetime.datetime.now():
            return False  # Fecha debe ser futura
        
        if self.estado == EstadoTarea.COMPLETADA:
            return False  # No se puede cambiar fecha de tarea completada
        
        self.fecha_vencimiento = fecha_vencimiento
        return True
    
    def agregar_etiqueta(self, etiqueta: str) -> bool:
        """Lógica de negocio: Agregar etiqueta a la tarea"""
        etiqueta = etiqueta.strip().lower()
        if not etiqueta:
            return False
        
        if etiqueta not in self.etiquetas:
            self.etiquetas.append(etiqueta)
            return True
        
        return False  # Etiqueta ya existe
    
    def remover_etiqueta(self, etiqueta: str) -> bool:
        """Lógica de negocio: Remover etiqueta de la tarea"""
        etiqueta = etiqueta.strip().lower()
        if etiqueta in self.etiquetas:
            self.etiquetas.remove(etiqueta)
            return True
        return False
    
    def agregar_comentario(self, comentario: str, usuario: str) -> bool:
        """Lógica de negocio: Agregar comentario a la tarea"""
        if not comentario.strip():
            return False
        
        nuevo_comentario = {
            "id": len(self.comentarios) + 1,
            "texto": comentario.strip(),
            "usuario": usuario,
            "fecha": datetime.datetime.now()
        }
        
        self.comentarios.append(nuevo_comentario)
        return True
    
    def establecer_tiempo_estimado(self, horas: float) -> bool:
        """Lógica de negocio: Establecer tiempo estimado"""
        if horas <= 0:
            return False
        
        self.tiempo_estimado_horas = horas
        return True
    
    def registrar_tiempo_real(self, horas: float) -> bool:
        """Lógica de negocio: Registrar tiempo real trabajado"""
        if horas <= 0:
            return False
        
        if self.tiempo_real_horas is None:
            self.tiempo_real_horas = 0
        
        self.tiempo_real_horas += horas
        return True
    
    # ========== CONSULTAS DE NEGOCIO ==========
    
    def esta_vencida(self) -> bool:
        """Verifica si la tarea está vencida"""
        if self.fecha_vencimiento is None:
            return False
        
        if self.estado == EstadoTarea.COMPLETADA:
            return False
        
        return datetime.datetime.now() > self.fecha_vencimiento
    
    def esta_en_plazo(self) -> bool:
        """Verifica si la tarea está en plazo"""
        return not self.esta_vencida()
    
    def dias_para_vencimiento(self) -> Optional[int]:
        """Calcula días restantes para vencimiento"""
        if self.fecha_vencimiento is None:
            return None
        
        if self.estado == EstadoTarea.COMPLETADA:
            return None
        
        diferencia = self.fecha_vencimiento - datetime.datetime.now()
        return diferencia.days
    
    def duracion_en_progreso(self) -> Optional[datetime.timedelta]:
        """Calcula tiempo que ha estado en progreso"""
        if self.fecha_inicio is None:
            return None
        
        fecha_fin = self.fecha_completado or datetime.datetime.now()
        return fecha_fin - self.fecha_inicio
    
    def es_alta_prioridad(self) -> bool:
        """Verifica si es de alta prioridad"""
        return self.prioridad in [PrioridadTarea.ALTA, PrioridadTarea.CRITICA]
    
    def es_critica(self) -> bool:
        """Verifica si es crítica"""
        return self.prioridad == PrioridadTarea.CRITICA
    
    def necesita_atencion(self) -> bool:
        """Determina si la tarea necesita atención urgente"""
        # Criterios de negocio para atención urgente
        if self.es_critica():
            return True
        
        if self.esta_vencida():
            return True
        
        if self.es_alta_prioridad() and self.dias_para_vencimiento() is not None:
            return self.dias_para_vencimiento() <= 1
        
        return False
    
    # ========== SERIALIZACIÓN ==========
    
    def to_dict(self) -> dict:
        """Convierte la tarea a diccionario para serialización"""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "usuario_asignado": self.usuario_asignado,
            "usuario_creador": self.usuario_creador,
            "prioridad": self.prioridad.value,
            "estado": self.estado.value,
            "fecha_creacion": self.fecha_creacion.isoformat(),
            "fecha_inicio": self.fecha_inicio.isoformat() if self.fecha_inicio else None,
            "fecha_completado": self.fecha_completado.isoformat() if self.fecha_completado else None,
            "fecha_vencimiento": self.fecha_vencimiento.isoformat() if self.fecha_vencimiento else None,
            "etiquetas": self.etiquetas,
            "comentarios": [
                {
                    **comentario,
                    "fecha": comentario["fecha"].isoformat()
                }
                for comentario in self.comentarios
            ],
            "tiempo_estimado_horas": self.tiempo_estimado_horas,
            "tiempo_real_horas": self.tiempo_real_horas,
            # Campos calculados
            "esta_vencida": self.esta_vencida(),
            "dias_para_vencimiento": self.dias_para_vencimiento(),
            "necesita_atencion": self.necesita_atencion()
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Tarea':
        """Crea una tarea desde un diccionario"""
        tarea = cls(
            id=data["id"],
            titulo=data["titulo"],
            descripcion=data["descripcion"],
            usuario_asignado=data["usuario_asignado"],
            prioridad=PrioridadTarea(data["prioridad"])
        )
        
        # Restaurar datos adicionales
        tarea.usuario_creador = data.get("usuario_creador", data["usuario_asignado"])
        tarea.estado = EstadoTarea(data["estado"])
        tarea.fecha_creacion = datetime.datetime.fromisoformat(data["fecha_creacion"])
        
        if data.get("fecha_inicio"):
            tarea.fecha_inicio = datetime.datetime.fromisoformat(data["fecha_inicio"])
        
        if data.get("fecha_completado"):
            tarea.fecha_completado = datetime.datetime.fromisoformat(data["fecha_completado"])
        
        if data.get("fecha_vencimiento"):
            tarea.fecha_vencimiento = datetime.datetime.fromisoformat(data["fecha_vencimiento"])
        
        tarea.etiquetas = data.get("etiquetas", [])
        tarea.tiempo_estimado_horas = data.get("tiempo_estimado_horas")
        tarea.tiempo_real_horas = data.get("tiempo_real_horas")
        
        # Restaurar comentarios
        for comentario_data in data.get("comentarios", []):
            comentario = comentario_data.copy()
            comentario["fecha"] = datetime.datetime.fromisoformat(comentario["fecha"])
            tarea.comentarios.append(comentario)
        
        return tarea
    
    def __str__(self) -> str:
        """Representación string de la tarea"""
        return f"Tarea({self.id}): {self.titulo} [{self.estado.value}] - {self.usuario_asignado}"
    
    def __repr__(self) -> str:
        """Representación detallada de la tarea"""
        return (f"Tarea(id={self.id}, titulo='{self.titulo}', "
                f"estado={self.estado.value}, prioridad={self.prioridad.value})")
