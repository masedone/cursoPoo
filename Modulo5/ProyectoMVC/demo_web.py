#!/usr/bin/env python3
"""
🎭 DEMO AUTOMÁTICA - MVC Web
Genera automáticamente el dashboard web para mostrar las ventajas de MVC
"""

import sys
import os

# Agregar el directorio raíz al path para imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.tarea_repository import TareaRepository
from controllers.web_controller import WebController
from config.settings import Settings

def demo_automatica():
    """Demostración automática del sistema MVC web"""
    
    print("🎭 DEMO AUTOMÁTICA: VENTAJAS DE MVC CON VISTA WEB")
    print("="*60)
    
    # Configurar directorios
    Settings.ensure_data_dir()
    
    # REUTILIZAR EL MISMO MODELO que la versión consola
    repository = TareaRepository(Settings.get_data_file_path())
    
    # NUEVO CONTROLADOR adaptado para web
    web_controller = WebController(repository)
    
    print(f"✅ MODELO: Repositorio cargado con {len(repository)} tareas")
    print(f"✅ CONTROLADOR: WebController inicializado")
    print(f"✅ VISTA: TareaWebView preparada")
    
    print(f"\n🏗️ DEMOSTRANDO VENTAJAS DE MVC:")
    print("-"*40)
    
    # 1. Generar Dashboard Web
    print(f"\n1️⃣ GENERANDO DASHBOARD WEB...")
    try:
        dashboard_html = web_controller.generar_dashboard_web()
        
        # Asegurar directorio
        if not os.path.exists("templates"):
            os.makedirs("templates")
        
        # Guardar dashboard
        with open("templates/dashboard_demo.html", 'w', encoding='utf-8') as f:
            f.write(dashboard_html)
        
        ruta_dashboard = os.path.abspath("templates/dashboard_demo.html")
        print(f"   ✅ Dashboard generado: {ruta_dashboard}")
        print(f"   📊 Tamaño: {len(dashboard_html):,} caracteres")
        
        # Mostrar estadísticas
        estadisticas = repository.obtener_estadisticas_generales()
        print(f"   📈 Datos mostrados:")
        print(f"      📋 Total: {estadisticas['total_tareas']} tareas")
        print(f"      🔄 Activas: {estadisticas['tareas_activas']}")
        print(f"      ✅ Completadas: {estadisticas['tareas_completadas']}")
        print(f"      🚨 Urgentes: {estadisticas['tareas_urgentes']}")
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # 2. Generar Lista de Tareas
    print(f"\n2️⃣ GENERANDO LISTA DE TAREAS WEB...")
    try:
        lista_html = web_controller.generar_lista_tareas_web("todas")
        
        # Guardar lista
        with open("templates/tareas_demo.html", 'w', encoding='utf-8') as f:
            f.write(lista_html)
        
        ruta_lista = os.path.abspath("templates/tareas_demo.html")
        print(f"   ✅ Lista generada: {ruta_lista}")
        print(f"   📊 Tamaño: {len(lista_html):,} caracteres")
        
        # Contar tareas por estado
        tareas = repository.obtener_todas_tareas()
        estados = {}
        for tarea in tareas:
            estado = tarea.estado.value
            estados[estado] = estados.get(estado, 0) + 1
        
        print(f"   📋 Tareas por estado:")
        for estado, cantidad in estados.items():
            print(f"      📊 {estado.title()}: {cantidad}")
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # 3. Generar API JSON
    print(f"\n3️⃣ GENERANDO API JSON...")
    try:
        json_dashboard = web_controller.generar_api_json("dashboard")
        json_tareas = web_controller.generar_api_json("tareas")
        
        # Guardar JSONs
        with open("templates/api_dashboard_demo.json", 'w', encoding='utf-8') as f:
            f.write(json_dashboard)
        
        with open("templates/api_tareas_demo.json", 'w', encoding='utf-8') as f:
            f.write(json_tareas)
        
        ruta_api1 = os.path.abspath("templates/api_dashboard_demo.json")
        ruta_api2 = os.path.abspath("templates/api_tareas_demo.json")
        
        print(f"   ✅ API Dashboard: {ruta_api1}")
        print(f"   ✅ API Tareas: {ruta_api2}")
        print(f"   📊 Tamaño Dashboard JSON: {len(json_dashboard):,} caracteres")
        print(f"   📊 Tamaño Tareas JSON: {len(json_tareas):,} caracteres")
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # 4. Crear archivo de ejemplo CSS
    print(f"\n4️⃣ CREANDO RECURSOS ADICIONALES...")
    try:
        if not os.path.exists("static/css"):
            os.makedirs("static/css")
        
        css_personalizado = """
/* Estilos personalizados para el Sistema MVC */
.mvc-demo {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
}

.mvc-card {
    border-radius: 15px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.mvc-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
}

.mvc-badge {
    border-radius: 20px;
    padding: 5px 12px;
    font-weight: 600;
}

/* Animaciones para demostrar interactividad */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.animate-fade-in {
    animation: fadeInUp 0.6s ease-out;
}
        """
        
        with open("static/css/mvc-demo.css", 'w', encoding='utf-8') as f:
            f.write(css_personalizado)
        
        ruta_css = os.path.abspath("static/css/mvc-demo.css")
        print(f"   ✅ CSS personalizado: {ruta_css}")
        
    except Exception as e:
        print(f"   ❌ Error creando CSS: {e}")
    
    # 5. Resumen final
    print(f"\n🎉 DEMOSTRACIÓN COMPLETADA")
    print("="*50)
    
    print(f"\n📁 ARCHIVOS GENERADOS:")
    archivos = [
        "templates/dashboard_demo.html",
        "templates/tareas_demo.html", 
        "templates/api_dashboard_demo.json",
        "templates/api_tareas_demo.json",
        "static/css/mvc-demo.css"
    ]
    
    for archivo in archivos:
        if os.path.exists(archivo):
            tamaño = os.path.getsize(archivo)
            print(f"   📄 {archivo} ({tamaño:,} bytes)")
        else:
            print(f"   ❌ {archivo} (no generado)")
    
    print(f"\n🏗️ VENTAJAS DE MVC DEMOSTRADAS:")
    print("="*40)
    
    print(f"\n📦 MODELO (TareaRepository):")
    print("   ✅ Mismos datos para consola y web")
    print("   ✅ Una sola fuente de verdad")
    print("   ✅ Lógica de negocio reutilizada")
    print("   ✅ Consultas consistentes")
    
    print(f"\n👁️ VISTA (TareaWebView):")
    print("   ✅ HTML moderno y responsive")
    print("   ✅ Bootstrap para diseño profesional") 
    print("   ✅ Mismos datos, presentación diferente")
    print("   ✅ Múltiples formatos (HTML, JSON)")
    
    print(f"\n🎮 CONTROLADOR (WebController):")
    print("   ✅ Coordina modelo con vista web")
    print("   ✅ Adaptado sin cambiar modelo")
    print("   ✅ Genera múltiples salidas")
    print("   ✅ Mantiene separación de responsabilidades")
    
    print(f"\n🎯 BENEFICIOS OBTENIDOS:")
    print("   🔄 Código reutilizado al 100%")
    print("   🎨 Interfaz moderna sin cambiar lógica")
    print("   🔧 Mantenimiento simplificado")
    print("   📱 Base para múltiples interfaces")
    print("   🧪 Testing independiente por capas")
    
    print(f"\n📂 PARA VER LOS RESULTADOS:")
    print("   1. Abrir templates/dashboard_demo.html en navegador")
    print("   2. Abrir templates/tareas_demo.html en navegador")
    print("   3. Revisar archivos JSON para APIs")
    print("   4. Comparar con la versión de consola (main.py)")
    
    print(f"\n🚀 PRÓXIMOS PASOS POSIBLES:")
    print("   📱 Vista móvil responsive")
    print("   🌐 Servidor web con Flask/FastAPI")
    print("   📊 Dashboard en tiempo real")
    print("   🔐 Autenticación de usuarios")
    print("   📧 Notificaciones automáticas")
    
    return {
        "dashboard": "templates/dashboard_demo.html",
        "tareas": "templates/tareas_demo.html",
        "api_dashboard": "templates/api_dashboard_demo.json",
        "api_tareas": "templates/api_tareas_demo.json",
        "css": "static/css/mvc-demo.css"
    }

if __name__ == "__main__":
    try:
        archivos = demo_automatica()
        
        print(f"\n✨ ¡Demo completada exitosamente!")
        print(f"📁 {len(archivos)} archivos generados")
        
    except Exception as e:
        print(f"\n❌ Error en la demostración: {e}")
        import traceback
        traceback.print_exc()
