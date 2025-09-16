"""
👁️ VISTA: Presentación de Tareas
Solo se encarga de mostrar información al usuario
No contiene lógica de negocio ni coordinación
"""

import datetime
from typing import List, Dict, Any
from models.tarea import Tarea, EstadoTarea, PrioridadTarea

class TareaView:
    """
    Vista de Tareas - Solo presentación
    No maneja datos ni coordinación
    """
    
    def __init__(self):
        # Configuración de presentación
        self.iconos_estado = {
            EstadoTarea.PENDIENTE: "⏳",
            EstadoTarea.EN_PROGRESO: "🔄",
            EstadoTarea.COMPLETADA: "✅",
            EstadoTarea.CANCELADA: "❌"
        }
        
        self.iconos_prioridad = {
            PrioridadTarea.BAJA: "🟢",
            PrioridadTarea.MEDIA: "🟡",
            PrioridadTarea.ALTA: "🔴",
            PrioridadTarea.CRITICA: "🚨"
        }
        
        self.colores_estado = {
            EstadoTarea.PENDIENTE: "blanco",
            EstadoTarea.EN_PROGRESO: "azul",
            EstadoTarea.COMPLETADA: "verde",
            EstadoTarea.CANCELADA: "rojo"
        }
    
    # ========== PRESENTACIÓN DE TAREAS ==========
    
    def mostrar_tarea_detalle(self, tarea: Tarea):
        """Muestra una tarea con todos sus detalles"""
        print(f"\n📋 DETALLE DE TAREA")
        print("="*40)
        
        # Información básica
        print(f"🆔 ID: {tarea.id}")
        print(f"📝 Título: {tarea.titulo}")
        print(f"📄 Descripción: {tarea.descripcion}")
        print(f"👤 Asignado a: {tarea.usuario_asignado}")
        print(f"👨‍💼 Creado por: {tarea.usuario_creador}")
        
        # Estado y prioridad
        icono_estado = self.iconos_estado[tarea.estado]
        icono_prioridad = self.iconos_prioridad[tarea.prioridad]
        
        print(f"📊 Estado: {icono_estado} {tarea.estado.value.title()}")
        print(f"⚡ Prioridad: {icono_prioridad} {tarea.prioridad.value.title()}")
        
        # Fechas
        print(f"📅 Creado: {self._formatear_fecha(tarea.fecha_creacion)}")
        
        if tarea.fecha_inicio:
            print(f"🚀 Iniciado: {self._formatear_fecha(tarea.fecha_inicio)}")
        
        if tarea.fecha_completado:
            print(f"🏁 Completado: {self._formatear_fecha(tarea.fecha_completado)}")
        
        if tarea.fecha_vencimiento:
            print(f"⏰ Vence: {self._formatear_fecha(tarea.fecha_vencimiento)}")
            
            # Mostrar días restantes
            dias_restantes = tarea.dias_para_vencimiento()
            if dias_restantes is not None:
                if dias_restantes < 0:
                    print(f"   🔴 VENCIDA hace {abs(dias_restantes)} días")
                elif dias_restantes == 0:
                    print(f"   ⚠️ VENCE HOY")
                elif dias_restantes <= 3:
                    print(f"   🟡 Vence en {dias_restantes} días")
                else:
                    print(f"   🟢 Vence en {dias_restantes} días")
        
        # Tiempo
        if tarea.tiempo_estimado_horas:
            print(f"⏱️ Tiempo estimado: {tarea.tiempo_estimado_horas} horas")
        
        if tarea.tiempo_real_horas:
            print(f"⏲️ Tiempo real: {tarea.tiempo_real_horas} horas")
        
        # Duración en progreso
        duracion = tarea.duracion_en_progreso()
        if duracion:
            print(f"⌛ Tiempo en progreso: {self._formatear_duracion(duracion)}")
        
        # Etiquetas
        if tarea.etiquetas:
            etiquetas_str = " ".join(f"#{tag}" for tag in tarea.etiquetas)
            print(f"🏷️ Etiquetas: {etiquetas_str}")
        
        # Alertas
        if tarea.necesita_atencion():
            print(f"\n🚨 NECESITA ATENCIÓN URGENTE")
        
        # Comentarios
        if tarea.comentarios:
            print(f"\n💬 COMENTARIOS ({len(tarea.comentarios)}):")
            for comentario in tarea.comentarios[-3:]:  # Mostrar últimos 3
                fecha_comentario = self._formatear_fecha(comentario["fecha"], incluir_hora=True)
                print(f"   • {comentario['usuario']} ({fecha_comentario}):")
                print(f"     {comentario['texto']}")
            
            if len(tarea.comentarios) > 3:
                print(f"   ... y {len(tarea.comentarios) - 3} comentarios más")
    
    def mostrar_lista_tareas(self, tareas: List[Tarea], titulo: str = "Lista de Tareas"):
        """Muestra una lista resumida de tareas"""
        if not tareas:
            print(f"\n📭 {titulo}")
            print("No hay tareas para mostrar")
            return
        
        print(f"\n📋 {titulo.upper()}")
        print("="*70)
        print(f"Total: {len(tareas)} tareas")
        print()
        
        # Encabezado de tabla
        print(f"{'ID':<4} {'Estado':<8} {'Prioridad':<10} {'Título':<25} {'Usuario':<12} {'Vence'}")
        print("-"*70)
        
        for tarea in tareas:
            # Iconos
            icono_estado = self.iconos_estado[tarea.estado]
            icono_prioridad = self.iconos_prioridad[tarea.prioridad]
            
            # Formato de fecha de vencimiento
            if tarea.fecha_vencimiento:
                fecha_venc = tarea.fecha_vencimiento.strftime("%d/%m")
                if tarea.esta_vencida():
                    fecha_venc = f"🔴{fecha_venc}"
                elif tarea.dias_para_vencimiento() <= 3:
                    fecha_venc = f"🟡{fecha_venc}"
                else:
                    fecha_venc = f"🟢{fecha_venc}"
            else:
                fecha_venc = "-"
            
            # Título truncado
            titulo_corto = (tarea.titulo[:22] + "...") if len(tarea.titulo) > 25 else tarea.titulo
            
            print(f"{tarea.id:<4} {icono_estado:<8} {icono_prioridad:<10} {titulo_corto:<25} "
                  f"{tarea.usuario_asignado:<12} {fecha_venc}")
    
    def mostrar_lista_compacta(self, tareas: List[Tarea], titulo: str = "Tareas"):
        """Muestra una lista muy compacta de tareas"""
        if not tareas:
            print(f"📭 {titulo}: Sin tareas")
            return
        
        print(f"\n{titulo} ({len(tareas)}):")
        for tarea in tareas:
            icono_estado = self.iconos_estado[tarea.estado]
            icono_prioridad = self.iconos_prioridad[tarea.prioridad]
            
            alerta = ""
            if tarea.necesita_atencion():
                alerta = " 🚨"
            elif tarea.esta_vencida():
                alerta = " 🔴"
            
            print(f"  {icono_estado} {icono_prioridad} {tarea.id:2d}. {tarea.titulo}{alerta}")
    
    def mostrar_tareas_por_estado(self, tareas_por_estado: Dict[EstadoTarea, List[Tarea]]):
        """Muestra tareas agrupadas por estado"""
        print(f"\n📊 TAREAS POR ESTADO")
        print("="*40)
        
        for estado in EstadoTarea:
            tareas = tareas_por_estado.get(estado, [])
            icono = self.iconos_estado[estado]
            
            if tareas:
                self.mostrar_lista_compacta(tareas, f"{icono} {estado.value.title()}")
            else:
                print(f"\n{icono} {estado.value.title()}: Sin tareas")
    
    def mostrar_tareas_por_usuario(self, tareas_por_usuario: Dict[str, List[Tarea]]):
        """Muestra tareas agrupadas por usuario"""
        print(f"\n👥 TAREAS POR USUARIO")
        print("="*35)
        
        for usuario, tareas in tareas_por_usuario.items():
            if tareas:
                self.mostrar_lista_compacta(tareas, f"👤 {usuario}")
            else:
                print(f"\n👤 {usuario}: Sin tareas")
    
    # ========== ESTADÍSTICAS Y REPORTES ==========
    
    def mostrar_estadisticas(self, estadisticas: Dict[str, Any]):
        """Muestra estadísticas del sistema"""
        print(f"\n📊 ESTADÍSTICAS DEL SISTEMA")
        print("="*35)
        
        # Estadísticas generales
        print(f"📋 Total de tareas: {estadisticas['total_tareas']}")
        print(f"🔄 Tareas activas: {estadisticas['tareas_activas']}")
        print(f"✅ Tareas completadas: {estadisticas['tareas_completadas']}")
        print(f"🔴 Tareas vencidas: {estadisticas['tareas_vencidas']}")
        print(f"🚨 Tareas urgentes: {estadisticas['tareas_urgentes']}")
        print(f"📈 Tasa de completado: {estadisticas['tasa_completado']:.1f}%")
        
        if estadisticas['tiempo_promedio_completado']:
            tiempo_promedio = estadisticas['tiempo_promedio_completado']
            print(f"⏱️ Tiempo promedio: {self._formatear_duracion(tiempo_promedio)}")
        
        # Por estado
        print(f"\n📊 DISTRIBUCIÓN POR ESTADO:")
        for estado, cantidad in estadisticas['por_estado'].items():
            icono = self.iconos_estado[EstadoTarea(estado)]
            porcentaje = (cantidad / estadisticas['total_tareas'] * 100) if estadisticas['total_tareas'] > 0 else 0
            print(f"   {icono} {estado.title()}: {cantidad} ({porcentaje:.1f}%)")
        
        # Por prioridad
        print(f"\n⚡ DISTRIBUCIÓN POR PRIORIDAD:")
        for prioridad, cantidad in estadisticas['por_prioridad'].items():
            icono = self.iconos_prioridad[PrioridadTarea(prioridad)]
            porcentaje = (cantidad / estadisticas['total_tareas'] * 100) if estadisticas['total_tareas'] > 0 else 0
            print(f"   {icono} {prioridad.title()}: {cantidad} ({porcentaje:.1f}%)")
        
        # Por usuario
        if estadisticas['por_usuario']:
            print(f"\n👥 DISTRIBUCIÓN POR USUARIO:")
            for usuario, cantidad in sorted(estadisticas['por_usuario'].items(), 
                                          key=lambda x: x[1], reverse=True):
                porcentaje = (cantidad / estadisticas['total_tareas'] * 100) if estadisticas['total_tareas'] > 0 else 0
                print(f"   👤 {usuario}: {cantidad} ({porcentaje:.1f}%)")
    
    def mostrar_dashboard(self, estadisticas: Dict[str, Any], tareas_urgentes: List[Tarea],
                         tareas_vencidas: List[Tarea], tareas_proximas: List[Tarea]):
        """Muestra un dashboard completo"""
        print(f"\n🏠 DASHBOARD DE TAREAS")
        print("="*50)
        
        # Resumen rápido
        print(f"📊 RESUMEN:")
        print(f"   Total: {estadisticas['total_tareas']} | "
              f"Activas: {estadisticas['tareas_activas']} | "
              f"Completadas: {estadisticas['tareas_completadas']} | "
              f"Urgentes: {estadisticas['tareas_urgentes']}")
        
        # Tareas que requieren atención
        if tareas_urgentes:
            self.mostrar_lista_compacta(tareas_urgentes, "🚨 REQUIEREN ATENCIÓN URGENTE")
        
        if tareas_vencidas:
            self.mostrar_lista_compacta(tareas_vencidas, "🔴 TAREAS VENCIDAS")
        
        if tareas_proximas:
            self.mostrar_lista_compacta(tareas_proximas, "⏰ VENCEN PRONTO")
        
        if not tareas_urgentes and not tareas_vencidas and not tareas_proximas:
            print(f"\n🟢 ¡Todo bajo control! No hay tareas urgentes.")
    
    # ========== MENÚS E INTERFAZ ==========
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal del sistema"""
        print(f"\n🏗️ SISTEMA MVC - GESTIÓN DE TAREAS")
        print("="*40)
        print("1. 📋 Ver todas las tareas")
        print("2. 👤 Ver mis tareas")
        print("3. 🔍 Buscar tareas")
        print("4. ➕ Crear nueva tarea")
        print("5. ✏️ Modificar tarea")
        print("6. 🗑️ Eliminar tarea")
        print("7. 📊 Ver estadísticas")
        print("8. 🏠 Dashboard")
        print("9. ⚙️ Configuración")
        print("10. 💾 Guardar datos")
        print("11. 🚪 Salir")
        print("-"*40)
    
    def mostrar_menu_filtros(self):
        """Muestra opciones de filtrado"""
        print(f"\n🔍 FILTROS DISPONIBLES")
        print("="*25)
        print("1. Por estado")
        print("2. Por prioridad")
        print("3. Por usuario")
        print("4. Por etiqueta")
        print("5. Tareas vencidas")
        print("6. Tareas urgentes")
        print("7. Vencen pronto")
        print("8. Completadas hoy")
        print("9. Volver")
    
    def mostrar_opciones_estado(self):
        """Muestra opciones de estado"""
        print(f"\n📊 ESTADOS DISPONIBLES")
        print("="*25)
        for i, estado in enumerate(EstadoTarea, 1):
            icono = self.iconos_estado[estado]
            print(f"{i}. {icono} {estado.value.title()}")
    
    def mostrar_opciones_prioridad(self):
        """Muestra opciones de prioridad"""
        print(f"\n⚡ PRIORIDADES DISPONIBLES")
        print("="*30)
        for i, prioridad in enumerate(PrioridadTarea, 1):
            icono = self.iconos_prioridad[prioridad]
            print(f"{i}. {icono} {prioridad.value.title()}")
    
    # ========== MENSAJES Y NOTIFICACIONES ==========
    
    def mostrar_mensaje_exito(self, mensaje: str):
        """Muestra mensaje de éxito"""
        print(f"✅ {mensaje}")
    
    def mostrar_mensaje_error(self, mensaje: str):
        """Muestra mensaje de error"""
        print(f"❌ {mensaje}")
    
    def mostrar_mensaje_advertencia(self, mensaje: str):
        """Muestra mensaje de advertencia"""
        print(f"⚠️ {mensaje}")
    
    def mostrar_mensaje_info(self, mensaje: str):
        """Muestra mensaje informativo"""
        print(f"ℹ️ {mensaje}")
    
    def confirmar_accion(self, mensaje: str) -> bool:
        """Solicita confirmación del usuario"""
        respuesta = input(f"❓ {mensaje} (s/n): ").lower().strip()
        return respuesta in ['s', 'si', 'sí', 'y', 'yes']
    
    def solicitar_entrada(self, prompt: str, requerido: bool = True) -> str:
        """Solicita entrada del usuario"""
        while True:
            valor = input(f"📝 {prompt}: ").strip()
            if valor or not requerido:
                return valor
            print("❌ Este campo es obligatorio")
    
    def solicitar_numero(self, prompt: str, minimo: int = None, maximo: int = None) -> int:
        """Solicita un número del usuario"""
        while True:
            try:
                valor = int(input(f"🔢 {prompt}: "))
                
                if minimo is not None and valor < minimo:
                    print(f"❌ El valor debe ser mayor o igual a {minimo}")
                    continue
                
                if maximo is not None and valor > maximo:
                    print(f"❌ El valor debe ser menor o igual a {maximo}")
                    continue
                
                return valor
                
            except ValueError:
                print("❌ Por favor ingrese un número válido")
    
    def solicitar_fecha(self, prompt: str) -> datetime.datetime:
        """Solicita una fecha del usuario"""
        while True:
            fecha_str = input(f"📅 {prompt} (YYYY-MM-DD HH:MM o YYYY-MM-DD): ").strip()
            
            if not fecha_str:
                return None
            
            try:
                # Intentar con hora
                if len(fecha_str) > 10:
                    return datetime.datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
                else:
                    # Solo fecha, asumir medianoche
                    fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
                    return fecha.replace(hour=23, minute=59)  # Final del día
                    
            except ValueError:
                print("❌ Formato de fecha inválido. Use YYYY-MM-DD o YYYY-MM-DD HH:MM")
    
    # ========== UTILIDADES DE FORMATO ==========
    
    def _formatear_fecha(self, fecha: datetime.datetime, incluir_hora: bool = False) -> str:
        """Formatea una fecha para mostrar"""
        if incluir_hora:
            return fecha.strftime("%d/%m/%Y %H:%M")
        else:
            return fecha.strftime("%d/%m/%Y")
    
    def _formatear_duracion(self, duracion: datetime.timedelta) -> str:
        """Formatea una duración para mostrar"""
        total_segundos = int(duracion.total_seconds())
        
        dias = total_segundos // 86400
        horas = (total_segundos % 86400) // 3600
        minutos = (total_segundos % 3600) // 60
        
        partes = []
        if dias > 0:
            partes.append(f"{dias}d")
        if horas > 0:
            partes.append(f"{horas}h")
        if minutos > 0:
            partes.append(f"{minutos}m")
        
        return " ".join(partes) if partes else "< 1m"
    
    def limpiar_pantalla(self):
        """Limpia la pantalla (simulado con líneas en blanco)"""
        print("\n" * 3)
    
    def pausar(self, mensaje: str = "Presiona Enter para continuar..."):
        """Pausa la ejecución esperando input del usuario"""
        input(f"\n⏸️ {mensaje}")
    
    def mostrar_separador(self, caracter: str = "=", longitud: int = 50):
        """Muestra un separador visual"""
        print(caracter * longitud)
