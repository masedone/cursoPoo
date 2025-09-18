# Test_clase_dominio.py
# para este proyecto de test necesitamos instalar pytest
# pip install pytest
# para ejecutar los tests necesitamos ejecutar el comando pytest
# pytest
# si queremos ejecutar los tests de un archivo en especifico podemos ejecutar el comando pytest Test_clase_dominio.py
from Prueba_clase_dominio import Pedido
    
#test unitario
def test_total_pedido():
    pedido = Pedido()
    pedido.agregar_producto(10)
    pedido.agregar_producto(20)
    assert pedido.total() == 30
