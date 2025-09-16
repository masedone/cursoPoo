# 🏗️ Proyecto MVC - Sistema de Gestión de Tareas

## 📋 Descripción
Sistema completo de gestión de tareas implementado con **arquitectura MVC (Model-View-Controller)**. Demuestra la separación clara de responsabilidades en capas independientes.

## 🎯 Características de la Arquitectura MVC

### ✅ Ventajas Demostradas
- **Separación de responsabilidades**: Cada capa tiene un propósito específico
- **Mantenibilidad**: Cambios localizados sin afectar otras capas
- **Testabilidad**: Cada componente se puede probar independientemente
- **Reutilización**: Vistas y modelos intercambiables
- **Escalabilidad**: Fácil agregar nuevas funcionalidades

### 🏗️ Estructura del Proyecto
```
ProyectoMVC/
├── models/                 # 📦 MODELO - Datos y lógica de negocio
│   ├── tarea.py           # Clase Tarea con lógica de negocio
│   ├── tarea_repository.py # Repositorio para persistencia
│   └── __init__.py
├── views/                  # 👁️ VISTA - Presentación
│   ├── tarea_view.py      # Interfaz de usuario (consola)
│   └── __init__.py
├── controllers/            # 🎮 CONTROLADOR - Coordinación
│   ├── tarea_controller.py # Lógica de aplicación
│   └── __init__.py
├── config/                 # ⚙️ CONFIGURACIÓN
│   ├── settings.py        # Configuraciones centralizadas
│   └── __init__.py
├── utils/                  # 🔧 UTILIDADES
│   ├── validators.py      # Validadores reutilizables
│   └── __init__.py
├── data/                   # 💾 DATOS (se crea automáticamente)
│   └── tareas.json        # Persistencia de datos
├── main.py                # 🚀 Aplicación principal
└── README.md              # Este archivo
```

## 🚀 Funcionalidades

### 📋 Gestión de Tareas
- **CRUD completo**: Crear, leer, actualizar y eliminar tareas
- **Estados**: Pendiente, En progreso, Completada, Cancelada
- **Prioridades**: Baja, Media, Alta, Crítica
- **Fechas**: Creación, inicio, completado, vencimiento
- **Usuarios**: Asignación y cambio de responsables
- **Etiquetas**: Categorización flexible
- **Comentarios**: Historial de notas
- **Tiempo**: Estimado vs. real trabajado

### 🔍 Búsqueda y Filtros
- Búsqueda por texto (título, descripción, usuario)
- Filtros por estado, prioridad, usuario, etiqueta
- Tareas vencidas y urgentes
- Tareas que vencen pronto
- Tareas completadas por fecha

### 📊 Reportes y Estadísticas
- Dashboard con resumen ejecutivo
- Estadísticas generales del sistema
- Distribución por estado, prioridad y usuario
- Tareas que requieren atención
- Tiempo promedio de completado
- Exportación de datos (JSON)

### ⚙️ Configuración
- Cambio de usuario
- Limpieza de tareas canceladas
- Persistencia automática
- Información del sistema

## 💻 Instalación y Uso

### Requisitos
- Python 3.7+
- No requiere librerías externas (solo módulos estándar)

### Ejecución
```bash
cd ProyectoMVC
python main.py
```

## 🏗️ Arquitectura MVC en Detalle

### 📦 MODELO (Model)
**Archivos**: `models/tarea.py`, `models/tarea_repository.py`

**Responsabilidades**:
- ✅ Lógica de negocio (validaciones, cálculos, reglas)
- ✅ Gestión de datos (CRUD, consultas, persistencia)
- ✅ Estados y transiciones de tareas
- ❌ NO maneja presentación
- ❌ NO coordina flujos de aplicación

**Ejemplo de lógica de negocio**:
```python
def cambiar_estado(self, nuevo_estado: EstadoTarea) -> bool:
    # Validar transiciones permitidas
    if nuevo_estado not in transiciones_validas[self.estado]:
        return False
    # Actualizar fechas automáticamente
    if nuevo_estado == EstadoTarea.COMPLETADA:
        self.fecha_completado = datetime.datetime.now()
    return True
```

### 👁️ VISTA (View)
**Archivos**: `views/tarea_view.py`

**Responsabilidades**:
- ✅ Presentación de datos al usuario
- ✅ Interfaces de entrada y salida
- ✅ Formateo y visualización
- ✅ Mensajes y notificaciones
- ❌ NO contiene lógica de negocio
- ❌ NO accede directamente a datos

**Ejemplo de presentación**:
```python
def mostrar_tarea_detalle(self, tarea: Tarea):
    icono_estado = self.iconos_estado[tarea.estado]
    icono_prioridad = self.iconos_prioridad[tarea.prioridad]
    print(f"📊 Estado: {icono_estado} {tarea.estado.value}")
    print(f"⚡ Prioridad: {icono_prioridad} {tarea.prioridad.value}")
```

### 🎮 CONTROLADOR (Controller)
**Archivos**: `controllers/tarea_controller.py`

**Responsabilidades**:
- ✅ Coordinación entre Modelo y Vista
- ✅ Flujo de aplicación
- ✅ Validaciones de entrada
- ✅ Manejo de errores
- ❌ NO contiene lógica de negocio
- ❌ NO maneja presentación directa

**Ejemplo de coordinación**:
```python
def crear_tarea_interactiva(self) -> bool:
    # 1. Vista: Solicitar datos
    titulo = self.view.solicitar_entrada("Título")
    
    # 2. Modelo: Crear tarea
    tarea = self.repository.crear_tarea(titulo, ...)
    
    # 3. Vista: Mostrar resultado
    self.view.mostrar_tarea_detalle(tarea)
    return True
```

## 📱 Interfaz de Usuario
Sistema de menús por consola con navegación intuitiva:

```
🏗️ SISTEMA MVC - GESTIÓN DE TAREAS
========================================
1. 📋 Ver todas las tareas
2. 👤 Ver mis tareas  
3. 🔍 Buscar tareas
4. ➕ Crear nueva tarea
5. ✏️ Modificar tarea
6. 🗑️ Eliminar tarea
7. 📊 Ver estadísticas
8. 🏠 Dashboard
9. ⚙️ Configuración
10. 💾 Guardar datos
11. 🚪 Salir
```

## 🔧 Características Técnicas

### Persistencia
- **Formato JSON** para legibilidad
- **Serialización automática** de objetos complejos
- **Carga lazy** de datos
- **Backup automático** con timestamps

### Validaciones
- **Capa de validación separada** (`utils/validators.py`)
- **Validación en múltiples niveles** (entrada, negocio, persistencia)
- **Mensajes de error descriptivos**
- **Validación de tipos y rangos**

### Configuración
- **Configuración centralizada** (`config/settings.py`)
- **Separación de constantes**
- **Rutas y archivos configurables**
- **Valores por defecto**

## 📊 Datos de Ejemplo
El sistema incluye datos iniciales para demostración:
- **5 tareas** con diferentes estados y prioridades
- **6 usuarios** predefinidos
- **Etiquetas** categorizadas (backend, frontend, testing, etc.)
- **Fechas de vencimiento** variadas
- **Comentarios** de ejemplo

## 🎓 Propósito Educativo

### Lo que demuestra este proyecto MVC:

1. **Separación clara de capas**:
   - Modelo: Solo datos y lógica de negocio
   - Vista: Solo presentación
   - Controlador: Solo coordinación

2. **Bajo acoplamiento**:
   - Cambiar la vista no afecta el modelo
   - Agregar lógica de negocio no afecta la vista
   - El controlador es el único punto de contacto

3. **Alta cohesión**:
   - Cada clase tiene una responsabilidad específica
   - Funciones enfocadas en una sola tarea
   - Organización lógica por funcionalidad

4. **Extensibilidad**:
   - Fácil agregar nuevas vistas (web, móvil, API)
   - Fácil cambiar persistencia (BD real)
   - Fácil agregar nuevas funcionalidades

### Comparación con Monolito:

| Aspecto | Monolito | MVC |
|---------|----------|-----|
| **Archivos** | 1 archivo (1000+ líneas) | 10+ archivos organizados |
| **Responsabilidades** | Mezcladas en métodos | Separadas por capas |
| **Testing** | Difícil (todo acoplado) | Fácil (componentes independientes) |
| **Mantenimiento** | Complejo (cambios afectan todo) | Simple (cambios localizados) |
| **Escalabilidad** | Limitada | Alta |
| **Reutilización** | Baja | Alta |

## 🔄 Evolución y Extensiones

### Posibles mejoras:
1. **Vista Web**: Agregar `web_view.py` con Flask/Django
2. **API REST**: Agregar `api_view.py` con endpoints JSON
3. **Base de datos real**: Cambiar repositorio a SQLAlchemy
4. **Autenticación**: Agregar sistema de usuarios real
5. **Notificaciones**: Integrar email/SMS
6. **Tests**: Agregar suite de pruebas unitarias

### Patrones implementados:
- **MVC**: Separación de responsabilidades
- **Repository**: Abstracción de persistencia
- **Strategy**: Diferentes formatos de exportación
- **Factory**: Creación de objetos complejos
- **Singleton**: Configuración centralizada

---

**Este proyecto es un ejemplo educativo completo de arquitectura MVC para comparar con implementaciones monolíticas y otras arquitecturas.**

## 🚀 Próximos Pasos
1. Ejecutar el proyecto: `python main.py`
2. Explorar el código fuente por capas
3. Comparar con el proyecto monolítico
4. Experimentar agregando nuevas funcionalidades
5. Implementar tests unitarios para cada capa
