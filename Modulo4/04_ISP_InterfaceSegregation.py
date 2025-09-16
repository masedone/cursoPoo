## 🔹 PRINCIPIO SOLID 4: INTERFACE SEGREGATION PRINCIPLE (ISP)
# "Una clase no debe implementar interfaces que no necesita"

print("=== PRINCIPIO ISP - SEGREGACIÓN DE INTERFACES ===\n")

from abc import ABC, abstractmethod

# ❌ VIOLACIÓN DE ISP - Interface demasiado grande
print("❌ VIOLACIÓN DE ISP - Interface demasiado grande:")

class TrabajadorCompleto(ABC):
    """VIOLA ISP: Interface demasiado grande que fuerza implementaciones innecesarias"""
    
    @abstractmethod
    def programar(self):
        pass
    
    @abstractmethod
    def diseñar(self):
        pass
    
    @abstractmethod
    def testear(self):
        pass
    
    @abstractmethod
    def gestionar_proyecto(self):
        pass
    
    @abstractmethod
    def hacer_marketing(self):
        pass
    
    @abstractmethod
    def vender(self):
        pass
    
    @abstractmethod
    def dar_soporte_tecnico(self):
        pass

class ProgramadorJunior(TrabajadorCompleto):
    """PROBLEMA: Debe implementar métodos que no necesita"""
    
    def programar(self):
        return "💻 Programando en Python"
    
    def diseñar(self):
        # ❌ No hace diseño, pero debe implementar el método
        raise NotImplementedError("Un programador junior no hace diseño")
    
    def testear(self):
        return "🧪 Haciendo tests unitarios"
    
    def gestionar_proyecto(self):
        # ❌ No gestiona proyectos, pero debe implementar el método
        raise NotImplementedError("Un programador junior no gestiona proyectos")
    
    def hacer_marketing(self):
        # ❌ No hace marketing, pero debe implementar el método
        raise NotImplementedError("Un programador junior no hace marketing")
    
    def vender(self):
        # ❌ No vende, pero debe implementar el método
        raise NotImplementedError("Un programador junior no vende")
    
    def dar_soporte_tecnico(self):
        # ❌ No da soporte, pero debe implementar el método
        raise NotImplementedError("Un programador junior no da soporte técnico")

class Vendedor(TrabajadorCompleto):
    """PROBLEMA: Debe implementar métodos técnicos que no conoce"""
    
    def programar(self):
        # ❌ No programa, pero debe implementar el método
        raise NotImplementedError("Un vendedor no programa")
    
    def diseñar(self):
        # ❌ No diseña software, pero debe implementar el método
        raise NotImplementedError("Un vendedor no diseña software")
    
    def testear(self):
        # ❌ No testea código, pero debe implementar el método
        raise NotImplementedError("Un vendedor no testea código")
    
    def gestionar_proyecto(self):
        return "📋 Gestionando pipeline de ventas"
    
    def hacer_marketing(self):
        return "📢 Haciendo marketing de productos"
    
    def vender(self):
        return "💰 Vendiendo productos a clientes"
    
    def dar_soporte_tecnico(self):
        # ❌ No da soporte técnico, pero debe implementar el método
        raise NotImplementedError("Un vendedor no da soporte técnico")

# Uso problemático
print("Usando interfaces que violan ISP:")
programador = ProgramadorJunior()
vendedor = Vendedor()

print(f"Programador: {programador.programar()}")
print(f"Vendedor: {vendedor.vender()}")

# Problemas al intentar usar métodos no aplicables
try:
    print(f"Programador diseñando: {programador.diseñar()}")
except NotImplementedError as e:
    print(f"❌ Error: {e}")

try:
    print(f"Vendedor programando: {vendedor.programar()}")
except NotImplementedError as e:
    print(f"❌ Error: {e}")

print("\n" + "="*70 + "\n")

# ✅ APLICANDO ISP - Interfaces pequeñas y específicas
print("✅ APLICANDO ISP - Interfaces segregadas:")

# Interfaces pequeñas y específicas
class IProgramador(ABC):
    """Interface específica para programadores"""
    @abstractmethod
    def programar(self):
        pass
    
    @abstractmethod
    def hacer_debug(self):
        pass

class ITester(ABC):
    """Interface específica para testers"""
    @abstractmethod
    def testear(self):
        pass
    
    @abstractmethod
    def reportar_bugs(self):
        pass

class IDiseñador(ABC):
    """Interface específica para diseñadores"""
    @abstractmethod
    def diseñar(self):
        pass
    
    @abstractmethod
    def crear_mockups(self):
        pass

class IGestorProyecto(ABC):
    """Interface específica para gestores de proyecto"""
    @abstractmethod
    def gestionar_proyecto(self):
        pass
    
    @abstractmethod
    def coordinar_equipo(self):
        pass

class IMarketing(ABC):
    """Interface específica para marketing"""
    @abstractmethod
    def hacer_marketing(self):
        pass
    
    @abstractmethod
    def analizar_mercado(self):
        pass

class IVentas(ABC):
    """Interface específica para ventas"""
    @abstractmethod
    def vender(self):
        pass
    
    @abstractmethod
    def gestionar_clientes(self):
        pass

class ISoporteTecnico(ABC):
    """Interface específica para soporte técnico"""
    @abstractmethod
    def dar_soporte_tecnico(self):
        pass
    
    @abstractmethod
    def resolver_incidencias(self):
        pass

# Implementaciones que CUMPLEN ISP - Solo implementan lo que necesitan

class ProgramadorJuniorISP(IProgramador, ITester):
    """Solo implementa interfaces que realmente usa"""
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    # Métodos de IProgramador
    def programar(self):
        return f"💻 {self.nombre} está programando en Python"
    
    def hacer_debug(self):
        return f"🐛 {self.nombre} está depurando código"
    
    # Métodos de ITester
    def testear(self):
        return f"🧪 {self.nombre} está haciendo tests unitarios"
    
    def reportar_bugs(self):
        return f"📝 {self.nombre} está reportando bugs encontrados"

class ProgramadorSenior(IProgramador, ITester, IDiseñador, IGestorProyecto):
    """Implementa múltiples interfaces porque tiene más responsabilidades"""
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    # Métodos de IProgramador
    def programar(self):
        return f"💻 {self.nombre} está programando arquitectura compleja"
    
    def hacer_debug(self):
        return f"🐛 {self.nombre} está resolviendo bugs críticos"
    
    # Métodos de ITester
    def testear(self):
        return f"🧪 {self.nombre} está diseñando estrategias de testing"
    
    def reportar_bugs(self):
        return f"📝 {self.nombre} está analizando patrones de bugs"
    
    # Métodos de IDiseñador
    def diseñar(self):
        return f"🎨 {self.nombre} está diseñando la arquitectura del sistema"
    
    def crear_mockups(self):
        return f"📐 {self.nombre} está creando mockups técnicos"
    
    # Métodos de IGestorProyecto
    def gestionar_proyecto(self):
        return f"📋 {self.nombre} está gestionando el proyecto técnico"
    
    def coordinar_equipo(self):
        return f"👥 {self.nombre} está coordinando el equipo de desarrollo"

class VendedorISP(IVentas, IMarketing):
    """Solo implementa interfaces relacionadas con ventas"""
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    # Métodos de IVentas
    def vender(self):
        return f"💰 {self.nombre} está vendiendo productos"
    
    def gestionar_clientes(self):
        return f"👥 {self.nombre} está gestionando la cartera de clientes"
    
    # Métodos de IMarketing
    def hacer_marketing(self):
        return f"📢 {self.nombre} está haciendo campañas de marketing"
    
    def analizar_mercado(self):
        return f"📊 {self.nombre} está analizando el mercado objetivo"

class TecnicoSoporte(ISoporteTecnico, ITester):
    """Implementa soporte técnico y algo de testing"""
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    # Métodos de ISoporteTecnico
    def dar_soporte_tecnico(self):
        return f"🛠️ {self.nombre} está dando soporte técnico a clientes"
    
    def resolver_incidencias(self):
        return f"🔧 {self.nombre} está resolviendo incidencias técnicas"
    
    # Métodos de ITester
    def testear(self):
        return f"🧪 {self.nombre} está haciendo tests de regresión"
    
    def reportar_bugs(self):
        return f"📝 {self.nombre} está documentando problemas encontrados"

class DiseñadorUX(IDiseñador):
    """Solo implementa diseño, nada más"""
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def diseñar(self):
        return f"🎨 {self.nombre} está diseñando la experiencia de usuario"
    
    def crear_mockups(self):
        return f"📐 {self.nombre} está creando mockups de UI/UX"

# Funciones que trabajan con interfaces específicas
def hacer_programar(programadores):
    """Función que funciona con cualquier IProgramador"""
    print("🔄 Haciendo programar:")
    for prog in programadores:
        print(f"   {prog.programar()}")

def hacer_testear(testers):
    """Función que funciona con cualquier ITester"""
    print("🔄 Haciendo testear:")
    for tester in testers:
        print(f"   {tester.testear()}")

def hacer_vender(vendedores):
    """Función que funciona con cualquier IVentas"""
    print("🔄 Haciendo vender:")
    for vendedor in vendedores:
        print(f"   {vendedor.vender()}")

# Uso correcto que CUMPLE ISP
print("Usando interfaces que cumplen ISP:")

# Crear empleados especializados
prog_junior = ProgramadorJuniorISP("Ana")
prog_senior = ProgramadorSenior("Carlos")
vendedor_isp = VendedorISP("María")
soporte = TecnicoSoporte("Luis")
diseñador = DiseñadorUX("Elena")

# Cada uno implementa solo lo que necesita
print(f"👨‍💻 Programador Junior: {prog_junior.programar()}")
print(f"👨‍💻 Programador Senior: {prog_senior.diseñar()}")
print(f"👩‍💼 Vendedor: {vendedor_isp.vender()}")
print(f"🛠️ Soporte: {soporte.dar_soporte_tecnico()}")
print(f"🎨 Diseñador: {diseñador.diseñar()}")

print()

# Funciones polimórficas con interfaces específicas
programadores = [prog_junior, prog_senior]
hacer_programar(programadores)

print()

testers = [prog_junior, prog_senior, soporte]  # Todos implementan ITester
hacer_testear(testers)

print()

vendedores = [vendedor_isp]
hacer_vender(vendedores)

print("\n" + "="*70 + "\n")

# 🔸 EJEMPLO AVANZADO: Sistema de dispositivos
print("🔸 EJEMPLO AVANZADO: Dispositivos con interfaces segregadas")

class IImprimible(ABC):
    """Interface para dispositivos que pueden imprimir"""
    @abstractmethod
    def imprimir(self, documento):
        pass

class IEscaneable(ABC):
    """Interface para dispositivos que pueden escanear"""
    @abstractmethod
    def escanear(self):
        pass

class IFaxeable(ABC):
    """Interface para dispositivos que pueden enviar fax"""
    @abstractmethod
    def enviar_fax(self, numero, documento):
        pass

class ICopiable(ABC):
    """Interface para dispositivos que pueden copiar"""
    @abstractmethod
    def copiar(self, documento, cantidad):
        pass

# Implementaciones específicas que cumplen ISP

class ImpresoraSimple(IImprimible):
    """Solo puede imprimir - cumple ISP"""
    
    def __init__(self, modelo):
        self.modelo = modelo
    
    def imprimir(self, documento):
        return f"🖨️ {self.modelo} imprimiendo: {documento}"

class Escaner(IEscaneable):
    """Solo puede escanear - cumple ISP"""
    
    def __init__(self, modelo):
        self.modelo = modelo
    
    def escanear(self):
        return f"📄 {self.modelo} escaneando documento"

class ImpresoraMultifuncion(IImprimible, IEscaneable, ICopiable, IFaxeable):
    """Implementa múltiples interfaces porque realmente las necesita"""
    
    def __init__(self, modelo):
        self.modelo = modelo
    
    def imprimir(self, documento):
        return f"🖨️ {self.modelo} (multifunción) imprimiendo: {documento}"
    
    def escanear(self):
        return f"📄 {self.modelo} (multifunción) escaneando"
    
    def copiar(self, documento, cantidad):
        return f"📋 {self.modelo} (multifunción) copiando {documento} x{cantidad}"
    
    def enviar_fax(self, numero, documento):
        return f"📠 {self.modelo} (multifunción) enviando fax a {numero}: {documento}"

class ImpresoraLaser(IImprimible, ICopiable):
    """Solo implementa lo que realmente puede hacer"""
    
    def __init__(self, modelo):
        self.modelo = modelo
    
    def imprimir(self, documento):
        return f"🖨️ {self.modelo} (láser) imprimiendo rápido: {documento}"
    
    def copiar(self, documento, cantidad):
        return f"📋 {self.modelo} (láser) copiando rápido {documento} x{cantidad}"

# Funciones que trabajan con interfaces específicas
def procesar_impresion(dispositivos_impresion, documento):
    """Funciona con cualquier dispositivo que implemente IImprimible"""
    print(f"🔄 Imprimiendo '{documento}' en todos los dispositivos:")
    for dispositivo in dispositivos_impresion:
        print(f"   {dispositivo.imprimir(documento)}")

def procesar_escaneo(dispositivos_escaneo):
    """Funciona con cualquier dispositivo que implemente IEscaneable"""
    print("🔄 Escaneando en todos los dispositivos compatibles:")
    for dispositivo in dispositivos_escaneo:
        print(f"   {dispositivo.escanear()}")

# Uso del sistema de dispositivos
print("Sistema de dispositivos con ISP:")

# Crear dispositivos
impresora_simple = ImpresoraSimple("HP LaserJet")
escaner = Escaner("Canon Scanner")
multifuncion = ImpresoraMultifuncion("Brother MFC-L2750DW")
impresora_laser = ImpresoraLaser("Samsung ProXpress")

# Agrupar por capacidades
dispositivos_que_imprimen = [impresora_simple, multifuncion, impresora_laser]
dispositivos_que_escanean = [escaner, multifuncion]

# Usar funciones polimórficas
procesar_impresion(dispositivos_que_imprimen, "Documento importante.pdf")
print()
procesar_escaneo(dispositivos_que_escanean)

print()

# Usar funcionalidades específicas
print("🔄 Usando funcionalidades específicas:")
print(f"   {multifuncion.enviar_fax('555-1234', 'Contrato.pdf')}")
print(f"   {multifuncion.copiar('Documento.pdf', 5)}")
print(f"   {impresora_laser.copiar('Presentación.pdf', 10)}")

print("\n=== VENTAJAS DE APLICAR ISP ===")
print("✅ Clases más pequeñas y enfocadas")
print("✅ Menos dependencias innecesarias")
print("✅ Fácil testing - solo pruebas lo que implementas")
print("✅ Mejor flexibilidad y mantenibilidad")
print("✅ Principio de responsabilidad única reforzado")

print("\n=== CÓMO IDENTIFICAR VIOLACIONES DE ISP ===")
print("❌ Interfaces con muchos métodos no relacionados")
print("❌ Clases que implementan métodos lanzando excepciones")
print("❌ Clases que implementan métodos vacíos o con pass")
print("❌ Necesidad de verificar capacidades antes de usar métodos")
print("❌ Interfaces que cambian frecuentemente")

print("\n=== ESTRATEGIAS PARA APLICAR ISP ===")
print("🔧 Dividir interfaces grandes en interfaces específicas")
print("🔧 Agrupar métodos por funcionalidad relacionada")
print("🔧 Usar composición de interfaces cuando sea necesario")
print("🔧 Crear interfaces cohesivas y con propósito único")
