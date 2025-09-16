"""
📦 MODELO: Repositorio de Tareas
Maneja la persistencia y consultas de tareas
Simula una base de datos
"""

import json
import datetime
from typing import List, Optional, Dict, Any
from models.tarea import Tarea, EstadoTarea, PrioridadTarea

class TareaRepository:
    """
    Repositorio de Tareas - Solo maneja datos
    No contiene lógica de presentación ni coordinación
    """
    
    def __init__(self, archivo_datos: str = "tareas.json"):
        self.archivo_datos = archivo_datos
        self.tareas: List[Tarea] = []
        self.siguiente_id = 1
        
        # Cargar datos existentes
        self.cargar_datos()
    
    # ========== OPERACIONES CRUD ==========
    
    def crear_tarea(self, titulo: str, descripcion: str, usuario_asignado: str,
                   prioridad: PrioridadTarea = PrioridadTarea.MEDIA) -> Tarea:
        """Crea una nueva tarea"""
        tarea = Tarea(
            id=self.siguiente_id,
            titulo=titulo,
            descripcion=descripcion,
            usuario_asignado=usuario_asignado,
            prioridad=prioridad
        )
        
        self.tareas.append(tarea)
        self.siguiente_id += 1
        
        return tarea
    
    def obtener_tarea_por_id(self, tarea_id: int) -> Optional[Tarea]:
        """Obtiene una tarea por su ID"""
        for tarea in self.tareas:
            if tarea.id == tarea_id:
                return tarea
        return None
    
    def obtener_todas_tareas(self) -> List[Tarea]:
        """Obtiene todas las tareas"""
        return self.tareas.copy()
    
    def obtener_tareas_activas(self) -> List[Tarea]:
        """Obtiene tareas que no están canceladas"""
        return [t for t in self.tareas if t.estado != EstadoTarea.CANCELADA]
    
    def actualizar_tarea(self, tarea: Tarea) -> bool:
        """Actualiza una tarea existente"""
        for i, t in enumerate(self.tareas):
            if t.id == tarea.id:
                self.tareas[i] = tarea
                return True
        return False
    
    def eliminar_tarea(self, tarea_id: int) -> bool:
        """Elimina una tarea (marca como cancelada)"""
        tarea = self.obtener_tarea_por_id(tarea_id)
        if tarea:
            tarea.cambiar_estado(EstadoTarea.CANCELADA)
            return True
        return False
    
    def eliminar_definitivamente(self, tarea_id: int) -> bool:
        """Elimina una tarea definitivamente de la lista"""
        for i, tarea in enumerate(self.tareas):
            if tarea.id == tarea_id:
                del self.tareas[i]
                return True
        return False
    
    # ========== CONSULTAS ESPECÍFICAS ==========
    
    def obtener_tareas_por_usuario(self, usuario: str) -> List[Tarea]:
        """Obtiene tareas asignadas a un usuario específico"""
        return [t for t in self.tareas if t.usuario_asignado == usuario]
    
    def obtener_tareas_por_estado(self, estado: EstadoTarea) -> List[Tarea]:
        """Obtiene tareas por estado"""
        return [t for t in self.tareas if t.estado == estado]
    
    def obtener_tareas_por_prioridad(self, prioridad: PrioridadTarea) -> List[Tarea]:
        """Obtiene tareas por prioridad"""
        return [t for t in self.tareas if t.prioridad == prioridad]
    
    def obtener_tareas_vencidas(self) -> List[Tarea]:
        """Obtiene tareas vencidas"""
        return [t for t in self.tareas if t.esta_vencida()]
    
    def obtener_tareas_urgentes(self) -> List[Tarea]:
        """Obtiene tareas que necesitan atención urgente"""
        return [t for t in self.tareas if t.necesita_atencion()]
    
    def obtener_tareas_por_etiqueta(self, etiqueta: str) -> List[Tarea]:
        """Obtiene tareas que contienen una etiqueta específica"""
        etiqueta = etiqueta.lower().strip()
        return [t for t in self.tareas if etiqueta in t.etiquetas]
    
    def buscar_tareas(self, criterio: str) -> List[Tarea]:
        """Busca tareas por título o descripción"""
        criterio = criterio.lower().strip()
        if not criterio:
            return []
        
        resultados = []
        for tarea in self.tareas:
            if (criterio in tarea.titulo.lower() or 
                criterio in tarea.descripcion.lower() or
                criterio in tarea.usuario_asignado.lower()):
                resultados.append(tarea)
        
        return resultados
    
    def obtener_tareas_por_fecha_creacion(self, fecha_inicio: datetime.date, 
                                         fecha_fin: datetime.date) -> List[Tarea]:
        """Obtiene tareas creadas en un rango de fechas"""
        resultados = []
        for tarea in self.tareas:
            fecha_tarea = tarea.fecha_creacion.date()
            if fecha_inicio <= fecha_tarea <= fecha_fin:
                resultados.append(tarea)
        
        return resultados
    
    def obtener_tareas_con_vencimiento_proximo(self, dias: int = 3) -> List[Tarea]:
        """Obtiene tareas que vencen en los próximos N días"""
        resultados = []
        for tarea in self.tareas:
            if tarea.estado in [EstadoTarea.PENDIENTE, EstadoTarea.EN_PROGRESO]:
                dias_restantes = tarea.dias_para_vencimiento()
                if dias_restantes is not None and 0 <= dias_restantes <= dias:
                    resultados.append(tarea)
        
        return resultados
    
    # ========== ESTADÍSTICAS ==========
    
    def contar_tareas_por_estado(self) -> Dict[str, int]:
        """Cuenta tareas agrupadas por estado"""
        conteo = {}
        for estado in EstadoTarea:
            conteo[estado.value] = len(self.obtener_tareas_por_estado(estado))
        return conteo
    
    def contar_tareas_por_prioridad(self) -> Dict[str, int]:
        """Cuenta tareas agrupadas por prioridad"""
        conteo = {}
        for prioridad in PrioridadTarea:
            conteo[prioridad.value] = len(self.obtener_tareas_por_prioridad(prioridad))
        return conteo
    
    def contar_tareas_por_usuario(self) -> Dict[str, int]:
        """Cuenta tareas agrupadas por usuario"""
        conteo = {}
        for tarea in self.tareas:
            usuario = tarea.usuario_asignado
            conteo[usuario] = conteo.get(usuario, 0) + 1
        return conteo
    
    def obtener_estadisticas_generales(self) -> Dict[str, Any]:
        """Obtiene estadísticas generales del sistema"""
        total_tareas = len(self.tareas)
        tareas_activas = len(self.obtener_tareas_activas())
        tareas_completadas = len(self.obtener_tareas_por_estado(EstadoTarea.COMPLETADA))
        tareas_vencidas = len(self.obtener_tareas_vencidas())
        tareas_urgentes = len(self.obtener_tareas_urgentes())
        
        # Tiempo promedio de completado
        tareas_con_tiempo = [t for t in self.tareas 
                           if t.estado == EstadoTarea.COMPLETADA and t.duracion_en_progreso()]
        
        tiempo_promedio = None
        if tareas_con_tiempo:
            total_tiempo = sum(t.duracion_en_progreso().total_seconds() 
                             for t in tareas_con_tiempo)
            tiempo_promedio_segundos = total_tiempo / len(tareas_con_tiempo)
            tiempo_promedio = datetime.timedelta(seconds=tiempo_promedio_segundos)
        
        return {
            "total_tareas": total_tareas,
            "tareas_activas": tareas_activas,
            "tareas_completadas": tareas_completadas,
            "tareas_vencidas": tareas_vencidas,
            "tareas_urgentes": tareas_urgentes,
            "tasa_completado": (tareas_completadas / total_tareas * 100) if total_tareas > 0 else 0,
            "tiempo_promedio_completado": tiempo_promedio,
            "por_estado": self.contar_tareas_por_estado(),
            "por_prioridad": self.contar_tareas_por_prioridad(),
            "por_usuario": self.contar_tareas_por_usuario()
        }
    
    # ========== ORDENAMIENTO ==========
    
    def ordenar_por_prioridad(self, tareas: List[Tarea] = None) -> List[Tarea]:
        """Ordena tareas por prioridad (crítica primero)"""
        if tareas is None:
            tareas = self.tareas
        
        orden_prioridad = {
            PrioridadTarea.CRITICA: 0,
            PrioridadTarea.ALTA: 1,
            PrioridadTarea.MEDIA: 2,
            PrioridadTarea.BAJA: 3
        }
        
        return sorted(tareas, key=lambda t: orden_prioridad[t.prioridad])
    
    def ordenar_por_fecha_vencimiento(self, tareas: List[Tarea] = None) -> List[Tarea]:
        """Ordena tareas por fecha de vencimiento (próximas primero)"""
        if tareas is None:
            tareas = self.tareas
        
        # Separar tareas con y sin fecha de vencimiento
        con_vencimiento = [t for t in tareas if t.fecha_vencimiento is not None]
        sin_vencimiento = [t for t in tareas if t.fecha_vencimiento is None]
        
        # Ordenar las que tienen vencimiento
        con_vencimiento.sort(key=lambda t: t.fecha_vencimiento)
        
        # Devolver primero las que vencen, luego las que no tienen fecha
        return con_vencimiento + sin_vencimiento
    
    def ordenar_por_fecha_creacion(self, tareas: List[Tarea] = None, 
                                  descendente: bool = True) -> List[Tarea]:
        """Ordena tareas por fecha de creación"""
        if tareas is None:
            tareas = self.tareas
        
        return sorted(tareas, key=lambda t: t.fecha_creacion, reverse=descendente)
    
    # ========== PERSISTENCIA ==========
    
    def guardar_datos(self) -> bool:
        """Guarda las tareas en archivo JSON"""
        try:
            data = {
                "tareas": [tarea.to_dict() for tarea in self.tareas],
                "siguiente_id": self.siguiente_id,
                "fecha_guardado": datetime.datetime.now().isoformat()
            }
            
            with open(self.archivo_datos, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            return True
            
        except Exception as e:
            print(f"Error al guardar datos: {e}")
            return False
    
    def cargar_datos(self) -> bool:
        """Carga las tareas desde archivo JSON"""
        try:
            with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Cargar tareas
            self.tareas = []
            for tarea_data in data.get("tareas", []):
                tarea = Tarea.from_dict(tarea_data)
                self.tareas.append(tarea)
            
            # Cargar siguiente ID
            self.siguiente_id = data.get("siguiente_id", 1)
            
            # Asegurar que el siguiente_id sea mayor que cualquier ID existente
            if self.tareas:
                max_id = max(tarea.id for tarea in self.tareas)
                self.siguiente_id = max(self.siguiente_id, max_id + 1)
            
            return True
            
        except FileNotFoundError:
            # Archivo no existe, inicializar con datos vacíos
            self._inicializar_datos_ejemplo()
            return True
            
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            return False
    
    def _inicializar_datos_ejemplo(self):
        """Inicializa datos de ejemplo para demostración"""
        tareas_ejemplo = [
            {
                "titulo": "Implementar sistema de login",
                "descripcion": "Desarrollar autenticación de usuarios con JWT",
                "usuario": "dev1",
                "prioridad": PrioridadTarea.ALTA
            },
            {
                "titulo": "Diseñar interfaz de usuario",
                "descripcion": "Crear mockups y prototipos de la aplicación",
                "usuario": "designer1",
                "prioridad": PrioridadTarea.MEDIA
            },
            {
                "titulo": "Configurar base de datos",
                "descripcion": "Instalar y configurar PostgreSQL",
                "usuario": "dev2",
                "prioridad": PrioridadTarea.ALTA
            },
            {
                "titulo": "Escribir documentación",
                "descripcion": "Documentar APIs y procesos de desarrollo",
                "usuario": "dev1",
                "prioridad": PrioridadTarea.BAJA
            },
            {
                "titulo": "Pruebas de integración",
                "descripcion": "Implementar tests automatizados",
                "usuario": "qa1",
                "prioridad": PrioridadTarea.MEDIA
            }
        ]
        
        for tarea_data in tareas_ejemplo:
            tarea = self.crear_tarea(
                titulo=tarea_data["titulo"],
                descripcion=tarea_data["descripcion"],
                usuario_asignado=tarea_data["usuario"],
                prioridad=tarea_data["prioridad"]
            )
            
            # Agregar algunas etiquetas de ejemplo
            if "login" in tarea.titulo.lower():
                tarea.agregar_etiqueta("backend")
                tarea.agregar_etiqueta("seguridad")
            elif "interfaz" in tarea.titulo.lower() or "diseñar" in tarea.titulo.lower():
                tarea.agregar_etiqueta("frontend")
                tarea.agregar_etiqueta("ui/ux")
            elif "base de datos" in tarea.titulo.lower():
                tarea.agregar_etiqueta("backend")
                tarea.agregar_etiqueta("base-datos")
            elif "documentación" in tarea.titulo.lower():
                tarea.agregar_etiqueta("documentacion")
            elif "pruebas" in tarea.titulo.lower():
                tarea.agregar_etiqueta("testing")
                tarea.agregar_etiqueta("qa")
        
        # Cambiar estado de algunas tareas para demostrar variedad
        if len(self.tareas) >= 3:
            self.tareas[0].cambiar_estado(EstadoTarea.EN_PROGRESO)  # Login en progreso
            self.tareas[2].cambiar_estado(EstadoTarea.COMPLETADA)   # BD completada
        
        # Establecer fechas de vencimiento para algunas tareas
        fecha_futura = datetime.datetime.now() + datetime.timedelta(days=7)
        fecha_muy_futura = datetime.datetime.now() + datetime.timedelta(days=14)
        
        if len(self.tareas) >= 2:
            self.tareas[0].establecer_fecha_vencimiento(fecha_futura)
            self.tareas[1].establecer_fecha_vencimiento(fecha_muy_futura)
    
    def exportar_datos(self, formato: str = "json") -> str:
        """Exporta datos en diferentes formatos"""
        if formato.lower() == "json":
            return json.dumps([tarea.to_dict() for tarea in self.tareas], 
                            indent=2, ensure_ascii=False)
        elif formato.lower() == "csv":
            # Implementar exportación CSV si se necesita
            pass
        else:
            raise ValueError(f"Formato no soportado: {formato}")
    
    def limpiar_tareas_canceladas(self) -> int:
        """Elimina definitivamente las tareas canceladas"""
        tareas_canceladas = [t for t in self.tareas if t.estado == EstadoTarea.CANCELADA]
        count = len(tareas_canceladas)
        
        self.tareas = [t for t in self.tareas if t.estado != EstadoTarea.CANCELADA]
        
        return count
    
    def __len__(self) -> int:
        """Retorna el número total de tareas"""
        return len(self.tareas)
    
    def __iter__(self):
        """Permite iterar sobre las tareas"""
        return iter(self.tareas)
