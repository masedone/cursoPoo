## 🔹 EJEMPLO 1: NOMBRES CLAROS Y AUTOEXPLICATIVOS
# Comparación entre nombres confusos y nombres descriptivos

print("=== NOMBRES CLAROS Y AUTOEXPLICATIVOS ===\n")

# ❌ MALA PRÁCTICA - Nombres confusos
print("❌ MALA PRÁCTICA - Nombres confusos:")

class P:                    # ¿Qué es P?
    def __init__(self, n, p):
        self.n = n          # ¿Qué es n?
        self.p = p          # ¿Qué es p?
    
    def f(self, x):         # ¿Qué hace f?
        return x * 1.21     # ¿Por qué 1.21?
    
    def g(self):            # ¿Qué hace g?
        if self.p < 10:
            return True
        return False

# Ejemplo de uso (confuso):
p = P("Laptop", 500)
print(f"Resultado de f(100): {p.f(100)}")  # ¿Qué está calculando?
print(f"Resultado de g(): {p.g()}")        # ¿Qué significa True/False?

print("\n" + "="*50 + "\n")

# ✅ BUENA PRÁCTICA - Nombres descriptivos
print("✅ BUENA PRÁCTICA - Nombres descriptivos:")

class Producto:
    IVA_PORCENTAJE = 1.21   # Constante clara
    
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base
    
    def calcular_precio_con_iva(self, precio_sin_iva):
        """Calcula el precio final incluyendo el IVA del 21%"""
        return precio_sin_iva * self.IVA_PORCENTAJE
    
    def es_producto_barato(self):
        """Determina si el producto cuesta menos de 10€"""
        return self.precio_base < 10
    
    def obtener_resumen(self):
        """Devuelve un resumen completo del producto"""
        precio_final = self.calcular_precio_con_iva(self.precio_base)
        categoria = "Barato" if self.es_producto_barato() else "Caro"
        return f"{self.nombre}: {precio_final:.2f}€ ({categoria})"
    
    def aplicar_descuento(self, porcentaje_descuento):
        """Aplica un descuento al precio base"""
        descuento = self.precio_base * (porcentaje_descuento / 100)
        precio_con_descuento = self.precio_base - descuento
        return precio_con_descuento

# Ejemplo de uso (claro):
laptop = Producto("Laptop Gaming", 500)
telefono = Producto("Smartphone", 8)

print(laptop.obtener_resumen())
print(telefono.obtener_resumen())
print(f"Precio con IVA de 100€: {laptop.calcular_precio_con_iva(100):.2f}€")
print(f"Laptop con 10% descuento: {laptop.aplicar_descuento(10):.2f}€")

print("\n" + "="*50 + "\n")

# 🔸 MÁS EJEMPLOS DE NOMBRES CLAROS
print("🔸 MÁS EJEMPLOS DE NOMBRES CLAROS:")

# ❌ Nombres confusos
def calc(x, y, z):
    return x + y * z

# ✅ Nombres descriptivos  
def calcular_precio_total(precio_base, cantidad, impuesto_porcentaje):
    """Calcula el precio total incluyendo impuestos"""
    return precio_base + (cantidad * impuesto_porcentaje)

# Comparación
resultado_confuso = calc(100, 5, 0.21)
resultado_claro = calcular_precio_total(100, 5, 0.21)

print(f"calc(100, 5, 0.21) = {resultado_confuso}")  # ¿Qué significa?
print(f"calcular_precio_total(100, 5, 0.21) = {resultado_claro}")  # ¡Claro!

print("\n=== VENTAJAS DE NOMBRES CLAROS ===")
print("✅ Código autodocumentado")
print("✅ Fácil de entender sin comentarios")
print("✅ Menos errores de programación")
print("✅ Mantenimiento más sencillo")
print("✅ Colaboración más eficiente")

print("\n=== REGLAS PARA NOMBRES CLAROS ===")
print("🔸 Usa nombres completos, no abreviaciones")
print("🔸 Describe QUÉ hace, no CÓMO lo hace")
print("🔸 Usa verbos para funciones: calcular, obtener, verificar")
print("🔸 Usa sustantivos para clases: Producto, Usuario, Pedido")
print("🔸 Sé específico: precio_con_iva vs precio")
print("🔸 Evita números mágicos: usa constantes con nombres")
