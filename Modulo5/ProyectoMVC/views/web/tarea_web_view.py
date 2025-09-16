"""
🌐 VISTA WEB: Presentación HTML de Tareas
Demuestra la ventaja de MVC: cambiar la vista sin afectar modelo/controlador
"""

import datetime
import json
from typing import List, Dict, Any
from models.tarea import Tarea, EstadoTarea, PrioridadTarea

class TareaWebView:
    """
    Vista Web de Tareas - Genera HTML dinámico
    Misma funcionalidad que TareaView pero con interfaz web
    """
    
    def __init__(self):
        # Configuración de iconos y colores para web
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
            EstadoTarea.PENDIENTE: "#6c757d",
            EstadoTarea.EN_PROGRESO: "#007bff",
            EstadoTarea.COMPLETADA: "#28a745",
            EstadoTarea.CANCELADA: "#dc3545"
        }
        
        self.colores_prioridad = {
            PrioridadTarea.BAJA: "#28a745",
            PrioridadTarea.MEDIA: "#ffc107",
            PrioridadTarea.ALTA: "#fd7e14",
            PrioridadTarea.CRITICA: "#dc3545"
        }
    
    def generar_dashboard_html(self, estadisticas: Dict[str, Any], 
                              tareas_urgentes: List[Tarea],
                              tareas_vencidas: List[Tarea], 
                              tareas_proximas: List[Tarea]) -> str:
        """Genera dashboard completo en HTML"""
        
        html = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>🏗️ Sistema MVC - Dashboard de Tareas</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
            <style>
                body {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }}
                .dashboard-container {{
                    padding: 20px;
                }}
                .card {{
                    border: none;
                    border-radius: 15px;
                    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
                    transition: transform 0.3s ease, box-shadow 0.3s ease;
                }}
                .card:hover {{
                    transform: translateY(-5px);
                    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
                }}
                .stat-card {{
                    text-align: center;
                    padding: 20px;
                    margin-bottom: 20px;
                }}
                .stat-number {{
                    font-size: 2.5rem;
                    font-weight: bold;
                    margin-bottom: 10px;
                }}
                .stat-label {{
                    font-size: 0.9rem;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                    opacity: 0.8;
                }}
                .priority-badge {{
                    padding: 5px 10px;
                    border-radius: 20px;
                    font-size: 0.8rem;
                    font-weight: bold;
                }}
                .status-badge {{
                    padding: 5px 10px;
                    border-radius: 20px;
                    font-size: 0.8rem;
                    font-weight: bold;
                }}
                .task-card {{
                    margin-bottom: 15px;
                    border-left: 4px solid;
                }}
                .task-title {{
                    font-weight: 600;
                    margin-bottom: 8px;
                }}
                .task-meta {{
                    font-size: 0.85rem;
                    color: #6c757d;
                }}
                .chart-container {{
                    height: 300px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }}
                .progress-ring {{
                    width: 120px;
                    height: 120px;
                    position: relative;
                }}
                .navbar {{
                    background: rgba(255,255,255,0.95) !important;
                    backdrop-filter: blur(10px);
                }}
                .btn-primary {{
                    background: linear-gradient(45deg, #667eea, #764ba2);
                    border: none;
                    border-radius: 25px;
                    padding: 10px 25px;
                }}
                .btn-primary:hover {{
                    background: linear-gradient(45deg, #764ba2, #667eea);
                }}
            </style>
        </head>
        <body>
            <!-- Navbar -->
            <nav class="navbar navbar-expand-lg navbar-light fixed-top">
                <div class="container">
                    <a class="navbar-brand fw-bold" href="#">
                        <i class="fas fa-tasks me-2"></i>
                        Sistema MVC - Gestión de Tareas
                    </a>
                    <div class="navbar-nav ms-auto">
                        <span class="navbar-text">
                            <i class="fas fa-user me-1"></i>
                            Usuario: <strong>usuario1</strong>
                        </span>
                    </div>
                </div>
            </nav>
            
            <div class="dashboard-container" style="margin-top: 80px;">
                <div class="container">
                    <!-- Header -->
                    <div class="row mb-4">
                        <div class="col-12">
                            <h1 class="text-white mb-3">
                                <i class="fas fa-chart-line me-2"></i>
                                Dashboard de Tareas
                            </h1>
                            <p class="text-white-50">Resumen ejecutivo de todas las tareas del sistema</p>
                        </div>
                    </div>
                    
                    <!-- Estadísticas principales -->
                    <div class="row mb-4">
                        <div class="col-md-3">
                            <div class="card stat-card bg-primary text-white">
                                <div class="stat-number">{estadisticas['total_tareas']}</div>
                                <div class="stat-label">
                                    <i class="fas fa-list me-1"></i>
                                    Total Tareas
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="card stat-card bg-info text-white">
                                <div class="stat-number">{estadisticas['tareas_activas']}</div>
                                <div class="stat-label">
                                    <i class="fas fa-play me-1"></i>
                                    Activas
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="card stat-card bg-success text-white">
                                <div class="stat-number">{estadisticas['tareas_completadas']}</div>
                                <div class="stat-label">
                                    <i class="fas fa-check me-1"></i>
                                    Completadas
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="card stat-card bg-warning text-white">
                                <div class="stat-number">{estadisticas['tareas_urgentes']}</div>
                                <div class="stat-label">
                                    <i class="fas fa-exclamation me-1"></i>
                                    Urgentes
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Tasa de completado -->
                    <div class="row mb-4">
                        <div class="col-md-6">
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title">
                                        <i class="fas fa-percentage me-2"></i>
                                        Tasa de Completado
                                    </h5>
                                    <div class="progress" style="height: 25px;">
                                        <div class="progress-bar bg-success progress-bar-striped progress-bar-animated" 
                                             style="width: {estadisticas['tasa_completado']:.1f}%">
                                            {estadisticas['tasa_completado']:.1f}%
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title">
                                        <i class="fas fa-chart-pie me-2"></i>
                                        Distribución por Estado
                                    </h5>
                                    <div class="row">
        """
        
        # Agregar distribución por estado
        for estado, cantidad in estadisticas['por_estado'].items():
            porcentaje = (cantidad / estadisticas['total_tareas'] * 100) if estadisticas['total_tareas'] > 0 else 0
            color = self.colores_estado.get(EstadoTarea(estado), "#6c757d")
            icono = self.iconos_estado.get(EstadoTarea(estado), "📋")
            
            html += f"""
                                        <div class="col-6 mb-2">
                                            <small class="text-muted">{icono} {estado.title()}</small>
                                            <div class="progress" style="height: 8px;">
                                                <div class="progress-bar" 
                                                     style="width: {porcentaje:.1f}%; background-color: {color}">
                                                </div>
                                            </div>
                                            <small>{cantidad} ({porcentaje:.1f}%)</small>
                                        </div>
            """
        
        html += """
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Tareas que requieren atención -->
        """
        
        if tareas_urgentes or tareas_vencidas or tareas_proximas:
            html += """
                    <div class="row mb-4">
                        <div class="col-12">
                            <h3 class="text-white mb-3">
                                <i class="fas fa-bell me-2"></i>
                                Tareas que Requieren Atención
                            </h3>
                        </div>
                    </div>
                    <div class="row mb-4">
            """
            
            # Tareas urgentes
            if tareas_urgentes:
                html += f"""
                        <div class="col-md-4">
                            <div class="card">
                                <div class="card-header bg-danger text-white">
                                    <h6 class="mb-0">
                                        <i class="fas fa-fire me-2"></i>
                                        Urgentes ({len(tareas_urgentes)})
                                    </h6>
                                </div>
                                <div class="card-body p-2">
                """
                
                for tarea in tareas_urgentes[:5]:  # Mostrar máximo 5
                    html += self._generar_tarea_compacta_html(tarea)
                
                html += """
                                </div>
                            </div>
                        </div>
                """
            
            # Tareas vencidas
            if tareas_vencidas:
                html += f"""
                        <div class="col-md-4">
                            <div class="card">
                                <div class="card-header bg-warning text-dark">
                                    <h6 class="mb-0">
                                        <i class="fas fa-clock me-2"></i>
                                        Vencidas ({len(tareas_vencidas)})
                                    </h6>
                                </div>
                                <div class="card-body p-2">
                """
                
                for tarea in tareas_vencidas[:5]:  # Mostrar máximo 5
                    html += self._generar_tarea_compacta_html(tarea)
                
                html += """
                                </div>
                            </div>
                        </div>
                """
            
            # Tareas próximas
            if tareas_proximas:
                html += f"""
                        <div class="col-md-4">
                            <div class="card">
                                <div class="card-header bg-info text-white">
                                    <h6 class="mb-0">
                                        <i class="fas fa-calendar me-2"></i>
                                        Vencen Pronto ({len(tareas_proximas)})
                                    </h6>
                                </div>
                                <div class="card-body p-2">
                """
                
                for tarea in tareas_proximas[:5]:  # Mostrar máximo 5
                    html += self._generar_tarea_compacta_html(tarea)
                
                html += """
                                </div>
                            </div>
                        </div>
                """
            
            html += """
                    </div>
            """
        else:
            html += """
                    <div class="row mb-4">
                        <div class="col-12">
                            <div class="card bg-success text-white">
                                <div class="card-body text-center">
                                    <i class="fas fa-check-circle fa-3x mb-3"></i>
                                    <h4>¡Todo bajo control!</h4>
                                    <p class="mb-0">No hay tareas urgentes que requieran atención inmediata.</p>
                                </div>
                            </div>
                        </div>
                    </div>
            """
        
        # Distribución por usuario
        if estadisticas['por_usuario']:
            html += """
                    <div class="row mb-4">
                        <div class="col-12">
                            <div class="card">
                                <div class="card-header">
                                    <h5 class="mb-0">
                                        <i class="fas fa-users me-2"></i>
                                        Distribución por Usuario
                                    </h5>
                                </div>
                                <div class="card-body">
                                    <div class="row">
            """
            
            for usuario, cantidad in sorted(estadisticas['por_usuario'].items(), 
                                          key=lambda x: x[1], reverse=True):
                porcentaje = (cantidad / estadisticas['total_tareas'] * 100) if estadisticas['total_tareas'] > 0 else 0
                
                html += f"""
                                        <div class="col-md-6 mb-3">
                                            <div class="d-flex justify-content-between align-items-center">
                                                <span>
                                                    <i class="fas fa-user me-2"></i>
                                                    {usuario}
                                                </span>
                                                <span class="badge bg-primary">{cantidad}</span>
                                            </div>
                                            <div class="progress mt-1" style="height: 8px;">
                                                <div class="progress-bar" style="width: {porcentaje:.1f}%"></div>
                                            </div>
                                            <small class="text-muted">{porcentaje:.1f}% del total</small>
                                        </div>
                """
            
            html += """
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
            """
        
        # Botones de acción
        html += """
                    <div class="row mb-4">
                        <div class="col-12 text-center">
                            <a href="#" class="btn btn-primary btn-lg me-3" onclick="mostrarTodasTareas()">
                                <i class="fas fa-list me-2"></i>
                                Ver Todas las Tareas
                            </a>
                            <a href="#" class="btn btn-outline-light btn-lg me-3" onclick="crearTarea()">
                                <i class="fas fa-plus me-2"></i>
                                Nueva Tarea
                            </a>
                            <a href="#" class="btn btn-outline-light btn-lg" onclick="mostrarEstadisticas()">
                                <i class="fas fa-chart-bar me-2"></i>
                                Estadísticas Detalladas
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Scripts -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
            <script>
                function mostrarTodasTareas() {
                    alert('🏗️ Funcionalidad MVC: Esta acción sería manejada por el Controlador');
                }
                
                function crearTarea() {
                    alert('🎮 MVC en acción: El Controlador coordinaría Modelo y Vista para crear una tarea');
                }
                
                function mostrarEstadisticas() {
                    alert('📊 Arquitectura MVC: El Modelo calcularía estadísticas, la Vista las mostraría');
                }
                
                // Animación de entrada
                document.addEventListener('DOMContentLoaded', function() {
                    const cards = document.querySelectorAll('.card');
                    cards.forEach((card, index) => {
                        card.style.opacity = '0';
                        card.style.transform = 'translateY(20px)';
                        setTimeout(() => {
                            card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                            card.style.opacity = '1';
                            card.style.transform = 'translateY(0)';
                        }, index * 100);
                    });
                });
            </script>
        </body>
        </html>
        """
        
        return html
    
    def generar_lista_tareas_html(self, tareas: List[Tarea], titulo: str = "Lista de Tareas") -> str:
        """Genera lista de tareas en HTML con diseño moderno"""
        
        html = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>📋 {titulo} - Sistema MVC</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
            <style>
                body {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                }}
                .task-card {{
                    border: none;
                    border-radius: 15px;
                    margin-bottom: 15px;
                    transition: all 0.3s ease;
                    border-left: 5px solid;
                }}
                .task-card:hover {{
                    transform: translateY(-3px);
                    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
                }}
                .priority-badge, .status-badge {{
                    border-radius: 20px;
                    padding: 5px 12px;
                    font-size: 0.8rem;
                    font-weight: 600;
                }}
                .task-actions {{
                    opacity: 0;
                    transition: opacity 0.3s ease;
                }}
                .task-card:hover .task-actions {{
                    opacity: 1;
                }}
            </style>
        </head>
        <body>
            <div class="container py-5">
                <div class="row">
                    <div class="col-12">
                        <div class="d-flex justify-content-between align-items-center mb-4">
                            <h1 class="text-white">
                                <i class="fas fa-tasks me-2"></i>
                                {titulo}
                            </h1>
                            <span class="badge bg-light text-dark fs-6">
                                {len(tareas)} tareas
                            </span>
                        </div>
                    </div>
                </div>
        """
        
        if not tareas:
            html += """
                <div class="row">
                    <div class="col-12">
                        <div class="card text-center">
                            <div class="card-body py-5">
                                <i class="fas fa-inbox fa-3x text-muted mb-3"></i>
                                <h4 class="text-muted">No hay tareas para mostrar</h4>
                                <p class="text-muted">¡Perfecto momento para crear una nueva tarea!</p>
                                <button class="btn btn-primary">
                                    <i class="fas fa-plus me-2"></i>
                                    Crear Nueva Tarea
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            """
        else:
            html += '<div class="row">'
            
            for tarea in tareas:
                html += f'<div class="col-md-6 col-lg-4">'
                html += self._generar_tarea_card_html(tarea)
                html += '</div>'
            
            html += '</div>'
        
        html += """
            </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
        """
        
        return html
    
    def _generar_tarea_card_html(self, tarea: Tarea) -> str:
        """Genera una tarjeta HTML para una tarea"""
        
        # Colores y estilos
        color_estado = self.colores_estado[tarea.estado]
        color_prioridad = self.colores_prioridad[tarea.prioridad]
        icono_estado = self.iconos_estado[tarea.estado]
        icono_prioridad = self.iconos_prioridad[tarea.prioridad]
        
        # Fecha de vencimiento
        fecha_venc_html = ""
        if tarea.fecha_vencimiento:
            dias_restantes = tarea.dias_para_vencimiento()
            if dias_restantes is not None:
                if dias_restantes < 0:
                    fecha_venc_html = f'<span class="text-danger"><i class="fas fa-exclamation-triangle me-1"></i>Vencida hace {abs(dias_restantes)} días</span>'
                elif dias_restantes == 0:
                    fecha_venc_html = f'<span class="text-warning"><i class="fas fa-clock me-1"></i>Vence hoy</span>'
                elif dias_restantes <= 3:
                    fecha_venc_html = f'<span class="text-warning"><i class="fas fa-calendar me-1"></i>Vence en {dias_restantes} días</span>'
                else:
                    fecha_venc_html = f'<span class="text-success"><i class="fas fa-calendar me-1"></i>Vence en {dias_restantes} días</span>'
        
        # Etiquetas
        etiquetas_html = ""
        if tarea.etiquetas:
            etiquetas_html = "".join([
                f'<span class="badge bg-secondary me-1">#{etiqueta}</span>'
                for etiqueta in tarea.etiquetas[:3]  # Máximo 3 etiquetas
            ])
        
        return f"""
        <div class="card task-card" style="border-left-color: {color_estado};">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-start mb-2">
                    <h6 class="card-title mb-0">{tarea.titulo}</h6>
                    <div class="task-actions">
                        <button class="btn btn-sm btn-outline-primary me-1" title="Editar">
                            <i class="fas fa-edit"></i>
                        </button>
                        <button class="btn btn-sm btn-outline-danger" title="Eliminar">
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                </div>
                
                <p class="card-text text-muted small mb-3">
                    {tarea.descripcion[:100]}{'...' if len(tarea.descripcion) > 100 else ''}
                </p>
                
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="status-badge text-white" style="background-color: {color_estado};">
                        {icono_estado} {tarea.estado.value.title()}
                    </span>
                    <span class="priority-badge text-white" style="background-color: {color_prioridad};">
                        {icono_prioridad} {tarea.prioridad.value.title()}
                    </span>
                </div>
                
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <small class="text-muted">
                        <i class="fas fa-user me-1"></i>
                        {tarea.usuario_asignado}
                    </small>
                    <small class="text-muted">
                        ID: {tarea.id}
                    </small>
                </div>
                
                {f'<div class="mb-2">{fecha_venc_html}</div>' if fecha_venc_html else ''}
                
                {f'<div class="mb-2">{etiquetas_html}</div>' if etiquetas_html else ''}
                
                {f'<div><small class="text-muted"><i class="fas fa-comments me-1"></i>{len(tarea.comentarios)} comentarios</small></div>' if tarea.comentarios else ''}
            </div>
        </div>
        """
    
    def _generar_tarea_compacta_html(self, tarea: Tarea) -> str:
        """Genera una vista compacta de tarea para listas pequeñas"""
        
        icono_estado = self.iconos_estado[tarea.estado]
        icono_prioridad = self.iconos_prioridad[tarea.prioridad]
        
        alerta = ""
        if tarea.necesita_atencion():
            alerta = ' <i class="fas fa-exclamation-triangle text-danger"></i>'
        elif tarea.esta_vencida():
            alerta = ' <i class="fas fa-clock text-warning"></i>'
        
        return f"""
        <div class="d-flex justify-content-between align-items-center py-2 border-bottom">
            <div>
                <span class="me-2">{icono_estado}</span>
                <span class="me-2">{icono_prioridad}</span>
                <strong>{tarea.id}.</strong>
                <span class="ms-1">{tarea.titulo[:30]}{'...' if len(tarea.titulo) > 30 else ''}</span>
                {alerta}
            </div>
            <small class="text-muted">{tarea.usuario_asignado}</small>
        </div>
        """
    
    def guardar_html(self, contenido_html: str, nombre_archivo: str) -> str:
        """Guarda el HTML en un archivo"""
        ruta_archivo = f"templates/{nombre_archivo}"
        
        try:
            with open(ruta_archivo, 'w', encoding='utf-8') as f:
                f.write(contenido_html)
            return ruta_archivo
        except Exception as e:
            return f"Error al guardar: {e}"
    
    def generar_json_api(self, datos: Any) -> str:
        """Genera respuesta JSON para API REST"""
        if hasattr(datos, 'to_dict'):
            datos_dict = datos.to_dict()
        elif isinstance(datos, list):
            datos_dict = [item.to_dict() if hasattr(item, 'to_dict') else item for item in datos]
        else:
            datos_dict = datos
        
        return json.dumps(datos_dict, indent=2, ensure_ascii=False, default=str)
