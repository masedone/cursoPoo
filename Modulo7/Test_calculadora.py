# Test_calculadora.py
# para este proyecto de test necesitamos instalar pytest
# pip install pytest
# para ejecutar los tests necesitamos ejecutar el comando pytest
# pytest
# si queremos ejecutar los tests de un archivo en especifico podemos ejecutar el comando pytest <nombre_del_archivo>
from Calculadora import sumar

def test_sumar():
    assert sumar(2, 3) == 5