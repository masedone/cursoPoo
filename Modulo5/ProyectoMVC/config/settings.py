"""
⚙️ CONFIGURACIÓN: Configuración del sistema
Centraliza todas las configuraciones
"""

import os

class Settings:
    """Configuración centralizada del sistema"""
    
    # Información del sistema
    APP_NAME = "Sistema MVC de Gestión de Tareas"
    APP_VERSION = "1.0.0"
    APP_DESCRIPTION = "Sistema de gestión de tareas implementado con arquitectura MVC"
    
    # Configuración de archivos
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    DEFAULT_DATA_FILE = os.path.join(DATA_DIR, "tareas.json")
    
    # Configuración de usuario
    DEFAULT_USER = "usuario1"
    AVAILABLE_USERS = ["usuario1", "admin", "dev1", "dev2", "designer1", "qa1"]
    
    # Configuración de tareas
    DEFAULT_PRIORITY = "media"
    MAX_TITLE_LENGTH = 100
    MAX_DESCRIPTION_LENGTH = 500
    DEFAULT_UPCOMING_DAYS = 3  # Días para considerar tareas próximas a vencer
    
    # Configuración de interfaz
    ITEMS_PER_PAGE = 10
    DATE_FORMAT = "%d/%m/%Y"
    DATETIME_FORMAT = "%d/%m/%Y %H:%M"
    
    # Configuración de colores/iconos (para futuras mejoras)
    COLORS = {
        "success": "green",
        "error": "red",
        "warning": "yellow",
        "info": "blue"
    }
    
    ICONS = {
        "pendiente": "⏳",
        "en_progreso": "🔄",
        "completada": "✅",
        "cancelada": "❌",
        "baja": "🟢",
        "media": "🟡",
        "alta": "🔴",
        "critica": "🚨"
    }
    
    @classmethod
    def ensure_data_dir(cls):
        """Asegura que el directorio de datos existe"""
        if not os.path.exists(cls.DATA_DIR):
            os.makedirs(cls.DATA_DIR)
    
    @classmethod
    def get_data_file_path(cls, filename: str = None) -> str:
        """Obtiene la ruta completa de un archivo de datos"""
        cls.ensure_data_dir()
        if filename is None:
            filename = "tareas.json"
        return os.path.join(cls.DATA_DIR, filename)
