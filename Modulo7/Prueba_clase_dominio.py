#Pruebas para Clases de Dominio
class Pedido:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def total(self):
        return sum(self.productos)
    
