### Objetivos del módulo
# Comprender los pilares de la POO.: Herencia, Polimorfismo, Abstracción, Composición, Interfaces.
# Diferenciar composición vs herencia.
# Aprender el rol de los constructores en la creacion de objetos.
# Practicar con ejemplos en **Python**.

##Constructores
#Los constructores son métodos especiales que inicializan un objeto al momento de su creación.
#En Python se utiliza __init__() y se ejecuta automáticamente al instanciar la clase.
#Ejemplo:
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    
p1 = Persona("Ana", 25)
p2=Persona("Juan", 30)
print(p1.presentarse())
print(p2.presentarse())


    



    