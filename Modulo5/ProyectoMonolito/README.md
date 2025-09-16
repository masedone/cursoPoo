# 🏛️ Proyecto Monolítico - Sistema de Inventario

## 📋 Descripción
Sistema completo de gestión de inventario implementado como **arquitectura monolítica**. Toda la funcionalidad está contenida en un solo archivo principal (`main.py`).

## 🎯 Características del Monolito

### ✅ Ventajas Demostradas
- **Simplicidad**: Todo el código en un solo lugar
- **Desarrollo rápido**: Funcionalidad inmediata sin configuración compleja
- **Deploy simple**: Un solo archivo ejecutable
- **Fácil comprensión**: Flujo de código lineal

### ❌ Limitaciones Evidentes
- **Archivo muy grande**: +1000 líneas en un solo archivo
- **Responsabilidades mezcladas**: UI, lógica de negocio y datos juntos
- **Difícil mantenimiento**: Cambios pequeños afectan todo el sistema
- **Testing complejo**: Todo está acoplado

## 🚀 Funcionalidades

### 📦 Gestión de Productos
- Agregar, modificar y eliminar productos
- Búsqueda por nombre, categoría o proveedor
- Gestión de precios con/sin IVA
- Control de productos activos/inactivos

### 📊 Control de Inventario
- Entrada y salida de stock
- Ajustes de inventario
- Alertas de stock bajo
- Historial de movimientos

### 📈 Reportes y Estadísticas
- Estado general del inventario
- Análisis por categorías y proveedores
- Ranking de productos por valor
- Exportación de datos (JSON)

### ⚙️ Configuración
- Gestión de usuarios
- Configuración de IVA
- Gestión de categorías y proveedores
- Persistencia de datos

## 💻 Instalación y Uso

### Requisitos
- Python 3.7+
- No requiere librerías externas (solo módulos estándar)

### Ejecución
```bash
cd ProyectoMonolito
python main.py
```

### Estructura del Proyecto
```
ProyectoMonolito/
├── main.py              # Aplicación monolítica completa
├── README.md            # Este archivo
└── inventario.json      # Datos persistentes (se crea automáticamente)
```

## 📱 Interfaz de Usuario
Sistema de menús por consola con navegación intuitiva:

```
🏛️ SISTEMA DE INVENTARIO MONOLÍTICO
Usuario: admin | Productos: 6
==================================================
1. 📦 Gestión de Productos
2. 📊 Inventario y Stock  
3. 📈 Reportes y Estadísticas
4. 🔄 Movimientos de Stock
5. ⚙️ Configuración
6. 💾 Guardar/Cargar Datos
7. 🚪 Salir
```

## 🔧 Características Técnicas

### Almacenamiento
- **Base de datos simulada** en memoria (listas y diccionarios)
- **Persistencia** mediante archivos JSON
- **Sin dependencias externas** de BD

### Validaciones
- Validación de datos en cada operación
- Control de stock negativo
- Verificación de productos activos
- Validación de usuarios y permisos

### Configuración
- IVA configurable
- Stock mínimo por defecto
- Categorías y proveedores personalizables
- Múltiples usuarios

## 📊 Datos de Ejemplo
El sistema incluye datos iniciales:
- **6 productos** de diferentes categorías
- **3 categorías**: Electrónicos, Oficina, Hogar, Deportes
- **3 proveedores**: Proveedor A, B, C
- **3 usuarios**: admin, vendedor1, vendedor2

## 🎓 Propósito Educativo

### Lo que demuestra este monolito:
1. **Simplicidad inicial**: Fácil de entender y ejecutar
2. **Desarrollo rápido**: Funcionalidad completa en poco tiempo
3. **Acoplamiento fuerte**: Todo está interconectado
4. **Escalabilidad limitada**: Difícil de extender sin afectar todo

### Cuándo usar esta arquitectura:
- ✅ Proyectos pequeños (< 10,000 líneas)
- ✅ Equipos pequeños (1-3 desarrolladores)  
- ✅ MVPs y prototipos rápidos
- ✅ Aplicaciones con lógica simple
- ✅ Tiempo de desarrollo muy limitado

### Cuándo NO usar esta arquitectura:
- ❌ Proyectos grandes con múltiples equipos
- ❌ Necesidad de múltiples interfaces (web, móvil, API)
- ❌ Requisitos de escalabilidad alta
- ❌ Mantenimiento a largo plazo
- ❌ Testing automatizado extensivo

## 🔄 Evolución Recomendada
Cuando el proyecto crezca, considerar migrar a:
1. **Arquitectura MVC** (separación por capas)
2. **Microservicios** (si escala mucho más)

## 📝 Notas de Implementación
- **Un solo archivo**: `main.py` contiene toda la aplicación
- **Clase monolítica**: `SistemaInventarioMonolitico` tiene todas las responsabilidades
- **Métodos largos**: Cada función maneja múltiples aspectos (UI, validación, lógica, datos)
- **Estado global**: Todas las variables compartidas en la misma clase

---

**Este proyecto es un ejemplo educativo de arquitectura monolítica para comparar con implementaciones MVC y otras arquitecturas.**
