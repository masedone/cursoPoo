# Paso 1: test (rojo)
def test_es_par():
    assert es_par(4) == True
    assert es_par(5) == False

# Paso 2: implementación
def es_par(n):
    return n % 2 == 0
