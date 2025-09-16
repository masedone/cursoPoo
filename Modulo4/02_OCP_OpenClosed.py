## 🔹 PRINCIPIO SOLID 2: OPEN/CLOSED PRINCIPLE (OCP)
# "Las clases deben estar abiertas a extensión pero cerradas a modificación"

print("=== PRINCIPIO OCP - ABIERTO/CERRADO ===\n")

# ❌ VIOLACIÓN DE OCP - Modificar código existente para agregar funcionalidad
print("❌ VIOLACIÓN DE OCP - Modificar código existente:")

class CalculadoraMala:
    """VIOLA OCP: Para agregar operaciones hay que modificar esta clase"""
    
    def calcular(self, operacion, a, b):
        if operacion == "suma":
            return a + b
        elif operacion == "resta":
            return a - b
        elif operacion == "multiplicacion":
            return a * b
        elif operacion == "division":
            if b != 0:
                return a / b
            else:
                raise ValueError("División por cero")
        # ❌ Para agregar potencia, hay que MODIFICAR esta clase
        elif operacion == "potencia":
            return a ** b
        # ❌ Para agregar raíz, hay que MODIFICAR esta clase otra vez
        elif operacion == "raiz":
            return a ** (1/b)
        else:
            raise ValueError(f"Operación no soportada: {operacion}")

# Uso problemático
print("Usando calculadora que viola OCP:")
calc_mala = CalculadoraMala()
print(f"Suma: {calc_mala.calcular('suma', 10, 5)}")
print(f"Resta: {calc_mala.calcular('resta', 10, 5)}")
print(f"Multiplicación: {calc_mala.calcular('multiplicacion', 10, 5)}")
print(f"División: {calc_mala.calcular('division', 10, 5)}")

# Problema: Para agregar nuevas operaciones, hay que modificar la clase
try:
    print(f"Módulo: {calc_mala.calcular('modulo', 10, 3)}")  # No existe
except ValueError as e:
    print(f"❌ Error: {e}")

print("\n" + "="*70 + "\n")

# ✅ APLICANDO OCP - Extensible sin modificación
print("✅ APLICANDO OCP - Extensible sin modificación:")

from abc import ABC, abstractmethod

class Operacion(ABC):
    """Clase abstracta que define el contrato para operaciones"""
    
    @abstractmethod
    def calcular(self, a, b):
        """Método que debe implementar cada operación"""
        pass
    
    @abstractmethod
    def obtener_nombre(self):
        """Nombre de la operación"""
        pass
    
    def validar_operandos(self, a, b):
        """Validación común para todas las operaciones"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Los operandos deben ser números")
        return True

# Implementaciones específicas de operaciones
class Suma(Operacion):
    def calcular(self, a, b):
        self.validar_operandos(a, b)
        resultado = a + b
        print(f"➕ {a} + {b} = {resultado}")
        return resultado
    
    def obtener_nombre(self):
        return "Suma"

class Resta(Operacion):
    def calcular(self, a, b):
        self.validar_operandos(a, b)
        resultado = a - b
        print(f"➖ {a} - {b} = {resultado}")
        return resultado
    
    def obtener_nombre(self):
        return "Resta"

class Multiplicacion(Operacion):
    def calcular(self, a, b):
        self.validar_operandos(a, b)
        resultado = a * b
        print(f"✖️ {a} × {b} = {resultado}")
        return resultado
    
    def obtener_nombre(self):
        return "Multiplicación"

class Division(Operacion):
    def calcular(self, a, b):
        self.validar_operandos(a, b)
        if b == 0:
            raise ValueError("División por cero no permitida")
        resultado = a / b
        print(f"➗ {a} ÷ {b} = {resultado}")
        return resultado
    
    def obtener_nombre(self):
        return "División"

# ✅ EXTENSIONES SIN MODIFICAR CÓDIGO EXISTENTE
class Potencia(Operacion):
    """Nueva operación SIN modificar código existente"""
    def calcular(self, a, b):
        self.validar_operandos(a, b)
        resultado = a ** b
        print(f"🔺 {a}^{b} = {resultado}")
        return resultado
    
    def obtener_nombre(self):
        return "Potencia"

class Modulo(Operacion):
    """Otra nueva operación SIN modificar código existente"""
    def calcular(self, a, b):
        self.validar_operandos(a, b)
        if b == 0:
            raise ValueError("Módulo por cero no permitido")
        resultado = a % b
        print(f"📐 {a} mod {b} = {resultado}")
        return resultado
    
    def obtener_nombre(self):
        return "Módulo"

class RaizCuadrada(Operacion):
    """Operación especial que solo usa el primer operando"""
    def calcular(self, a, b=2):
        self.validar_operandos(a, b)
        if a < 0:
            raise ValueError("No se puede calcular raíz de número negativo")
        resultado = a ** (1/b)
        print(f"√ {a} = {resultado}")
        return resultado
    
    def obtener_nombre(self):
        return "Raíz"

class CalculadoraBuena:
    """CUMPLE OCP: Extensible sin modificación"""
    
    def __init__(self):
        self.operaciones = {}
    
    def registrar_operacion(self, nombre, operacion):
        """Permite registrar nuevas operaciones dinámicamente"""
        if not isinstance(operacion, Operacion):
            raise TypeError("La operación debe heredar de Operacion")
        self.operaciones[nombre] = operacion
        print(f"✅ Operación '{nombre}' registrada")
    
    def calcular(self, nombre_operacion, a, b):
        """Ejecuta una operación registrada"""
        if nombre_operacion not in self.operaciones:
            raise ValueError(f"Operación '{nombre_operacion}' no registrada")
        
        operacion = self.operaciones[nombre_operacion]
        return operacion.calcular(a, b)
    
    def listar_operaciones(self):
        """Lista todas las operaciones disponibles"""
        print("📋 Operaciones disponibles:")
        for nombre, operacion in self.operaciones.items():
            print(f"  - {nombre}: {operacion.obtener_nombre()}")
    
    def ejecutar_todas_operaciones(self, a, b):
        """Ejecuta todas las operaciones registradas"""
        print(f"🔄 Ejecutando todas las operaciones con {a} y {b}:")
        resultados = {}
        
        for nombre, operacion in self.operaciones.items():
            try:
                resultado = operacion.calcular(a, b)
                resultados[nombre] = resultado
            except Exception as e:
                print(f"❌ Error en {nombre}: {e}")
                resultados[nombre] = None
        
        return resultados

# Uso con OCP (mucho mejor):
print("Usando calculadora que cumple OCP:")

# Crear calculadora
calc_buena = CalculadoraBuena()

# Registrar operaciones básicas
calc_buena.registrar_operacion("suma", Suma())
calc_buena.registrar_operacion("resta", Resta())
calc_buena.registrar_operacion("multiplicacion", Multiplicacion())
calc_buena.registrar_operacion("division", Division())

print("\nOperaciones básicas registradas:")
calc_buena.listar_operaciones()

print(f"\nEjecutando operaciones básicas:")
print(f"Suma: {calc_buena.calcular('suma', 10, 5)}")
print(f"División: {calc_buena.calcular('division', 10, 5)}")

print("\n" + "="*50 + "\n")

# ✅ EXTENSIÓN SIN MODIFICACIÓN - Agregar nuevas operaciones
print("🔧 EXTENDIENDO sin modificar código existente:")

# Agregar nuevas operaciones SIN modificar la calculadora
calc_buena.registrar_operacion("potencia", Potencia())
calc_buena.registrar_operacion("modulo", Modulo())
calc_buena.registrar_operacion("raiz", RaizCuadrada())

print("\nTodas las operaciones disponibles:")
calc_buena.listar_operaciones()

print(f"\nUsando nuevas operaciones:")
print(f"Potencia: {calc_buena.calcular('potencia', 2, 8)}")
print(f"Módulo: {calc_buena.calcular('modulo', 17, 5)}")

print("\n" + "="*50 + "\n")

# 🔸 EJEMPLO AVANZADO: Sistema de descuentos extensible
print("🔸 EJEMPLO AVANZADO: Sistema de descuentos extensible")

class EstrategiaDescuento(ABC):
    """Interfaz para estrategias de descuento"""
    
    @abstractmethod
    def calcular_descuento(self, precio_original, datos_cliente=None):
        pass
    
    @abstractmethod
    def obtener_descripcion(self):
        pass

class DescuentoEstudiante(EstrategiaDescuento):
    def calcular_descuento(self, precio_original, datos_cliente=None):
        descuento = precio_original * 0.15  # 15% descuento
        precio_final = precio_original - descuento
        print(f"🎓 Descuento estudiante: -{descuento:.2f}€")
        return precio_final
    
    def obtener_descripcion(self):
        return "Descuento para estudiantes (15%)"

class DescuentoSenior(EstrategiaDescuento):
    def calcular_descuento(self, precio_original, datos_cliente=None):
        descuento = precio_original * 0.20  # 20% descuento
        precio_final = precio_original - descuento
        print(f"👴 Descuento senior: -{descuento:.2f}€")
        return precio_final
    
    def obtener_descripcion(self):
        return "Descuento para mayores de 65 años (20%)"

class DescuentoVIP(EstrategiaDescuento):
    def calcular_descuento(self, precio_original, datos_cliente=None):
        descuento = precio_original * 0.25  # 25% descuento
        precio_final = precio_original - descuento
        print(f"⭐ Descuento VIP: -{descuento:.2f}€")
        return precio_final
    
    def obtener_descripcion(self):
        return "Descuento VIP (25%)"

# ✅ NUEVA ESTRATEGIA SIN MODIFICAR CÓDIGO EXISTENTE
class DescuentoBlackFriday(EstrategiaDescuento):
    """Nueva estrategia agregada sin modificar código existente"""
    def calcular_descuento(self, precio_original, datos_cliente=None):
        descuento = precio_original * 0.50  # 50% descuento
        precio_final = precio_original - descuento
        print(f"🖤 Descuento Black Friday: -{descuento:.2f}€")
        return precio_final
    
    def obtener_descripcion(self):
        return "Descuento Black Friday (50%)"

class CalculadoraPrecio:
    """CUMPLE OCP: Extensible con nuevas estrategias de descuento"""
    
    def __init__(self):
        self.estrategias_descuento = {}
    
    def registrar_estrategia(self, nombre, estrategia):
        if not isinstance(estrategia, EstrategiaDescuento):
            raise TypeError("Debe ser una EstrategiaDescuento")
        self.estrategias_descuento[nombre] = estrategia
        print(f"✅ Estrategia '{nombre}' registrada")
    
    def calcular_precio_con_descuento(self, precio_original, tipo_descuento, datos_cliente=None):
        if tipo_descuento not in self.estrategias_descuento:
            print(f"❌ Estrategia '{tipo_descuento}' no encontrada")
            return precio_original
        
        estrategia = self.estrategias_descuento[tipo_descuento]
        print(f"💰 Precio original: {precio_original:.2f}€")
        print(f"📋 Aplicando: {estrategia.obtener_descripcion()}")
        
        precio_final = estrategia.calcular_descuento(precio_original, datos_cliente)
        print(f"💵 Precio final: {precio_final:.2f}€")
        return precio_final
    
    def listar_descuentos_disponibles(self):
        print("📋 Descuentos disponibles:")
        for nombre, estrategia in self.estrategias_descuento.items():
            print(f"  - {nombre}: {estrategia.obtener_descripcion()}")

# Uso del sistema de descuentos
print("\nSistema de descuentos extensible:")
calculadora_precio = CalculadoraPrecio()

# Registrar estrategias básicas
calculadora_precio.registrar_estrategia("estudiante", DescuentoEstudiante())
calculadora_precio.registrar_estrategia("senior", DescuentoSenior())
calculadora_precio.registrar_estrategia("vip", DescuentoVIP())

# Listar descuentos
calculadora_precio.listar_descuentos_disponibles()

# Aplicar descuentos
print(f"\n🛒 Calculando precios para producto de 100€:")
calculadora_precio.calcular_precio_con_descuento(100, "estudiante")
print()
calculadora_precio.calcular_precio_con_descuento(100, "vip")

# ✅ EXTENSIÓN: Agregar nueva estrategia sin modificar código
print(f"\n🔧 Agregando nueva estrategia Black Friday:")
calculadora_precio.registrar_estrategia("blackfriday", DescuentoBlackFriday())

print()
calculadora_precio.calcular_precio_con_descuento(100, "blackfriday")

print("\n=== VENTAJAS DE APLICAR OCP ===")
print("✅ Agregar funcionalidad sin modificar código existente")
print("✅ Reduce el riesgo de introducir bugs")
print("✅ Código más mantenible y extensible")
print("✅ Fácil testing de nuevas funcionalidades")
print("✅ Cumple el principio de responsabilidad única")

print("\n=== CÓMO IDENTIFICAR VIOLACIONES DE OCP ===")
print("❌ Muchas declaraciones if/elif para diferentes casos")
print("❌ Modificar clases existentes para agregar funcionalidad")
print("❌ Código duplicado para casos similares")
print("❌ Difícil agregar nuevos tipos sin cambiar código base")
