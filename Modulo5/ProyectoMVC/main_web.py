#!/usr/bin/env python3
"""
🌐 PROYECTO MVC WEB - Sistema de Gestión de Tareas
Demuestra la ventaja de MVC: cambiar la vista sin afectar modelo/controlador
"""

import sys
import os

# Agregar el directorio raíz al path para imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.tarea_repository import TareaRepository
from controllers.web_controller import WebController
from config.settings import Settings

class AplicacionMVCWeb:
    """
    Aplicación Web MVC - Demuestra reutilización del modelo
    """
    
    def __init__(self):
        # Configurar directorios
        Settings.ensure_data_dir()
        
        # REUTILIZAR EL MISMO MODELO que la versión consola
        self.repository = TareaRepository(Settings.get_data_file_path())
        
        # NUEVO CONTROLADOR adaptado para web
        self.web_controller = WebController(self.repository)
        
        print(f"🌐 {Settings.APP_NAME} - VERSIÓN WEB")
        print("="*60)
        print("✅ MODELO: Mismo repositorio que versión consola")
        print("✅ CONTROLADOR: Adaptado para generar HTML")
        print("✅ VISTA: Nueva implementación web moderna")
        print(f"✅ DATOS: {len(self.repository)} tareas reutilizadas")
        print()
    
    def ejecutar(self):
        """Ejecuta la demostración web"""
        try:
            self.mostrar_menu_web()
            
        except KeyboardInterrupt:
            print("\n\nAplicación web interrumpida por el usuario")
            
        except Exception as e:
            print(f"\n❌ Error crítico: {e}")
    
    def mostrar_menu_web(self):
        """Menú para generar diferentes vistas web"""
        while True:
            print(f"\n🌐 SISTEMA MVC - GENERADOR WEB")
            print("="*40)
            print("1. 🏠 Dashboard web completo")
            print("2. 📋 Lista de todas las tareas")
            print("3. 👤 Mis tareas")
            print("4. 🚨 Tareas urgentes")
            print("5. ⏰ Tareas vencidas")
            print("6. 🔗 API JSON (dashboard)")
            print("7. 🔗 API JSON (todas las tareas)")
            print("8. 🎭 Demostración completa MVC")
            print("9. 🚪 Salir")
            print("-"*40)
            
            try:
                opcion = input("Seleccione una opción (1-9): ").strip()
                
                if opcion == "1":
                    self.generar_dashboard()
                    
                elif opcion == "2":
                    self.generar_lista_tareas("todas")
                    
                elif opcion == "3":
                    self.generar_lista_tareas("mis_tareas")
                    
                elif opcion == "4":
                    self.generar_lista_tareas("urgentes")
                    
                elif opcion == "5":
                    self.generar_lista_tareas("vencidas")
                    
                elif opcion == "6":
                    self.generar_api_json("dashboard")
                    
                elif opcion == "7":
                    self.generar_api_json("tareas")
                    
                elif opcion == "8":
                    self.demostracion_completa()
                    
                elif opcion == "9":
                    print("👋 ¡Hasta luego!")
                    break
                    
                else:
                    print("❌ Opción no válida")
                
                if opcion != "9":
                    input("\nPresiona Enter para continuar...")
                    
            except Exception as e:
                print(f"❌ Error en la operación: {e}")
                input("Presiona Enter para continuar...")
    
    def generar_dashboard(self):
        """Genera y abre dashboard web"""
        print("\n🏠 GENERANDO DASHBOARD WEB...")
        print("-"*30)
        
        try:
            html = self.web_controller.generar_dashboard_web()
            resultado = self.web_controller.abrir_en_navegador(html, "dashboard_mvc.html")
            
            print(f"📊 Dashboard generado exitosamente")
            print(f"🌐 {resultado}")
            print(f"📁 Archivo: templates/dashboard_mvc.html")
            
            # Mostrar estadísticas en consola también
            estadisticas = self.repository.obtener_estadisticas_generales()
            print(f"\n📈 ESTADÍSTICAS MOSTRADAS EN WEB:")
            print(f"   📋 Total tareas: {estadisticas['total_tareas']}")
            print(f"   🔄 Activas: {estadisticas['tareas_activas']}")
            print(f"   ✅ Completadas: {estadisticas['tareas_completadas']}")
            print(f"   🚨 Urgentes: {estadisticas['tareas_urgentes']}")
            print(f"   📊 Tasa completado: {estadisticas['tasa_completado']:.1f}%")
            
        except Exception as e:
            print(f"❌ Error generando dashboard: {e}")
    
    def generar_lista_tareas(self, filtro: str):
        """Genera y abre lista de tareas web"""
        filtros_nombres = {
            "todas": "📋 TODAS LAS TAREAS",
            "mis_tareas": "👤 MIS TAREAS", 
            "urgentes": "🚨 TAREAS URGENTES",
            "vencidas": "⏰ TAREAS VENCIDAS"
        }
        
        print(f"\n{filtros_nombres.get(filtro, '📋 LISTA DE TAREAS')}...")
        print("-"*30)
        
        try:
            html = self.web_controller.generar_lista_tareas_web(filtro)
            nombre_archivo = f"tareas_{filtro}_mvc.html"
            resultado = self.web_controller.abrir_en_navegador(html, nombre_archivo)
            
            print(f"📋 Lista generada exitosamente")
            print(f"🌐 {resultado}")
            print(f"📁 Archivo: templates/{nombre_archivo}")
            
            # Mostrar resumen en consola
            if filtro == "todas":
                tareas = self.repository.obtener_todas_tareas()
            elif filtro == "mis_tareas":
                tareas = self.repository.obtener_tareas_por_usuario(self.web_controller.usuario_actual)
            elif filtro == "urgentes":
                tareas = self.repository.obtener_tareas_urgentes()
            elif filtro == "vencidas":
                tareas = self.repository.obtener_tareas_vencidas()
            
            print(f"\n📊 RESUMEN:")
            print(f"   📋 Total tareas mostradas: {len(tareas)}")
            
            if tareas:
                estados = {}
                for tarea in tareas:
                    estado = tarea.estado.value
                    estados[estado] = estados.get(estado, 0) + 1
                
                for estado, cantidad in estados.items():
                    print(f"   📊 {estado.title()}: {cantidad}")
            
        except Exception as e:
            print(f"❌ Error generando lista: {e}")
    
    def generar_api_json(self, endpoint: str):
        """Genera API JSON"""
        endpoints_nombres = {
            "dashboard": "🔗 API JSON - DASHBOARD",
            "tareas": "🔗 API JSON - TAREAS"
        }
        
        print(f"\n{endpoints_nombres.get(endpoint, '🔗 API JSON')}...")
        print("-"*30)
        
        try:
            json_data = self.web_controller.generar_api_json(endpoint)
            nombre_archivo = f"api_{endpoint}.json"
            
            # Asegurar directorio
            if not os.path.exists("templates"):
                os.makedirs("templates")
            
            # Guardar JSON
            ruta_completa = os.path.abspath(f"templates/{nombre_archivo}")
            with open(ruta_completa, 'w', encoding='utf-8') as f:
                f.write(json_data)
            
            print(f"🔗 API JSON generada exitosamente")
            print(f"📁 Archivo: {ruta_completa}")
            print(f"📊 Tamaño: {len(json_data)} caracteres")
            
            # Mostrar preview del JSON
            import json
            data = json.loads(json_data)
            
            if isinstance(data, dict):
                print(f"\n📋 PREVIEW JSON (claves principales):")
                for key in list(data.keys())[:5]:  # Primeras 5 claves
                    print(f"   🔑 {key}: {type(data[key]).__name__}")
            elif isinstance(data, list):
                print(f"\n📋 PREVIEW JSON:")
                print(f"   📊 Array con {len(data)} elementos")
                if data:
                    print(f"   🔑 Tipo de elementos: {type(data[0]).__name__}")
            
        except Exception as e:
            print(f"❌ Error generando API JSON: {e}")
    
    def demostracion_completa(self):
        """Demostración completa de las ventajas de MVC"""
        print("\n🎭 DEMOSTRACIÓN COMPLETA MVC WEB")
        print("="*50)
        
        try:
            # Usar el método del controlador web
            archivos = self.web_controller.demostrar_mvc_web()
            
            print(f"\n📁 ARCHIVOS GENERADOS:")
            for tipo, archivo in archivos.items():
                print(f"   📄 {tipo}: {archivo}")
            
            print(f"\n🏗️ ARQUITECTURA MVC DEMOSTRADA:")
            print("="*40)
            
            print(f"\n📦 MODELO (TareaRepository):")
            print("   ✅ Mismos datos para consola y web")
            print("   ✅ Misma lógica de negocio")
            print("   ✅ Mismas consultas y cálculos")
            print("   ✅ Una sola fuente de verdad")
            
            print(f"\n🎮 CONTROLADOR (WebController):")
            print("   ✅ Coordina modelo con vista web")
            print("   ✅ Adaptado para generar HTML")
            print("   ✅ Reutiliza lógica de aplicación")
            print("   ✅ Genera múltiples formatos (HTML, JSON)")
            
            print(f"\n👁️ VISTA (TareaWebView):")
            print("   ✅ HTML moderno y responsive")
            print("   ✅ Bootstrap para diseño profesional")
            print("   ✅ Mismos datos, presentación diferente")
            print("   ✅ Compatible con navegadores modernos")
            
            print(f"\n🎯 BENEFICIOS OBTENIDOS:")
            print("   🔄 Reutilización de código")
            print("   🎨 Múltiples interfaces sin duplicar lógica")
            print("   🔧 Mantenimiento simplificado")
            print("   📱 Fácil agregar más vistas (móvil, API, etc.)")
            print("   🧪 Testing independiente de cada capa")
            
            print(f"\n🚀 PRÓXIMOS PASOS POSIBLES:")
            print("   📱 Agregar vista móvil")
            print("   🌐 API REST completa")
            print("   📊 Dashboard en tiempo real")
            print("   🔐 Sistema de autenticación")
            print("   📧 Notificaciones por email")
            
        except Exception as e:
            print(f"❌ Error en demostración: {e}")

def main():
    """Función principal del sistema web"""
    try:
        print("🌐 INICIANDO SISTEMA MVC WEB")
        print("="*40)
        
        # Crear y ejecutar aplicación web MVC
        app = AplicacionMVCWeb()
        app.ejecutar()
        
    except Exception as e:
        print(f"\n❌ Error crítico del sistema web: {e}")
        print("Por favor, contacte al administrador")

if __name__ == "__main__":
    main()