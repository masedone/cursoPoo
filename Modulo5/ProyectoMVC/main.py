#!/usr/bin/env python3
"""
🏗️ PROYECTO MVC - Sistema de Gestión de Tareas
Aplicación principal que demuestra arquitectura MVC
"""

import sys
import os

# Agregar el directorio raíz al path para imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.tarea_repository import TareaRepository
from views.tarea_view import TareaView
from controllers.tarea_controller import TareaController
from config.settings import Settings

class AplicacionMVC:
    """
    Aplicación principal que coordina todos los componentes MVC
    """
    
    def __init__(self):
        # Configurar directorios
        Settings.ensure_data_dir()
        
        # Inicializar componentes MVC
        self.repository = TareaRepository(Settings.get_data_file_path())
        self.view = TareaView()
        self.controller = TareaController(self.repository, self.view)
        
        print(f"🏗️ {Settings.APP_NAME} v{Settings.APP_VERSION}")
        print("="*60)
        print("✅ Modelo: Repositorio de tareas inicializado")
        print("✅ Vista: Interfaz de consola configurada")
        print("✅ Controlador: Lógica de aplicación lista")
        print(f"✅ Datos: {len(self.repository)} tareas cargadas")
        print()
    
    def ejecutar(self):
        """Ejecuta la aplicación principal"""
        try:
            self.mostrar_bienvenida()
            self.menu_principal()
            
        except KeyboardInterrupt:
            self.view.mostrar_mensaje_info("\n\nAplicación interrumpida por el usuario")
            
        except Exception as e:
            self.view.mostrar_mensaje_error(f"Error crítico: {e}")
            
        finally:
            self.finalizar()
    
    def mostrar_bienvenida(self):
        """Muestra mensaje de bienvenida y información inicial"""
        self.view.mostrar_mensaje_info(f"Bienvenido al {Settings.APP_NAME}")
        self.view.mostrar_mensaje_info(f"Usuario actual: {self.controller.obtener_usuario_actual()}")
        
        # Mostrar dashboard inicial
        self.controller.mostrar_dashboard()
    
    def menu_principal(self):
        """Menú principal de la aplicación"""
        while True:
            self.view.mostrar_menu_principal()
            
            try:
                opcion = self.view.solicitar_numero("Seleccione una opción", 1, 11)
                
                if opcion == 1:
                    self.controller.listar_todas_tareas()
                    
                elif opcion == 2:
                    self.controller.listar_mis_tareas()
                    
                elif opcion == 3:
                    self.menu_busqueda_filtros()
                    
                elif opcion == 4:
                    self.controller.crear_tarea_interactiva()
                    
                elif opcion == 5:
                    self.controller.modificar_tarea_interactiva()
                    
                elif opcion == 6:
                    self.controller.eliminar_tarea_interactiva()
                    
                elif opcion == 7:
                    self.menu_estadisticas()
                    
                elif opcion == 8:
                    self.controller.mostrar_dashboard()
                    
                elif opcion == 9:
                    self.menu_configuracion()
                    
                elif opcion == 10:
                    self.controller.guardar_datos()
                    
                elif opcion == 11:
                    if self.view.confirmar_accion("¿Está seguro de que desea salir?"):
                        break
                
                # Pausa después de cada operación
                if opcion != 11:
                    self.view.pausar()
                    
            except Exception as e:
                self.view.mostrar_mensaje_error(f"Error en la operación: {e}")
                self.view.pausar()
    
    def menu_busqueda_filtros(self):
        """Submenú de búsqueda y filtros"""
        while True:
            print(f"\n🔍 BÚSQUEDA Y FILTROS")
            print("="*30)
            print("1. Buscar tareas")
            print("2. Filtrar tareas")
            print("3. Ver tarea específica")
            print("4. Tareas por estado")
            print("5. Tareas por usuario")
            print("6. Volver al menú principal")
            
            try:
                opcion = self.view.solicitar_numero("Seleccione opción", 1, 6)
                
                if opcion == 1:
                    self.controller.buscar_tareas_interactivo()
                    
                elif opcion == 2:
                    self.controller.filtrar_tareas_interactivo()
                    
                elif opcion == 3:
                    self.controller.ver_tarea_por_id()
                    
                elif opcion == 4:
                    self.controller.mostrar_tareas_por_estado()
                    
                elif opcion == 5:
                    self.controller.mostrar_tareas_por_usuario()
                    
                elif opcion == 6:
                    break
                
                if opcion != 6:
                    self.view.pausar()
                    
            except Exception as e:
                self.view.mostrar_mensaje_error(f"Error en búsqueda/filtros: {e}")
                self.view.pausar()
    
    def menu_estadisticas(self):
        """Submenú de estadísticas y reportes"""
        while True:
            print(f"\n📊 ESTADÍSTICAS Y REPORTES")
            print("="*35)
            print("1. Estadísticas generales")
            print("2. Dashboard completo")
            print("3. Tareas por estado")
            print("4. Tareas por usuario")
            print("5. Exportar datos")
            print("6. Volver al menú principal")
            
            try:
                opcion = self.view.solicitar_numero("Seleccione opción", 1, 6)
                
                if opcion == 1:
                    self.controller.mostrar_estadisticas()
                    
                elif opcion == 2:
                    self.controller.mostrar_dashboard()
                    
                elif opcion == 3:
                    self.controller.mostrar_tareas_por_estado()
                    
                elif opcion == 4:
                    self.controller.mostrar_tareas_por_usuario()
                    
                elif opcion == 5:
                    self.exportar_datos()
                    
                elif opcion == 6:
                    break
                
                if opcion != 6:
                    self.view.pausar()
                    
            except Exception as e:
                self.view.mostrar_mensaje_error(f"Error en estadísticas: {e}")
                self.view.pausar()
    
    def menu_configuracion(self):
        """Submenú de configuración"""
        while True:
            print(f"\n⚙️ CONFIGURACIÓN")
            print("="*20)
            print(f"Usuario actual: {self.controller.obtener_usuario_actual()}")
            print(f"Total tareas: {len(self.repository)}")
            print()
            print("1. Cambiar usuario")
            print("2. Información del sistema")
            print("3. Limpiar tareas canceladas")
            print("4. Guardar datos")
            print("5. Recargar datos")
            print("6. Volver al menú principal")
            
            try:
                opcion = self.view.solicitar_numero("Seleccione opción", 1, 6)
                
                if opcion == 1:
                    self.cambiar_usuario()
                    
                elif opcion == 2:
                    self.mostrar_info_sistema()
                    
                elif opcion == 3:
                    self.controller.limpiar_tareas_canceladas()
                    
                elif opcion == 4:
                    self.controller.guardar_datos()
                    
                elif opcion == 5:
                    self.recargar_datos()
                    
                elif opcion == 6:
                    break
                
                if opcion != 6:
                    self.view.pausar()
                    
            except Exception as e:
                self.view.mostrar_mensaje_error(f"Error en configuración: {e}")
                self.view.pausar()
    
    def cambiar_usuario(self):
        """Cambia el usuario actual"""
        print(f"\n👤 CAMBIO DE USUARIO")
        print("="*25)
        print(f"Usuario actual: {self.controller.obtener_usuario_actual()}")
        print(f"Usuarios disponibles: {', '.join(Settings.AVAILABLE_USERS)}")
        
        nuevo_usuario = self.view.solicitar_entrada("Nuevo usuario")
        self.controller.cambiar_usuario(nuevo_usuario)
    
    def mostrar_info_sistema(self):
        """Muestra información del sistema"""
        estadisticas = self.repository.obtener_estadisticas_generales()
        
        print(f"\n🖥️ INFORMACIÓN DEL SISTEMA")
        print("="*35)
        print(f"Aplicación: {Settings.APP_NAME}")
        print(f"Versión: {Settings.APP_VERSION}")
        print(f"Descripción: {Settings.APP_DESCRIPTION}")
        print()
        print(f"📁 Directorio de datos: {Settings.DATA_DIR}")
        print(f"📄 Archivo de datos: {Settings.DEFAULT_DATA_FILE}")
        print()
        print(f"👤 Usuario actual: {self.controller.obtener_usuario_actual()}")
        print(f"👥 Usuarios disponibles: {len(Settings.AVAILABLE_USERS)}")
        print()
        print(f"📋 Total de tareas: {estadisticas['total_tareas']}")
        print(f"🔄 Tareas activas: {estadisticas['tareas_activas']}")
        print(f"✅ Tareas completadas: {estadisticas['tareas_completadas']}")
        print(f"❌ Tareas canceladas: {estadisticas['por_estado'].get('cancelada', 0)}")
        print()
        print("🏗️ ARQUITECTURA MVC:")
        print("   📦 Modelo: TareaRepository + Tarea")
        print("   👁️ Vista: TareaView")
        print("   🎮 Controlador: TareaController")
        print("   ⚙️ Configuración: Settings")
        print("   🔧 Utilidades: Validators")
    
    def exportar_datos(self):
        """Exporta datos del sistema"""
        try:
            print(f"\n💾 EXPORTAR DATOS")
            print("="*20)
            print("1. Exportar como JSON")
            print("2. Cancelar")
            
            opcion = self.view.solicitar_numero("Seleccione formato", 1, 2)
            
            if opcion == 1:
                datos_json = self.repository.exportar_datos("json")
                
                # Generar nombre de archivo con timestamp
                import datetime
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                nombre_archivo = f"tareas_export_{timestamp}.json"
                archivo_path = Settings.get_data_file_path(nombre_archivo)
                
                with open(archivo_path, 'w', encoding='utf-8') as f:
                    f.write(datos_json)
                
                self.view.mostrar_mensaje_exito(f"Datos exportados a: {archivo_path}")
            
        except Exception as e:
            self.view.mostrar_mensaje_error(f"Error al exportar datos: {e}")
    
    def recargar_datos(self):
        """Recarga los datos desde archivo"""
        if self.view.confirmar_accion("¿Desea recargar los datos? Se perderán los cambios no guardados"):
            try:
                if self.repository.cargar_datos():
                    self.view.mostrar_mensaje_exito("Datos recargados exitosamente")
                else:
                    self.view.mostrar_mensaje_error("Error al recargar datos")
            except Exception as e:
                self.view.mostrar_mensaje_error(f"Error al recargar: {e}")
    
    def finalizar(self):
        """Finaliza la aplicación"""
        print(f"\n👋 FINALIZANDO {Settings.APP_NAME}")
        print("="*50)
        
        # Preguntar si desea guardar antes de salir
        if self.view.confirmar_accion("¿Desea guardar los datos antes de salir?"):
            if self.controller.guardar_datos():
                self.view.mostrar_mensaje_exito("Datos guardados exitosamente")
            else:
                self.view.mostrar_mensaje_error("Error al guardar datos")
        
        # Mostrar estadísticas finales
        estadisticas = self.repository.obtener_estadisticas_generales()
        print(f"\n📊 ESTADÍSTICAS DE LA SESIÓN:")
        print(f"   Total de tareas procesadas: {estadisticas['total_tareas']}")
        print(f"   Usuario: {self.controller.obtener_usuario_actual()}")
        
        print(f"\n🏗️ DEMOSTRACIÓN MVC COMPLETADA:")
        print("✅ Modelo: Gestión de datos y lógica de negocio")
        print("✅ Vista: Presentación e interfaz de usuario")
        print("✅ Controlador: Coordinación entre componentes")
        print("✅ Separación clara de responsabilidades")
        
        print(f"\n¡Gracias por usar {Settings.APP_NAME}!")

def main():
    """Función principal del sistema"""
    try:
        # Crear y ejecutar aplicación MVC
        app = AplicacionMVC()
        app.ejecutar()
        
    except Exception as e:
        print(f"\n❌ Error crítico del sistema: {e}")
        print("Por favor, contacte al administrador")

if __name__ == "__main__":
    main()
