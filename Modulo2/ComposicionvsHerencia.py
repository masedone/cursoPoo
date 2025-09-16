##Composicion vs Herencia
#La composicion consiste en que una clase tenga un objeto de otra clase.
#Ejemplo:
class Motor:
    def __init__(self):
        self.encender()
        
    def encender(self):
        return "Motor encendido"
        
class Coche:
    def __init__(self):
        self.motor = Motor()
        
    def arrancar(self):
        return self.motor.encender() + " y el coche arranca"
        
coche = Coche()
print(coche.arrancar())

