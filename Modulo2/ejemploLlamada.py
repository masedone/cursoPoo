
# Importamos las clases y funciones que necesitamos
from 2Herencia import Vehiculo, Gato, hacer_hablar, Coche, Bicicleta

# Ahora sí podemos usar la función hacer_hablar
print("=== USANDO IMPORTACIONES ===")
hacer_hablar(Gato("Luna"))

# También podemos usar los vehículos
print("\n=== USANDO VEHÍCULOS IMPORTADOS ===")
mi_coche = Coche("Honda")
mi_bici = Bicicleta("Giant")

print(mi_coche.acelerar())
print(mi_bici.acelerar())