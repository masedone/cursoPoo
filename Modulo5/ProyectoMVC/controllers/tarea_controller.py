"""
🎮 CONTROLADOR: Gestión de Tareas
Coordina entre Modelo y Vista
No contiene lógica de negocio ni presentación
"""

import datetime
from typing import List, Optional
from models.tarea import Tarea, EstadoTarea, PrioridadTarea
from models.tarea_repository import TareaRepository
from views.tarea_view import TareaView

class TareaController:
    """
    Controlador de Tareas - Solo coordinación
    Orquesta la comunicación entre Modelo y Vista
    """
    
    def __init__(self, repository: TareaRepository, view: TareaView):
        self.repository = repository
        self.view = view
        self.usuario_actual = "usuario1"  # Usuario por defecto
    
    # ========== GESTIÓN DE USUARIO ==========
    
    def cambiar_usuario(self, nuevo_usuario: str) -> bool:
        """Cambia el usuario actual del sistema"""
        if not nuevo_usuario.strip():
            self.view.mostrar_mensaje_error("El nombre de usuario no puede estar vacío")
            return False
        
        usuario_anterior = self.usuario_actual
        self.usuario_actual = nuevo_usuario.strip()
        
        self.view.mostrar_mensaje_exito(f"Usuario cambiado de '{usuario_anterior}' a '{self.usuario_actual}'")
        return True
    
    def obtener_usuario_actual(self) -> str:
        """Obtiene el usuario actual"""
        return self.usuario_actual
    
    # ========== OPERACIONES CRUD ==========
    
    def crear_tarea_interactiva(self) -> bool:
        """Crea una nueva tarea de forma interactiva"""
        try:
            self.view.mostrar_mensaje_info("Creando nueva tarea")
            
            # Solicitar datos básicos
            titulo = self.view.solicitar_entrada("Título de la tarea")
            if not titulo:
                self.view.mostrar_mensaje_error("El título es obligatorio")
                return False
            
            descripcion = self.view.solicitar_entrada("Descripción", requerido=False)
            if not descripcion:
                descripcion = "Sin descripción"
            
            # Solicitar usuario asignado
            usuario_asignado = self.view.solicitar_entrada(
                f"Usuario asignado (Enter para '{self.usuario_actual}')", 
                requerido=False
            )
            if not usuario_asignado:
                usuario_asignado = self.usuario_actual
            
            # Solicitar prioridad
            self.view.mostrar_opciones_prioridad()
            prioridad_idx = self.view.solicitar_numero("Seleccione prioridad", 1, len(PrioridadTarea))
            prioridad = list(PrioridadTarea)[prioridad_idx - 1]
            
            # Crear tarea usando el repositorio
            tarea = self.repository.crear_tarea(
                titulo=titulo,
                descripcion=descripcion,
                usuario_asignado=usuario_asignado,
                prioridad=prioridad
            )
            
            # Preguntar por fecha de vencimiento (opcional)
            if self.view.confirmar_accion("¿Desea establecer fecha de vencimiento?"):
                fecha_vencimiento = self.view.solicitar_fecha("Fecha de vencimiento")
                if fecha_vencimiento:
                    if not tarea.establecer_fecha_vencimiento(fecha_vencimiento):
                        self.view.mostrar_mensaje_advertencia("No se pudo establecer la fecha de vencimiento")
            
            # Preguntar por etiquetas (opcional)
            if self.view.confirmar_accion("¿Desea agregar etiquetas?"):
                etiquetas_str = self.view.solicitar_entrada("Etiquetas (separadas por comas)", requerido=False)
                if etiquetas_str:
                    etiquetas = [e.strip() for e in etiquetas_str.split(",") if e.strip()]
                    for etiqueta in etiquetas:
                        tarea.agregar_etiqueta(etiqueta)
            
            # Mostrar tarea creada
            self.view.mostrar_mensaje_exito(f"Tarea '{titulo}' creada exitosamente con ID: {tarea.id}")
            self.view.mostrar_tarea_detalle(tarea)
            
            return True
            
        except Exception as e:
            self.view.mostrar_mensaje_error(f"Error al crear tarea: {e}")
            return False
    
    def ver_tarea_por_id(self, tarea_id: int = None) -> bool:
        """Muestra una tarea específica por ID"""
        try:
            if tarea_id is None:
                tarea_id = self.view.solicitar_numero("ID de la tarea a ver")
            
            tarea = self.repository.obtener_tarea_por_id(tarea_id)
            if not tarea:
                self.view.mostrar_mensaje_error(f"No se encontró tarea con ID: {tarea_id}")
                return False
            
            self.view.mostrar_tarea_detalle(tarea)
            return True
            
        except Exception as e:
            self.view.mostrar_mensaje_error(f"Error al mostrar tarea: {e}")
            return False
    
    def modificar_tarea_interactiva(self) -> bool:
        """Modifica una tarea de forma interactiva"""
        try:
            tarea_id = self.view.solicitar_numero("ID de la tarea a modificar")
            tarea = self.repository.obtener_tarea_por_id(tarea_id)
            
            if not tarea:
                self.view.mostrar_mensaje_error(f"No se encontró tarea con ID: {tarea_id}")
                return False
            
            # Mostrar tarea actual
            self.view.mostrar_mensaje_info("Tarea actual:")
            self.view.mostrar_tarea_detalle(tarea)
            
            # Menú de modificaciones
            while True:
                print(f"\n✏️ ¿QUÉ DESEA MODIFICAR?")
                print("1. Estado")
                print("2. Prioridad")
                print("3. Usuario asignado")
                print("4. Título")
                print("5. Descripción")
                print("6. Fecha de vencimiento")
                print("7. Agregar etiqueta")
                print("8. Remover etiqueta")
                print("9. Agregar comentario")
                print("10. Tiempo estimado")
                print("11. Registrar tiempo trabajado")
                print("12. Terminar modificaciones")
                
                opcion = self.view.solicitar_numero("Seleccione opción", 1, 12)
                
                if opcion == 1:
                    self._modificar_estado_tarea(tarea)
                elif opcion == 2:
                    self._modificar_prioridad_tarea(tarea)
                elif opcion == 3:
                    self._modificar_usuario_tarea(tarea)
                elif opcion == 4:
                    self._modificar_titulo_tarea(tarea)
                elif opcion == 5:
                    self._modificar_descripcion_tarea(tarea)
                elif opcion == 6:
                    self._modificar_fecha_vencimiento_tarea(tarea)
                elif opcion == 7:
                    self._agregar_etiqueta_tarea(tarea)
                elif opcion == 8:
                    self._remover_etiqueta_tarea(tarea)
                elif opcion == 9:
                    self._agregar_comentario_tarea(tarea)
                elif opcion == 10:
                    self._modificar_tiempo_estimado_tarea(tarea)
                elif opcion == 11:
                    self._registrar_tiempo_trabajado_tarea(tarea)
                elif opcion == 12:
                    break
            
            # Actualizar en repositorio
            self.repository.actualizar_tarea(tarea)
            self.view.mostrar_mensaje_exito("Tarea actualizada exitosamente")
            
            return True
            
        except Exception as e:
            self.view.mostrar_mensaje_error(f"Error al modificar tarea: {e}")
            return False
    
    def eliminar_tarea_interactiva(self) -> bool:
        """Elimina una tarea de forma interactiva"""
        try:
            tarea_id = self.view.solicitar_numero("ID de la tarea a eliminar")
            tarea = self.repository.obtener_tarea_por_id(tarea_id)
            
            if not tarea:
                self.view.mostrar_mensaje_error(f"No se encontró tarea con ID: {tarea_id}")
                return False
            
            # Mostrar tarea a eliminar
            self.view.mostrar_mensaje_info("Tarea a eliminar:")
            self.view.mostrar_tarea_detalle(tarea)
            
            # Confirmar eliminación
            if not self.view.confirmar_accion(f"¿Está seguro de eliminar la tarea '{tarea.titulo}'?"):
                self.view.mostrar_mensaje_info("Eliminación cancelada")
                return False
            
            # Preguntar tipo de eliminación
            print(f"\n🗑️ TIPO DE ELIMINACIÓN:")
            print("1. Marcar como cancelada (recomendado)")
            print("2. Eliminar definitivamente")
            
            tipo_eliminacion = self.view.solicitar_numero("Seleccione tipo", 1, 2)
            
            if tipo_eliminacion == 1:
                # Marcar como cancelada
                if self.repository.eliminar_tarea(tarea_id):
                    self.view.mostrar_mensaje_exito(f"Tarea '{tarea.titulo}' marcada como cancelada")
                else:
                    self.view.mostrar_mensaje_error("No se pudo cancelar la tarea")
                    return False
            else:
                # Eliminar definitivamente
                if self.repository.eliminar_definitivamente(tarea_id):
                    self.view.mostrar_mensaje_exito(f"Tarea '{tarea.titulo}' eliminada definitivamente")
                else:
                    self.view.mostrar_mensaje_error("No se pudo eliminar la tarea")
                    return False
            
            return True
            
        except Exception as e:
            self.view.mostrar_mensaje_error(f"Error al eliminar tarea: {e}")
            return False
    
    # ========== CONSULTAS Y FILTROS ==========
    
    def listar_todas_tareas(self):
        """Lista todas las tareas"""
        tareas = self.repository.obtener_todas_tareas()
        tareas_ordenadas = self.repository.ordenar_por_prioridad(tareas)
        self.view.mostrar_lista_tareas(tareas_ordenadas, "Todas las Tareas")
    
    def listar_mis_tareas(self):
        """Lista las tareas del usuario actual"""
        tareas = self.repository.obtener_tareas_por_usuario(self.usuario_actual)
        tareas_ordenadas = self.repository.ordenar_por_prioridad(tareas)
        self.view.mostrar_lista_tareas(tareas_ordenadas, f"Tareas de {self.usuario_actual}")
    
    def buscar_tareas_interactivo(self):
        """Busca tareas de forma interactiva"""
        criterio = self.view.solicitar_entrada("Criterio de búsqueda (título, descripción o usuario)")
        
        if not criterio:
            self.view.mostrar_mensaje_error("Debe ingresar un criterio de búsqueda")
            return
        
        tareas = self.repository.buscar_tareas(criterio)
        self.view.mostrar_lista_tareas(tareas, f"Resultados para: '{criterio}'")
    
    def filtrar_tareas_interactivo(self):
        """Filtra tareas de forma interactiva"""
        while True:
            self.view.mostrar_menu_filtros()
            opcion = self.view.solicitar_numero("Seleccione filtro", 1, 9)
            
            if opcion == 1:
                self._filtrar_por_estado()
            elif opcion == 2:
                self._filtrar_por_prioridad()
            elif opcion == 3:
                self._filtrar_por_usuario()
            elif opcion == 4:
                self._filtrar_por_etiqueta()
            elif opcion == 5:
                self._mostrar_tareas_vencidas()
            elif opcion == 6:
                self._mostrar_tareas_urgentes()
            elif opcion == 7:
                self._mostrar_tareas_proximas()
            elif opcion == 8:
                self._mostrar_tareas_completadas_hoy()
            elif opcion == 9:
                break
    
    # ========== REPORTES Y ESTADÍSTICAS ==========
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas del sistema"""
        estadisticas = self.repository.obtener_estadisticas_generales()
        self.view.mostrar_estadisticas(estadisticas)
    
    def mostrar_dashboard(self):
        """Muestra el dashboard principal"""
        # Obtener datos para el dashboard
        estadisticas = self.repository.obtener_estadisticas_generales()
        tareas_urgentes = self.repository.obtener_tareas_urgentes()
        tareas_vencidas = self.repository.obtener_tareas_vencidas()
        tareas_proximas = self.repository.obtener_tareas_con_vencimiento_proximo(3)
        
        # Mostrar dashboard
        self.view.mostrar_dashboard(estadisticas, tareas_urgentes, tareas_vencidas, tareas_proximas)
    
    def mostrar_tareas_por_estado(self):
        """Muestra tareas agrupadas por estado"""
        tareas_por_estado = {}
        for estado in EstadoTarea:
            tareas_por_estado[estado] = self.repository.obtener_tareas_por_estado(estado)
        
        self.view.mostrar_tareas_por_estado(tareas_por_estado)
    
    def mostrar_tareas_por_usuario(self):
        """Muestra tareas agrupadas por usuario"""
        estadisticas = self.repository.obtener_estadisticas_generales()
        usuarios = estadisticas['por_usuario'].keys()
        
        tareas_por_usuario = {}
        for usuario in usuarios:
            tareas_por_usuario[usuario] = self.repository.obtener_tareas_por_usuario(usuario)
        
        self.view.mostrar_tareas_por_usuario(tareas_por_usuario)
    
    # ========== PERSISTENCIA ==========
    
    def guardar_datos(self) -> bool:
        """Guarda los datos del sistema"""
        if self.repository.guardar_datos():
            self.view.mostrar_mensaje_exito("Datos guardados exitosamente")
            return True
        else:
            self.view.mostrar_mensaje_error("Error al guardar datos")
            return False
    
    def limpiar_tareas_canceladas(self) -> bool:
        """Limpia las tareas canceladas del sistema"""
        if not self.view.confirmar_accion("¿Desea eliminar definitivamente todas las tareas canceladas?"):
            return False
        
        cantidad = self.repository.limpiar_tareas_canceladas()
        if cantidad > 0:
            self.view.mostrar_mensaje_exito(f"Se eliminaron {cantidad} tareas canceladas")
        else:
            self.view.mostrar_mensaje_info("No hay tareas canceladas para eliminar")
        
        return True
    
    # ========== MÉTODOS AUXILIARES PARA MODIFICACIONES ==========
    
    def _modificar_estado_tarea(self, tarea: Tarea):
        """Modifica el estado de una tarea"""
        self.view.mostrar_opciones_estado()
        estado_idx = self.view.solicitar_numero("Nuevo estado", 1, len(EstadoTarea))
        nuevo_estado = list(EstadoTarea)[estado_idx - 1]
        
        if tarea.cambiar_estado(nuevo_estado):
            self.view.mostrar_mensaje_exito(f"Estado cambiado a: {nuevo_estado.value}")
        else:
            self.view.mostrar_mensaje_error("No se puede cambiar a ese estado")
    
    def _modificar_prioridad_tarea(self, tarea: Tarea):
        """Modifica la prioridad de una tarea"""
        self.view.mostrar_opciones_prioridad()
        prioridad_idx = self.view.solicitar_numero("Nueva prioridad", 1, len(PrioridadTarea))
        nueva_prioridad = list(PrioridadTarea)[prioridad_idx - 1]
        
        if tarea.cambiar_prioridad(nueva_prioridad):
            self.view.mostrar_mensaje_exito(f"Prioridad cambiada a: {nueva_prioridad.value}")
        else:
            self.view.mostrar_mensaje_error("No se puede cambiar la prioridad")
    
    def _modificar_usuario_tarea(self, tarea: Tarea):
        """Modifica el usuario asignado de una tarea"""
        nuevo_usuario = self.view.solicitar_entrada("Nuevo usuario asignado")
        
        if tarea.asignar_usuario(nuevo_usuario):
            self.view.mostrar_mensaje_exito(f"Usuario asignado cambiado a: {nuevo_usuario}")
        else:
            self.view.mostrar_mensaje_error("No se puede cambiar el usuario asignado")
    
    def _modificar_titulo_tarea(self, tarea: Tarea):
        """Modifica el título de una tarea"""
        nuevo_titulo = self.view.solicitar_entrada("Nuevo título")
        
        if nuevo_titulo:
            tarea.titulo = nuevo_titulo
            self.view.mostrar_mensaje_exito("Título actualizado")
    
    def _modificar_descripcion_tarea(self, tarea: Tarea):
        """Modifica la descripción de una tarea"""
        nueva_descripcion = self.view.solicitar_entrada("Nueva descripción", requerido=False)
        
        tarea.descripcion = nueva_descripcion or "Sin descripción"
        self.view.mostrar_mensaje_exito("Descripción actualizada")
    
    def _modificar_fecha_vencimiento_tarea(self, tarea: Tarea):
        """Modifica la fecha de vencimiento de una tarea"""
        fecha_vencimiento = self.view.solicitar_fecha("Nueva fecha de vencimiento")
        
        if fecha_vencimiento:
            if tarea.establecer_fecha_vencimiento(fecha_vencimiento):
                self.view.mostrar_mensaje_exito("Fecha de vencimiento actualizada")
            else:
                self.view.mostrar_mensaje_error("No se pudo establecer la fecha de vencimiento")
        else:
            tarea.fecha_vencimiento = None
            self.view.mostrar_mensaje_exito("Fecha de vencimiento eliminada")
    
    def _agregar_etiqueta_tarea(self, tarea: Tarea):
        """Agrega una etiqueta a una tarea"""
        etiqueta = self.view.solicitar_entrada("Nueva etiqueta")
        
        if tarea.agregar_etiqueta(etiqueta):
            self.view.mostrar_mensaje_exito(f"Etiqueta '{etiqueta}' agregada")
        else:
            self.view.mostrar_mensaje_error("La etiqueta ya existe o es inválida")
    
    def _remover_etiqueta_tarea(self, tarea: Tarea):
        """Remueve una etiqueta de una tarea"""
        if not tarea.etiquetas:
            self.view.mostrar_mensaje_info("La tarea no tiene etiquetas")
            return
        
        self.view.mostrar_mensaje_info(f"Etiquetas actuales: {', '.join(tarea.etiquetas)}")
        etiqueta = self.view.solicitar_entrada("Etiqueta a remover")
        
        if tarea.remover_etiqueta(etiqueta):
            self.view.mostrar_mensaje_exito(f"Etiqueta '{etiqueta}' removida")
        else:
            self.view.mostrar_mensaje_error("Etiqueta no encontrada")
    
    def _agregar_comentario_tarea(self, tarea: Tarea):
        """Agrega un comentario a una tarea"""
        comentario = self.view.solicitar_entrada("Comentario")
        
        if tarea.agregar_comentario(comentario, self.usuario_actual):
            self.view.mostrar_mensaje_exito("Comentario agregado")
        else:
            self.view.mostrar_mensaje_error("No se pudo agregar el comentario")
    
    def _modificar_tiempo_estimado_tarea(self, tarea: Tarea):
        """Modifica el tiempo estimado de una tarea"""
        try:
            horas = float(self.view.solicitar_entrada("Tiempo estimado en horas"))
            
            if tarea.establecer_tiempo_estimado(horas):
                self.view.mostrar_mensaje_exito(f"Tiempo estimado establecido: {horas} horas")
            else:
                self.view.mostrar_mensaje_error("Tiempo inválido")
        except ValueError:
            self.view.mostrar_mensaje_error("Por favor ingrese un número válido")
    
    def _registrar_tiempo_trabajado_tarea(self, tarea: Tarea):
        """Registra tiempo trabajado en una tarea"""
        try:
            horas = float(self.view.solicitar_entrada("Horas trabajadas"))
            
            if tarea.registrar_tiempo_real(horas):
                total = tarea.tiempo_real_horas or 0
                self.view.mostrar_mensaje_exito(f"Tiempo registrado. Total: {total} horas")
            else:
                self.view.mostrar_mensaje_error("Tiempo inválido")
        except ValueError:
            self.view.mostrar_mensaje_error("Por favor ingrese un número válido")
    
    # ========== MÉTODOS AUXILIARES PARA FILTROS ==========
    
    def _filtrar_por_estado(self):
        """Filtra tareas por estado"""
        self.view.mostrar_opciones_estado()
        estado_idx = self.view.solicitar_numero("Estado a filtrar", 1, len(EstadoTarea))
        estado = list(EstadoTarea)[estado_idx - 1]
        
        tareas = self.repository.obtener_tareas_por_estado(estado)
        self.view.mostrar_lista_tareas(tareas, f"Tareas con estado: {estado.value}")
    
    def _filtrar_por_prioridad(self):
        """Filtra tareas por prioridad"""
        self.view.mostrar_opciones_prioridad()
        prioridad_idx = self.view.solicitar_numero("Prioridad a filtrar", 1, len(PrioridadTarea))
        prioridad = list(PrioridadTarea)[prioridad_idx - 1]
        
        tareas = self.repository.obtener_tareas_por_prioridad(prioridad)
        self.view.mostrar_lista_tareas(tareas, f"Tareas con prioridad: {prioridad.value}")
    
    def _filtrar_por_usuario(self):
        """Filtra tareas por usuario"""
        usuario = self.view.solicitar_entrada("Usuario a filtrar")
        tareas = self.repository.obtener_tareas_por_usuario(usuario)
        self.view.mostrar_lista_tareas(tareas, f"Tareas de: {usuario}")
    
    def _filtrar_por_etiqueta(self):
        """Filtra tareas por etiqueta"""
        etiqueta = self.view.solicitar_entrada("Etiqueta a filtrar")
        tareas = self.repository.obtener_tareas_por_etiqueta(etiqueta)
        self.view.mostrar_lista_tareas(tareas, f"Tareas con etiqueta: #{etiqueta}")
    
    def _mostrar_tareas_vencidas(self):
        """Muestra tareas vencidas"""
        tareas = self.repository.obtener_tareas_vencidas()
        self.view.mostrar_lista_tareas(tareas, "Tareas Vencidas")
    
    def _mostrar_tareas_urgentes(self):
        """Muestra tareas urgentes"""
        tareas = self.repository.obtener_tareas_urgentes()
        self.view.mostrar_lista_tareas(tareas, "Tareas Urgentes")
    
    def _mostrar_tareas_proximas(self):
        """Muestra tareas que vencen pronto"""
        dias = self.view.solicitar_numero("Días para considerar 'próximo'", 1, 30)
        tareas = self.repository.obtener_tareas_con_vencimiento_proximo(dias)
        self.view.mostrar_lista_tareas(tareas, f"Tareas que vencen en {dias} días")
    
    def _mostrar_tareas_completadas_hoy(self):
        """Muestra tareas completadas hoy"""
        hoy = datetime.date.today()
        tareas = self.repository.obtener_tareas_por_fecha_creacion(hoy, hoy)
        tareas_completadas = [t for t in tareas if t.estado == EstadoTarea.COMPLETADA]
        self.view.mostrar_lista_tareas(tareas_completadas, "Tareas Completadas Hoy")
