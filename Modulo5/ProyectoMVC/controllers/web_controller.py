"""
🌐 CONTROLADOR WEB: Coordinación para interfaz web
Demuestra MVC: mismo modelo, controlador adaptado, nueva vista
"""

import webbrowser
import os
from models.tarea_repository import TareaRepository
from views.web.tarea_web_view import TareaWebView

class WebController:
    """
    Controlador Web - Coordina Modelo con Vista Web
    Reutiliza el mismo modelo, pero adapta la coordinación para web
    """
    
    def __init__(self, repository: TareaRepository):
        self.repository = repository
        self.web_view = TareaWebView()
        self.usuario_actual = "usuario1"
    
    def generar_dashboard_web(self) -> str:
        """Genera dashboard web completo"""
        # Usar el MISMO modelo que la versión consola
        estadisticas = self.repository.obtener_estadisticas_generales()
        tareas_urgentes = self.repository.obtener_tareas_urgentes()
        tareas_vencidas = self.repository.obtener_tareas_vencidas()
        tareas_proximas = self.repository.obtener_tareas_con_vencimiento_proximo(3)
        
        # Usar la NUEVA vista web
        html = self.web_view.generar_dashboard_html(
            estadisticas, tareas_urgentes, tareas_vencidas, tareas_proximas
        )
        
        return html
    
    def generar_lista_tareas_web(self, filtro: str = "todas") -> str:
        """Genera lista de tareas en formato web"""
        # Usar el MISMO modelo con diferentes filtros
        if filtro == "todas":
            tareas = self.repository.obtener_todas_tareas()
            titulo = "Todas las Tareas"
        elif filtro == "mis_tareas":
            tareas = self.repository.obtener_tareas_por_usuario(self.usuario_actual)
            titulo = f"Mis Tareas ({self.usuario_actual})"
        elif filtro == "urgentes":
            tareas = self.repository.obtener_tareas_urgentes()
            titulo = "Tareas Urgentes"
        elif filtro == "vencidas":
            tareas = self.repository.obtener_tareas_vencidas()
            titulo = "Tareas Vencidas"
        else:
            tareas = self.repository.obtener_todas_tareas()
            titulo = "Lista de Tareas"
        
        # Ordenar por prioridad (reutilizando lógica del modelo)
        tareas_ordenadas = self.repository.ordenar_por_prioridad(tareas)
        
        # Usar la NUEVA vista web
        html = self.web_view.generar_lista_tareas_html(tareas_ordenadas, titulo)
        
        return html
    
    def generar_api_json(self, endpoint: str) -> str:
        """Genera respuestas JSON para API REST"""
        if endpoint == "dashboard":
            estadisticas = self.repository.obtener_estadisticas_generales()
            return self.web_view.generar_json_api(estadisticas)
        
        elif endpoint == "tareas":
            tareas = self.repository.obtener_todas_tareas()
            return self.web_view.generar_json_api(tareas)
        
        elif endpoint == "urgentes":
            tareas = self.repository.obtener_tareas_urgentes()
            return self.web_view.generar_json_api(tareas)
        
        else:
            return self.web_view.generar_json_api({"error": "Endpoint no encontrado"})
    
    def abrir_en_navegador(self, contenido_html: str, nombre_archivo: str = "dashboard.html"):
        """Guarda HTML y lo abre en el navegador"""
        # Asegurar que existe el directorio templates
        if not os.path.exists("templates"):
            os.makedirs("templates")
        
        # Guardar archivo HTML
        ruta_completa = os.path.abspath(f"templates/{nombre_archivo}")
        
        try:
            with open(ruta_completa, 'w', encoding='utf-8') as f:
                f.write(contenido_html)
            
            # Abrir en navegador
            webbrowser.open(f"file://{ruta_completa}")
            
            return f"✅ Dashboard web abierto en navegador: {ruta_completa}"
            
        except Exception as e:
            return f"❌ Error al abrir dashboard: {e}"
    
    def demostrar_mvc_web(self):
        """Demuestra las ventajas de MVC con múltiples vistas"""
        print("🌐 DEMOSTRANDO VENTAJAS DE MVC CON VISTA WEB")
        print("="*55)
        
        print("📦 MODELO: Usando el mismo TareaRepository")
        print(f"   - {len(self.repository)} tareas cargadas")
        print(f"   - Misma lógica de negocio")
        print(f"   - Mismas consultas y cálculos")
        
        print("\n🎮 CONTROLADOR: Adaptado para web")
        print("   - Coordina mismo modelo con nueva vista")
        print("   - Genera HTML en lugar de mostrar en consola")
        print("   - Misma lógica de aplicación")
        
        print("\n👁️ VISTA: Nueva implementación web")
        print("   - HTML moderno con Bootstrap")
        print("   - Diseño responsive")
        print("   - Mismos datos, presentación diferente")
        
        # Generar dashboard web
        print(f"\n🚀 GENERANDO DASHBOARD WEB...")
        dashboard_html = self.generar_dashboard_web()
        resultado = self.abrir_en_navegador(dashboard_html, "dashboard_mvc.html")
        print(f"   {resultado}")
        
        # Generar lista de tareas
        print(f"\n📋 GENERANDO LISTA DE TAREAS WEB...")
        lista_html = self.generar_lista_tareas_web("todas")
        resultado = self.abrir_en_navegador(lista_html, "tareas_mvc.html")
        print(f"   {resultado}")
        
        # Generar API JSON
        print(f"\n🔗 GENERANDO API JSON...")
        json_data = self.generar_api_json("dashboard")
        
        with open("templates/api_dashboard.json", 'w', encoding='utf-8') as f:
            f.write(json_data)
        
        print(f"   ✅ API JSON guardada: templates/api_dashboard.json")
        
        print(f"\n🎉 VENTAJAS DE MVC DEMOSTRADAS:")
        print("   ✅ MISMO MODELO para consola y web")
        print("   ✅ CONTROLADOR adaptable a diferentes vistas")
        print("   ✅ VISTA intercambiable sin afectar lógica")
        print("   ✅ DATOS consistentes en todas las interfaces")
        print("   ✅ MANTENIMIENTO simplificado")
        
        return {
            "dashboard_html": "templates/dashboard_mvc.html",
            "tareas_html": "templates/tareas_mvc.html", 
            "api_json": "templates/api_dashboard.json"
        }
