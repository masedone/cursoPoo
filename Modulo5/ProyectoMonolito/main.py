#!/usr/bin/env python3
"""
🏛️ PROYECTO MONOLÍTICO - Sistema de Inventario
Toda la aplicación está contenida en un solo archivo principal
"""

import json
import datetime
from typing import List, Dict, Optional

class SistemaInventarioMonolitico:
    """
    MONOLITO: Una sola clase contiene toda la funcionalidad del sistema
    - Base de datos (simulada)
    - Lógica de negocio
    - Validaciones
    - Interfaz de usuario
    - Reportes
    - Configuración
    """
    
    def __init__(self):
        # Configuración del sistema
        self.version = "1.0.0"
        self.nombre_empresa = "TechStore S.L."
        self.archivo_datos = "inventario.json"
        
        # Base de datos simulada en memoria
        self.productos = []
        self.categorias = ["Electrónicos", "Oficina", "Hogar", "Deportes"]
        self.proveedores = ["Proveedor A", "Proveedor B", "Proveedor C"]
        self.historial_movimientos = []
        self.usuarios = ["admin", "vendedor1", "vendedor2"]
        self.usuario_actual = "admin"
        
        # Contadores
        self.siguiente_id_producto = 1
        self.siguiente_id_movimiento = 1
        
        # Configuración de negocio
        self.stock_minimo_default = 5
        self.iva_porcentaje = 21.0
        
        print(f"🏛️ {self.nombre_empresa} - Sistema de Inventario v{self.version}")
        print("="*60)
        
        # Cargar datos iniciales
        self._inicializar_datos()
    
    def _inicializar_datos(self):
        """Inicializa datos de prueba del sistema"""
        productos_iniciales = [
            ("Laptop HP Pavilion", "Electrónicos", 899.99, 10, "Proveedor A"),
            ("Mouse Inalámbrico", "Electrónicos", 25.99, 50, "Proveedor B"),
            ("Silla Ergonómica", "Oficina", 199.99, 8, "Proveedor A"),
            ("Escritorio Blanco", "Oficina", 149.99, 5, "Proveedor C"),
            ("Aspiradora Robot", "Hogar", 299.99, 3, "Proveedor B"),
            ("Balón de Fútbol", "Deportes", 29.99, 15, "Proveedor C")
        ]
        
        for nombre, categoria, precio, stock, proveedor in productos_iniciales:
            self._crear_producto_interno(nombre, categoria, precio, stock, proveedor)
        
        print(f"✅ Sistema inicializado con {len(self.productos)} productos")
    
    def _crear_producto_interno(self, nombre, categoria, precio, stock, proveedor):
        """Método interno para crear productos sin validaciones extras"""
        producto = {
            "id": self.siguiente_id_producto,
            "nombre": nombre,
            "categoria": categoria,
            "precio_sin_iva": precio,
            "precio_con_iva": precio * (1 + self.iva_porcentaje / 100),
            "stock": stock,
            "stock_minimo": self.stock_minimo_default,
            "proveedor": proveedor,
            "activo": True,
            "fecha_creacion": datetime.datetime.now().isoformat(),
            "usuario_creacion": self.usuario_actual
        }
        self.productos.append(producto)
        self.siguiente_id_producto += 1
        
        # Registrar movimiento
        self._registrar_movimiento("ALTA", producto["id"], stock, "Producto creado")
    
    def mostrar_menu_principal(self):
        """Interfaz de usuario - Menú principal"""
        while True:
            print(f"\n🏛️ SISTEMA DE INVENTARIO MONOLÍTICO")
            print(f"Usuario: {self.usuario_actual} | Productos: {len(self.productos)}")
            print("="*50)
            print("1. 📦 Gestión de Productos")
            print("2. 📊 Inventario y Stock")
            print("3. 📈 Reportes y Estadísticas")
            print("4. 🔄 Movimientos de Stock")
            print("5. ⚙️ Configuración")
            print("6. 💾 Guardar/Cargar Datos")
            print("7. 🚪 Salir")
            print("-"*50)
            
            opcion = input("Selecciona una opción (1-7): ").strip()
            
            if opcion == "1":
                self._menu_productos()
            elif opcion == "2":
                self._menu_inventario()
            elif opcion == "3":
                self._menu_reportes()
            elif opcion == "4":
                self._menu_movimientos()
            elif opcion == "5":
                self._menu_configuracion()
            elif opcion == "6":
                self._menu_datos()
            elif opcion == "7":
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción no válida")
    
    def _menu_productos(self):
        """Submenú de gestión de productos"""
        while True:
            print(f"\n📦 GESTIÓN DE PRODUCTOS")
            print("="*30)
            print("1. Ver todos los productos")
            print("2. Buscar producto")
            print("3. Agregar producto")
            print("4. Modificar producto")
            print("5. Eliminar producto")
            print("6. Volver al menú principal")
            
            opcion = input("Opción: ").strip()
            
            if opcion == "1":
                self.listar_productos()
            elif opcion == "2":
                criterio = input("Buscar por nombre: ")
                self.buscar_productos(criterio)
            elif opcion == "3":
                self.agregar_producto_interactivo()
            elif opcion == "4":
                self.modificar_producto_interactivo()
            elif opcion == "5":
                self.eliminar_producto_interactivo()
            elif opcion == "6":
                break
            else:
                print("❌ Opción no válida")
    
    def listar_productos(self, mostrar_inactivos=False):
        """Muestra lista de todos los productos"""
        productos_filtrados = [p for p in self.productos if mostrar_inactivos or p["activo"]]
        
        if not productos_filtrados:
            print("📭 No hay productos para mostrar")
            return
        
        print(f"\n📋 LISTA DE PRODUCTOS ({len(productos_filtrados)} total)")
        print("="*80)
        print(f"{'ID':<4} {'Nombre':<25} {'Categoría':<12} {'Precio':<10} {'Stock':<6} {'Estado':<8}")
        print("-"*80)
        
        for producto in productos_filtrados:
            estado = "✅ Activo" if producto["activo"] else "❌ Inactivo"
            stock_alerta = "⚠️" if producto["stock"] <= producto["stock_minimo"] else "✅"
            
            print(f"{producto['id']:<4} {producto['nombre']:<25} {producto['categoria']:<12} "
                  f"{producto['precio_sin_iva']:<10.2f}€ {stock_alerta}{producto['stock']:<5} {estado}")
    
    def buscar_productos(self, criterio):
        """Busca productos por nombre o categoría"""
        if not criterio:
            print("❌ Debe ingresar un criterio de búsqueda")
            return
        
        criterio_lower = criterio.lower()
        resultados = []
        
        for producto in self.productos:
            if (criterio_lower in producto["nombre"].lower() or 
                criterio_lower in producto["categoria"].lower() or
                criterio_lower in producto["proveedor"].lower()):
                resultados.append(producto)
        
        if not resultados:
            print(f"📭 No se encontraron productos con '{criterio}'")
            return
        
        print(f"\n🔍 RESULTADOS DE BÚSQUEDA: '{criterio}' ({len(resultados)} encontrados)")
        print("="*70)
        
        for producto in resultados:
            print(f"📦 ID: {producto['id']} | {producto['nombre']}")
            print(f"   📂 Categoría: {producto['categoria']}")
            print(f"   💰 Precio: {producto['precio_sin_iva']:.2f}€ (sin IVA) | {producto['precio_con_iva']:.2f}€ (con IVA)")
            print(f"   📊 Stock: {producto['stock']} unidades | Mínimo: {producto['stock_minimo']}")
            print(f"   🏢 Proveedor: {producto['proveedor']}")
            print()
    
    def agregar_producto_interactivo(self):
        """Interfaz para agregar un nuevo producto"""
        print(f"\n➕ AGREGAR NUEVO PRODUCTO")
        print("="*30)
        
        try:
            # Recopilar datos
            nombre = input("Nombre del producto: ").strip()
            if not nombre or len(nombre) < 3:
                print("❌ El nombre debe tener al menos 3 caracteres")
                return
            
            print(f"Categorías disponibles: {', '.join(self.categorias)}")
            categoria = input("Categoría: ").strip()
            if categoria not in self.categorias:
                print("❌ Categoría no válida")
                return
            
            precio = float(input("Precio sin IVA (€): "))
            if precio <= 0:
                print("❌ El precio debe ser mayor a 0")
                return
            
            stock = int(input("Stock inicial: "))
            if stock < 0:
                print("❌ El stock no puede ser negativo")
                return
            
            stock_minimo = int(input(f"Stock mínimo (default {self.stock_minimo_default}): ") or self.stock_minimo_default)
            
            print(f"Proveedores disponibles: {', '.join(self.proveedores)}")
            proveedor = input("Proveedor: ").strip()
            if proveedor not in self.proveedores:
                print("❌ Proveedor no válido")
                return
            
            # Crear producto
            producto = {
                "id": self.siguiente_id_producto,
                "nombre": nombre,
                "categoria": categoria,
                "precio_sin_iva": precio,
                "precio_con_iva": precio * (1 + self.iva_porcentaje / 100),
                "stock": stock,
                "stock_minimo": stock_minimo,
                "proveedor": proveedor,
                "activo": True,
                "fecha_creacion": datetime.datetime.now().isoformat(),
                "usuario_creacion": self.usuario_actual
            }
            
            self.productos.append(producto)
            self.siguiente_id_producto += 1
            
            # Registrar movimiento
            self._registrar_movimiento("ALTA", producto["id"], stock, "Producto agregado manualmente")
            
            print(f"✅ Producto '{nombre}' agregado exitosamente con ID: {producto['id']}")
            print(f"   💰 Precio con IVA ({self.iva_porcentaje}%): {producto['precio_con_iva']:.2f}€")
            
        except ValueError as e:
            print(f"❌ Error en los datos ingresados: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def modificar_producto_interactivo(self):
        """Interfaz para modificar un producto existente"""
        print(f"\n✏️ MODIFICAR PRODUCTO")
        print("="*25)
        
        try:
            producto_id = int(input("ID del producto a modificar: "))
            producto = self._buscar_producto_por_id(producto_id)
            
            if not producto:
                print("❌ Producto no encontrado")
                return
            
            if not producto["activo"]:
                print("❌ No se puede modificar un producto inactivo")
                return
            
            print(f"\n📦 Producto actual: {producto['nombre']}")
            print(f"   📂 Categoría: {producto['categoria']}")
            print(f"   💰 Precio: {producto['precio_sin_iva']:.2f}€")
            print(f"   📊 Stock: {producto['stock']}")
            print(f"   🏢 Proveedor: {producto['proveedor']}")
            
            print(f"\n¿Qué desea modificar?")
            print("1. Precio")
            print("2. Stock mínimo")
            print("3. Proveedor")
            print("4. Cancelar")
            
            opcion = input("Opción: ").strip()
            
            if opcion == "1":
                nuevo_precio = float(input(f"Nuevo precio sin IVA (actual: {producto['precio_sin_iva']:.2f}€): "))
                if nuevo_precio > 0:
                    producto["precio_sin_iva"] = nuevo_precio
                    producto["precio_con_iva"] = nuevo_precio * (1 + self.iva_porcentaje / 100)
                    print(f"✅ Precio actualizado a {nuevo_precio:.2f}€ (sin IVA)")
                else:
                    print("❌ Precio inválido")
            
            elif opcion == "2":
                nuevo_minimo = int(input(f"Nuevo stock mínimo (actual: {producto['stock_minimo']}): "))
                if nuevo_minimo >= 0:
                    producto["stock_minimo"] = nuevo_minimo
                    print(f"✅ Stock mínimo actualizado a {nuevo_minimo}")
                else:
                    print("❌ Stock mínimo inválido")
            
            elif opcion == "3":
                print(f"Proveedores disponibles: {', '.join(self.proveedores)}")
                nuevo_proveedor = input(f"Nuevo proveedor (actual: {producto['proveedor']}): ").strip()
                if nuevo_proveedor in self.proveedores:
                    producto["proveedor"] = nuevo_proveedor
                    print(f"✅ Proveedor actualizado a {nuevo_proveedor}")
                else:
                    print("❌ Proveedor inválido")
            
            elif opcion == "4":
                print("Modificación cancelada")
            else:
                print("❌ Opción no válida")
                
        except ValueError as e:
            print(f"❌ Error en los datos: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def eliminar_producto_interactivo(self):
        """Interfaz para eliminar (desactivar) un producto"""
        print(f"\n🗑️ ELIMINAR PRODUCTO")
        print("="*22)
        
        try:
            producto_id = int(input("ID del producto a eliminar: "))
            producto = self._buscar_producto_por_id(producto_id)
            
            if not producto:
                print("❌ Producto no encontrado")
                return
            
            if not producto["activo"]:
                print("❌ El producto ya está inactivo")
                return
            
            print(f"\n📦 Producto a eliminar:")
            print(f"   ID: {producto['id']}")
            print(f"   Nombre: {producto['nombre']}")
            print(f"   Stock actual: {producto['stock']}")
            
            if producto['stock'] > 0:
                print(f"⚠️ ATENCIÓN: El producto tiene stock ({producto['stock']} unidades)")
                print("Al eliminarlo, el stock se perderá del inventario")
            
            confirmacion = input("\n¿Está seguro de eliminar este producto? (si/no): ").lower().strip()
            
            if confirmacion in ['si', 'sí', 's', 'yes', 'y']:
                # Registrar movimiento de baja si hay stock
                if producto['stock'] > 0:
                    self._registrar_movimiento("BAJA", producto_id, -producto['stock'], "Producto eliminado")
                
                producto["activo"] = False
                print(f"✅ Producto '{producto['nombre']}' eliminado exitosamente")
            else:
                print("Eliminación cancelada")
                
        except ValueError as e:
            print(f"❌ Error en los datos: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def _menu_inventario(self):
        """Submenú de inventario y stock"""
        while True:
            print(f"\n📊 INVENTARIO Y STOCK")
            print("="*25)
            print("1. Estado general del inventario")
            print("2. Productos con stock bajo")
            print("3. Entrada de stock")
            print("4. Salida de stock")
            print("5. Ajuste de inventario")
            print("6. Volver al menú principal")
            
            opcion = input("Opción: ").strip()
            
            if opcion == "1":
                self.mostrar_estado_inventario()
            elif opcion == "2":
                self.mostrar_stock_bajo()
            elif opcion == "3":
                self.entrada_stock_interactiva()
            elif opcion == "4":
                self.salida_stock_interactiva()
            elif opcion == "5":
                self.ajuste_inventario_interactivo()
            elif opcion == "6":
                break
            else:
                print("❌ Opción no válida")
    
    def mostrar_estado_inventario(self):
        """Muestra el estado general del inventario"""
        productos_activos = [p for p in self.productos if p["activo"]]
        
        if not productos_activos:
            print("📭 No hay productos activos en el inventario")
            return
        
        # Calcular estadísticas
        total_productos = len(productos_activos)
        valor_total_sin_iva = sum(p["precio_sin_iva"] * p["stock"] for p in productos_activos)
        valor_total_con_iva = sum(p["precio_con_iva"] * p["stock"] for p in productos_activos)
        stock_total = sum(p["stock"] for p in productos_activos)
        productos_sin_stock = len([p for p in productos_activos if p["stock"] == 0])
        productos_stock_bajo = len([p for p in productos_activos if 0 < p["stock"] <= p["stock_minimo"]])
        
        # Estadísticas por categoría
        stats_categoria = {}
        for producto in productos_activos:
            cat = producto["categoria"]
            if cat not in stats_categoria:
                stats_categoria[cat] = {"productos": 0, "stock": 0, "valor": 0}
            stats_categoria[cat]["productos"] += 1
            stats_categoria[cat]["stock"] += producto["stock"]
            stats_categoria[cat]["valor"] += producto["precio_sin_iva"] * producto["stock"]
        
        print(f"\n📊 ESTADO GENERAL DEL INVENTARIO")
        print("="*40)
        print(f"📦 Total productos activos: {total_productos}")
        print(f"📊 Stock total: {stock_total:,} unidades")
        print(f"💰 Valor inventario (sin IVA): {valor_total_sin_iva:,.2f}€")
        print(f"💰 Valor inventario (con IVA): {valor_total_con_iva:,.2f}€")
        print(f"📭 Productos sin stock: {productos_sin_stock}")
        print(f"⚠️ Productos con stock bajo: {productos_stock_bajo}")
        
        print(f"\n📂 ESTADÍSTICAS POR CATEGORÍA:")
        print("-"*50)
        for categoria, stats in stats_categoria.items():
            print(f"{categoria:<15} | {stats['productos']:>3} productos | {stats['stock']:>5} unidades | {stats['valor']:>10.2f}€")
    
    def mostrar_stock_bajo(self):
        """Muestra productos con stock bajo o sin stock"""
        productos_activos = [p for p in self.productos if p["activo"]]
        productos_alerta = [p for p in productos_activos if p["stock"] <= p["stock_minimo"]]
        
        if not productos_alerta:
            print("✅ No hay productos con stock bajo")
            return
        
        print(f"\n⚠️ PRODUCTOS CON STOCK BAJO ({len(productos_alerta)} productos)")
        print("="*60)
        print(f"{'ID':<4} {'Nombre':<25} {'Stock':<8} {'Mínimo':<8} {'Estado'}")
        print("-"*60)
        
        for producto in productos_alerta:
            if producto["stock"] == 0:
                estado = "🔴 SIN STOCK"
            elif producto["stock"] <= producto["stock_minimo"]:
                estado = "⚠️ STOCK BAJO"
            else:
                estado = "✅ OK"
            
            print(f"{producto['id']:<4} {producto['nombre']:<25} {producto['stock']:<8} "
                  f"{producto['stock_minimo']:<8} {estado}")
    
    def entrada_stock_interactiva(self):
        """Interfaz para registrar entrada de stock"""
        print(f"\n📥 ENTRADA DE STOCK")
        print("="*20)
        
        try:
            producto_id = int(input("ID del producto: "))
            producto = self._buscar_producto_por_id(producto_id)
            
            if not producto:
                print("❌ Producto no encontrado")
                return
            
            if not producto["activo"]:
                print("❌ No se puede modificar stock de producto inactivo")
                return
            
            print(f"📦 Producto: {producto['nombre']}")
            print(f"📊 Stock actual: {producto['stock']}")
            
            cantidad = int(input("Cantidad a agregar: "))
            if cantidad <= 0:
                print("❌ La cantidad debe ser mayor a 0")
                return
            
            motivo = input("Motivo (opcional): ").strip() or "Entrada de stock"
            
            # Actualizar stock
            producto["stock"] += cantidad
            
            # Registrar movimiento
            self._registrar_movimiento("ENTRADA", producto_id, cantidad, motivo)
            
            print(f"✅ Stock actualizado: {producto['stock']} unidades (+{cantidad})")
            
        except ValueError as e:
            print(f"❌ Error en los datos: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def salida_stock_interactiva(self):
        """Interfaz para registrar salida de stock"""
        print(f"\n📤 SALIDA DE STOCK")
        print("="*19)
        
        try:
            producto_id = int(input("ID del producto: "))
            producto = self._buscar_producto_por_id(producto_id)
            
            if not producto:
                print("❌ Producto no encontrado")
                return
            
            if not producto["activo"]:
                print("❌ No se puede modificar stock de producto inactivo")
                return
            
            print(f"📦 Producto: {producto['nombre']}")
            print(f"📊 Stock actual: {producto['stock']}")
            
            cantidad = int(input("Cantidad a retirar: "))
            if cantidad <= 0:
                print("❌ La cantidad debe ser mayor a 0")
                return
            
            if cantidad > producto["stock"]:
                print(f"❌ Stock insuficiente. Disponible: {producto['stock']}")
                return
            
            motivo = input("Motivo (opcional): ").strip() or "Salida de stock"
            
            # Actualizar stock
            producto["stock"] -= cantidad
            
            # Registrar movimiento
            self._registrar_movimiento("SALIDA", producto_id, -cantidad, motivo)
            
            print(f"✅ Stock actualizado: {producto['stock']} unidades (-{cantidad})")
            
            # Alerta si queda stock bajo
            if producto["stock"] <= producto["stock_minimo"]:
                print(f"⚠️ ALERTA: Stock bajo ({producto['stock']} <= {producto['stock_minimo']})")
            
        except ValueError as e:
            print(f"❌ Error en los datos: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def ajuste_inventario_interactivo(self):
        """Interfaz para ajustar inventario (correcciones)"""
        print(f"\n🔧 AJUSTE DE INVENTARIO")
        print("="*25)
        
        try:
            producto_id = int(input("ID del producto: "))
            producto = self._buscar_producto_por_id(producto_id)
            
            if not producto:
                print("❌ Producto no encontrado")
                return
            
            if not producto["activo"]:
                print("❌ No se puede ajustar stock de producto inactivo")
                return
            
            print(f"📦 Producto: {producto['nombre']}")
            print(f"📊 Stock actual: {producto['stock']}")
            
            nuevo_stock = int(input("Nuevo stock correcto: "))
            if nuevo_stock < 0:
                print("❌ El stock no puede ser negativo")
                return
            
            diferencia = nuevo_stock - producto["stock"]
            
            if diferencia == 0:
                print("ℹ️ El stock ya es correcto")
                return
            
            motivo = input("Motivo del ajuste: ").strip()
            if not motivo:
                motivo = f"Ajuste de inventario ({'+' if diferencia > 0 else ''}{diferencia})"
            
            print(f"\n📋 RESUMEN DEL AJUSTE:")
            print(f"   Stock actual: {producto['stock']}")
            print(f"   Stock nuevo: {nuevo_stock}")
            print(f"   Diferencia: {'+' if diferencia > 0 else ''}{diferencia}")
            print(f"   Motivo: {motivo}")
            
            confirmacion = input("\n¿Confirmar ajuste? (si/no): ").lower().strip()
            
            if confirmacion in ['si', 'sí', 's', 'yes', 'y']:
                # Actualizar stock
                producto["stock"] = nuevo_stock
                
                # Registrar movimiento
                self._registrar_movimiento("AJUSTE", producto_id, diferencia, motivo)
                
                print(f"✅ Inventario ajustado: {nuevo_stock} unidades")
            else:
                print("Ajuste cancelado")
            
        except ValueError as e:
            print(f"❌ Error en los datos: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def _menu_reportes(self):
        """Submenú de reportes y estadísticas"""
        while True:
            print(f"\n📈 REPORTES Y ESTADÍSTICAS")
            print("="*30)
            print("1. Reporte de productos")
            print("2. Reporte de movimientos")
            print("3. Análisis de categorías")
            print("4. Análisis de proveedores")
            print("5. Productos más/menos valiosos")
            print("6. Exportar datos")
            print("7. Volver al menú principal")
            
            opcion = input("Opción: ").strip()
            
            if opcion == "1":
                self.generar_reporte_productos()
            elif opcion == "2":
                self.generar_reporte_movimientos()
            elif opcion == "3":
                self.generar_analisis_categorias()
            elif opcion == "4":
                self.generar_analisis_proveedores()
            elif opcion == "5":
                self.generar_ranking_productos()
            elif opcion == "6":
                self.exportar_datos()
            elif opcion == "7":
                break
            else:
                print("❌ Opción no válida")
    
    def generar_reporte_productos(self):
        """Genera reporte detallado de productos"""
        productos_activos = [p for p in self.productos if p["activo"]]
        
        if not productos_activos:
            print("📭 No hay productos activos")
            return
        
        print(f"\n📋 REPORTE DETALLADO DE PRODUCTOS")
        print("="*50)
        print(f"Fecha: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total productos: {len(productos_activos)}")
        print()
        
        for producto in productos_activos:
            valor_stock = producto["precio_sin_iva"] * producto["stock"]
            estado_stock = "🔴" if producto["stock"] == 0 else "⚠️" if producto["stock"] <= producto["stock_minimo"] else "✅"
            
            print(f"📦 {producto['nombre']} (ID: {producto['id']})")
            print(f"   📂 Categoría: {producto['categoria']}")
            print(f"   🏢 Proveedor: {producto['proveedor']}")
            print(f"   💰 Precio: {producto['precio_sin_iva']:.2f}€ (sin IVA) | {producto['precio_con_iva']:.2f}€ (con IVA)")
            print(f"   📊 Stock: {estado_stock} {producto['stock']} unidades (mínimo: {producto['stock_minimo']})")
            print(f"   💵 Valor en stock: {valor_stock:.2f}€")
            print(f"   📅 Creado: {producto['fecha_creacion'][:10]} por {producto['usuario_creacion']}")
            print()
    
    def generar_reporte_movimientos(self):
        """Genera reporte de movimientos de stock"""
        if not self.historial_movimientos:
            print("📭 No hay movimientos registrados")
            return
        
        # Mostrar últimos 20 movimientos
        movimientos_recientes = self.historial_movimientos[-20:]
        
        print(f"\n🔄 REPORTE DE MOVIMIENTOS (últimos {len(movimientos_recientes)})")
        print("="*60)
        print(f"{'ID':<4} {'Fecha':<12} {'Tipo':<8} {'Producto':<20} {'Cant.':<6} {'Motivo'}")
        print("-"*60)
        
        for mov in reversed(movimientos_recientes):
            producto = self._buscar_producto_por_id(mov["producto_id"])
            nombre_producto = producto["nombre"][:20] if producto else "N/A"
            fecha = mov["fecha"][:10]
            
            print(f"{mov['id']:<4} {fecha:<12} {mov['tipo']:<8} {nombre_producto:<20} "
                  f"{mov['cantidad']:>+6} {mov['motivo']}")
    
    def generar_analisis_categorias(self):
        """Análisis por categorías"""
        productos_activos = [p for p in self.productos if p["activo"]]
        
        if not productos_activos:
            print("📭 No hay productos activos")
            return
        
        # Agrupar por categorías
        stats_categoria = {}
        for producto in productos_activos:
            cat = producto["categoria"]
            if cat not in stats_categoria:
                stats_categoria[cat] = {
                    "productos": 0,
                    "stock_total": 0,
                    "valor_sin_iva": 0,
                    "valor_con_iva": 0,
                    "stock_bajo": 0,
                    "sin_stock": 0
                }
            
            stats = stats_categoria[cat]
            stats["productos"] += 1
            stats["stock_total"] += producto["stock"]
            stats["valor_sin_iva"] += producto["precio_sin_iva"] * producto["stock"]
            stats["valor_con_iva"] += producto["precio_con_iva"] * producto["stock"]
            
            if producto["stock"] == 0:
                stats["sin_stock"] += 1
            elif producto["stock"] <= producto["stock_minimo"]:
                stats["stock_bajo"] += 1
        
        print(f"\n📂 ANÁLISIS POR CATEGORÍAS")
        print("="*40)
        
        for categoria, stats in sorted(stats_categoria.items()):
            print(f"\n📁 {categoria.upper()}")
            print(f"   📦 Productos: {stats['productos']}")
            print(f"   📊 Stock total: {stats['stock_total']:,} unidades")
            print(f"   💰 Valor inventario: {stats['valor_sin_iva']:,.2f}€ (sin IVA)")
            print(f"   💰 Valor con IVA: {stats['valor_con_iva']:,.2f}€")
            print(f"   ⚠️ Stock bajo: {stats['stock_bajo']} productos")
            print(f"   🔴 Sin stock: {stats['sin_stock']} productos")
    
    def generar_analisis_proveedores(self):
        """Análisis por proveedores"""
        productos_activos = [p for p in self.productos if p["activo"]]
        
        if not productos_activos:
            print("📭 No hay productos activos")
            return
        
        # Agrupar por proveedores
        stats_proveedor = {}
        for producto in productos_activos:
            prov = producto["proveedor"]
            if prov not in stats_proveedor:
                stats_proveedor[prov] = {
                    "productos": 0,
                    "categorias": set(),
                    "stock_total": 0,
                    "valor_inventario": 0
                }
            
            stats = stats_proveedor[prov]
            stats["productos"] += 1
            stats["categorias"].add(producto["categoria"])
            stats["stock_total"] += producto["stock"]
            stats["valor_inventario"] += producto["precio_sin_iva"] * producto["stock"]
        
        print(f"\n🏢 ANÁLISIS POR PROVEEDORES")
        print("="*35)
        
        for proveedor, stats in sorted(stats_proveedor.items()):
            print(f"\n🏢 {proveedor.upper()}")
            print(f"   📦 Productos: {stats['productos']}")
            print(f"   📂 Categorías: {', '.join(sorted(stats['categorias']))}")
            print(f"   📊 Stock total: {stats['stock_total']:,} unidades")
            print(f"   💰 Valor inventario: {stats['valor_inventario']:,.2f}€")
    
    def generar_ranking_productos(self):
        """Ranking de productos por valor"""
        productos_activos = [p for p in self.productos if p["activo"]]
        
        if not productos_activos:
            print("📭 No hay productos activos")
            return
        
        # Calcular valor de inventario para cada producto
        productos_con_valor = []
        for producto in productos_activos:
            valor = producto["precio_sin_iva"] * producto["stock"]
            productos_con_valor.append((producto, valor))
        
        # Ordenar por valor descendente
        productos_con_valor.sort(key=lambda x: x[1], reverse=True)
        
        print(f"\n🏆 RANKING DE PRODUCTOS POR VALOR DE INVENTARIO")
        print("="*55)
        print(f"{'Pos':<4} {'Producto':<25} {'Stock':<8} {'P.Unit':<10} {'Valor Total'}")
        print("-"*55)
        
        for i, (producto, valor) in enumerate(productos_con_valor[:10], 1):
            print(f"{i:<4} {producto['nombre'][:25]:<25} {producto['stock']:<8} "
                  f"{producto['precio_sin_iva']:<10.2f}€ {valor:>10.2f}€")
        
        if len(productos_con_valor) > 10:
            print(f"\n... y {len(productos_con_valor) - 10} productos más")
    
    def exportar_datos(self):
        """Exporta datos del sistema"""
        print(f"\n💾 EXPORTAR DATOS")
        print("="*18)
        print("1. Exportar productos (JSON)")
        print("2. Exportar movimientos (JSON)")
        print("3. Exportar todo (JSON)")
        print("4. Cancelar")
        
        opcion = input("Opción: ").strip()
        
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            
            if opcion == "1":
                filename = f"productos_{timestamp}.json"
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(self.productos, f, indent=2, ensure_ascii=False)
                print(f"✅ Productos exportados a: {filename}")
            
            elif opcion == "2":
                filename = f"movimientos_{timestamp}.json"
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(self.historial_movimientos, f, indent=2, ensure_ascii=False)
                print(f"✅ Movimientos exportados a: {filename}")
            
            elif opcion == "3":
                data = {
                    "sistema": {
                        "version": self.version,
                        "empresa": self.nombre_empresa,
                        "fecha_exportacion": datetime.datetime.now().isoformat()
                    },
                    "productos": self.productos,
                    "movimientos": self.historial_movimientos,
                    "configuracion": {
                        "categorias": self.categorias,
                        "proveedores": self.proveedores,
                        "iva_porcentaje": self.iva_porcentaje,
                        "stock_minimo_default": self.stock_minimo_default
                    }
                }
                filename = f"inventario_completo_{timestamp}.json"
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"✅ Datos completos exportados a: {filename}")
            
            elif opcion == "4":
                print("Exportación cancelada")
            else:
                print("❌ Opción no válida")
                
        except Exception as e:
            print(f"❌ Error al exportar: {e}")
    
    def _menu_movimientos(self):
        """Submenú de movimientos de stock"""
        print(f"\n🔄 HISTORIAL DE MOVIMIENTOS")
        print("="*32)
        
        if not self.historial_movimientos:
            print("📭 No hay movimientos registrados")
            input("Presiona Enter para continuar...")
            return
        
        # Mostrar estadísticas de movimientos
        total_movimientos = len(self.historial_movimientos)
        tipos_movimientos = {}
        
        for mov in self.historial_movimientos:
            tipo = mov["tipo"]
            tipos_movimientos[tipo] = tipos_movimientos.get(tipo, 0) + 1
        
        print(f"📊 Total movimientos: {total_movimientos}")
        for tipo, cantidad in tipos_movimientos.items():
            print(f"   {tipo}: {cantidad} movimientos")
        
        print(f"\n🔄 ÚLTIMOS 15 MOVIMIENTOS:")
        print("-"*70)
        
        movimientos_recientes = self.historial_movimientos[-15:]
        for mov in reversed(movimientos_recientes):
            producto = self._buscar_producto_por_id(mov["producto_id"])
            nombre_producto = producto["nombre"] if producto else "Producto eliminado"
            
            print(f"{mov['fecha'][:16]} | {mov['tipo']:<8} | {nombre_producto[:25]:<25} | "
                  f"{mov['cantidad']:>+4} | {mov['motivo']}")
        
        input("\nPresiona Enter para continuar...")
    
    def _menu_configuracion(self):
        """Submenú de configuración del sistema"""
        while True:
            print(f"\n⚙️ CONFIGURACIÓN DEL SISTEMA")
            print("="*32)
            print(f"Usuario actual: {self.usuario_actual}")
            print(f"IVA: {self.iva_porcentaje}%")
            print(f"Stock mínimo por defecto: {self.stock_minimo_default}")
            print()
            print("1. Cambiar usuario")
            print("2. Configurar IVA")
            print("3. Configurar stock mínimo por defecto")
            print("4. Gestionar categorías")
            print("5. Gestionar proveedores")
            print("6. Información del sistema")
            print("7. Volver al menú principal")
            
            opcion = input("Opción: ").strip()
            
            if opcion == "1":
                self._cambiar_usuario()
            elif opcion == "2":
                self._configurar_iva()
            elif opcion == "3":
                self._configurar_stock_minimo()
            elif opcion == "4":
                self._gestionar_categorias()
            elif opcion == "5":
                self._gestionar_proveedores()
            elif opcion == "6":
                self._mostrar_info_sistema()
            elif opcion == "7":
                break
            else:
                print("❌ Opción no válida")
    
    def _cambiar_usuario(self):
        """Cambiar usuario actual del sistema"""
        print(f"\n👤 CAMBIAR USUARIO")
        print("="*18)
        print(f"Usuario actual: {self.usuario_actual}")
        print(f"Usuarios disponibles: {', '.join(self.usuarios)}")
        
        nuevo_usuario = input("Nuevo usuario: ").strip()
        if nuevo_usuario in self.usuarios:
            self.usuario_actual = nuevo_usuario
            print(f"✅ Usuario cambiado a: {nuevo_usuario}")
        else:
            print("❌ Usuario no válido")
    
    def _configurar_iva(self):
        """Configurar porcentaje de IVA"""
        print(f"\n💰 CONFIGURAR IVA")
        print("="*17)
        print(f"IVA actual: {self.iva_porcentaje}%")
        
        try:
            nuevo_iva = float(input("Nuevo porcentaje de IVA: "))
            if 0 <= nuevo_iva <= 50:  # Rango razonable
                self.iva_porcentaje = nuevo_iva
                
                # Recalcular precios con IVA para todos los productos
                for producto in self.productos:
                    producto["precio_con_iva"] = producto["precio_sin_iva"] * (1 + nuevo_iva / 100)
                
                print(f"✅ IVA actualizado a {nuevo_iva}%")
                print("✅ Precios con IVA recalculados para todos los productos")
            else:
                print("❌ Porcentaje de IVA debe estar entre 0 y 50")
        except ValueError:
            print("❌ Valor inválido")
    
    def _configurar_stock_minimo(self):
        """Configurar stock mínimo por defecto"""
        print(f"\n📊 CONFIGURAR STOCK MÍNIMO POR DEFECTO")
        print("="*38)
        print(f"Stock mínimo actual: {self.stock_minimo_default}")
        
        try:
            nuevo_minimo = int(input("Nuevo stock mínimo por defecto: "))
            if nuevo_minimo >= 0:
                self.stock_minimo_default = nuevo_minimo
                print(f"✅ Stock mínimo por defecto actualizado a {nuevo_minimo}")
                print("ℹ️ Esto solo afecta a nuevos productos")
            else:
                print("❌ El stock mínimo no puede ser negativo")
        except ValueError:
            print("❌ Valor inválido")
    
    def _gestionar_categorias(self):
        """Gestionar categorías de productos"""
        print(f"\n📂 GESTIONAR CATEGORÍAS")
        print("="*25)
        print(f"Categorías actuales: {', '.join(self.categorias)}")
        print()
        print("1. Agregar categoría")
        print("2. Eliminar categoría")
        print("3. Volver")
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            nueva_categoria = input("Nueva categoría: ").strip()
            if nueva_categoria and nueva_categoria not in self.categorias:
                self.categorias.append(nueva_categoria)
                print(f"✅ Categoría '{nueva_categoria}' agregada")
            else:
                print("❌ Categoría inválida o ya existe")
        
        elif opcion == "2":
            categoria = input("Categoría a eliminar: ").strip()
            if categoria in self.categorias:
                # Verificar si hay productos con esta categoría
                productos_con_categoria = [p for p in self.productos if p["categoria"] == categoria and p["activo"]]
                if productos_con_categoria:
                    print(f"❌ No se puede eliminar. Hay {len(productos_con_categoria)} productos con esta categoría")
                else:
                    self.categorias.remove(categoria)
                    print(f"✅ Categoría '{categoria}' eliminada")
            else:
                print("❌ Categoría no encontrada")
    
    def _gestionar_proveedores(self):
        """Gestionar proveedores"""
        print(f"\n🏢 GESTIONAR PROVEEDORES")
        print("="*26)
        print(f"Proveedores actuales: {', '.join(self.proveedores)}")
        print()
        print("1. Agregar proveedor")
        print("2. Eliminar proveedor")
        print("3. Volver")
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            nuevo_proveedor = input("Nuevo proveedor: ").strip()
            if nuevo_proveedor and nuevo_proveedor not in self.proveedores:
                self.proveedores.append(nuevo_proveedor)
                print(f"✅ Proveedor '{nuevo_proveedor}' agregado")
            else:
                print("❌ Proveedor inválido o ya existe")
        
        elif opcion == "2":
            proveedor = input("Proveedor a eliminar: ").strip()
            if proveedor in self.proveedores:
                # Verificar si hay productos con este proveedor
                productos_con_proveedor = [p for p in self.productos if p["proveedor"] == proveedor and p["activo"]]
                if productos_con_proveedor:
                    print(f"❌ No se puede eliminar. Hay {len(productos_con_proveedor)} productos de este proveedor")
                else:
                    self.proveedores.remove(proveedor)
                    print(f"✅ Proveedor '{proveedor}' eliminado")
            else:
                print("❌ Proveedor no encontrado")
    
    def _mostrar_info_sistema(self):
        """Muestra información del sistema"""
        print(f"\n🖥️ INFORMACIÓN DEL SISTEMA")
        print("="*30)
        print(f"Empresa: {self.nombre_empresa}")
        print(f"Versión: {self.version}")
        print(f"Usuario actual: {self.usuario_actual}")
        print(f"Total productos: {len(self.productos)}")
        print(f"Productos activos: {len([p for p in self.productos if p['activo']])}")
        print(f"Total movimientos: {len(self.historial_movimientos)}")
        print(f"Categorías: {len(self.categorias)}")
        print(f"Proveedores: {len(self.proveedores)}")
        print(f"IVA configurado: {self.iva_porcentaje}%")
        print(f"Stock mínimo por defecto: {self.stock_minimo_default}")
        
        input("\nPresiona Enter para continuar...")
    
    def _menu_datos(self):
        """Submenú para guardar/cargar datos"""
        print(f"\n💾 GESTIÓN DE DATOS")
        print("="*20)
        print("1. Guardar datos")
        print("2. Cargar datos")
        print("3. Volver al menú principal")
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            self._guardar_datos()
        elif opcion == "2":
            self._cargar_datos()
        elif opcion == "3":
            pass
        else:
            print("❌ Opción no válida")
    
    def _guardar_datos(self):
        """Guarda todos los datos del sistema"""
        try:
            data = {
                "sistema": {
                    "version": self.version,
                    "empresa": self.nombre_empresa,
                    "fecha_guardado": datetime.datetime.now().isoformat(),
                    "usuario": self.usuario_actual
                },
                "productos": self.productos,
                "movimientos": self.historial_movimientos,
                "configuracion": {
                    "categorias": self.categorias,
                    "proveedores": self.proveedores,
                    "usuarios": self.usuarios,
                    "iva_porcentaje": self.iva_porcentaje,
                    "stock_minimo_default": self.stock_minimo_default,
                    "siguiente_id_producto": self.siguiente_id_producto,
                    "siguiente_id_movimiento": self.siguiente_id_movimiento
                }
            }
            
            with open(self.archivo_datos, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Datos guardados en: {self.archivo_datos}")
            
        except Exception as e:
            print(f"❌ Error al guardar: {e}")
    
    def _cargar_datos(self):
        """Carga datos del sistema desde archivo"""
        try:
            with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Cargar datos
            self.productos = data.get("productos", [])
            self.historial_movimientos = data.get("movimientos", [])
            
            # Cargar configuración
            config = data.get("configuracion", {})
            self.categorias = config.get("categorias", self.categorias)
            self.proveedores = config.get("proveedores", self.proveedores)
            self.usuarios = config.get("usuarios", self.usuarios)
            self.iva_porcentaje = config.get("iva_porcentaje", self.iva_porcentaje)
            self.stock_minimo_default = config.get("stock_minimo_default", self.stock_minimo_default)
            self.siguiente_id_producto = config.get("siguiente_id_producto", self.siguiente_id_producto)
            self.siguiente_id_movimiento = config.get("siguiente_id_movimiento", self.siguiente_id_movimiento)
            
            sistema_info = data.get("sistema", {})
            fecha_guardado = sistema_info.get("fecha_guardado", "N/A")
            
            print(f"✅ Datos cargados exitosamente")
            print(f"   Fecha guardado: {fecha_guardado[:19] if fecha_guardado != 'N/A' else 'N/A'}")
            print(f"   Productos cargados: {len(self.productos)}")
            print(f"   Movimientos cargados: {len(self.historial_movimientos)}")
            
        except FileNotFoundError:
            print(f"❌ Archivo no encontrado: {self.archivo_datos}")
        except json.JSONDecodeError:
            print(f"❌ Error en el formato del archivo")
        except Exception as e:
            print(f"❌ Error al cargar: {e}")
    
    # Métodos auxiliares
    def _buscar_producto_por_id(self, producto_id):
        """Busca un producto por ID"""
        for producto in self.productos:
            if producto["id"] == producto_id:
                return producto
        return None
    
    def _registrar_movimiento(self, tipo, producto_id, cantidad, motivo):
        """Registra un movimiento en el historial"""
        movimiento = {
            "id": self.siguiente_id_movimiento,
            "fecha": datetime.datetime.now().isoformat(),
            "tipo": tipo,
            "producto_id": producto_id,
            "cantidad": cantidad,
            "motivo": motivo,
            "usuario": self.usuario_actual
        }
        
        self.historial_movimientos.append(movimiento)
        self.siguiente_id_movimiento += 1

def main():
    """Función principal del sistema"""
    try:
        print("🏛️ INICIANDO SISTEMA DE INVENTARIO MONOLÍTICO")
        print("="*50)
        
        # Crear e inicializar sistema
        sistema = SistemaInventarioMonolitico()
        
        # Mostrar menú principal
        sistema.mostrar_menu_principal()
        
    except KeyboardInterrupt:
        print("\n\n👋 Sistema interrumpido por el usuario")
    except Exception as e:
        print(f"\n❌ Error crítico del sistema: {e}")
        print("Por favor, contacte al administrador")

if __name__ == "__main__":
    main()
