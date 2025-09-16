## 🔹 INTERFACES - Ejemplo Simple
# Interface = Contrato que define QUÉ métodos debe tener una clase

from abc import ABC, abstractmethod

print("=== INTERFACES SIMPLES ===\n")

# 🔸 INTERFACE 1: Reproducible
class IReproducible(ABC):
    """Todo lo que se puede reproducir debe tener estos métodos"""
    
    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def pause(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

# 🔸 INTERFACE 2: Guardable
class IGuardable(ABC):
    """Todo lo que se puede guardar debe tener estos métodos"""
    
    @abstractmethod
    def guardar(self):
        pass
    
    @abstractmethod
    def cargar(self):
        pass

# 🔸 IMPLEMENTACIONES
class ReproductorMusica(IReproducible):
    def __init__(self, cancion):
        self.cancion = cancion
    
    def play(self):
        return f"🎵 Reproduciendo: {self.cancion}"
    
    def pause(self):
        return f"⏸️ Pausando: {self.cancion}"
    
    def stop(self):
        return f"⏹️ Deteniendo: {self.cancion}"

class ReproductorVideo(IReproducible):
    def __init__(self, video):
        self.video = video
    
    def play(self):
        return f"🎬 Reproduciendo video: {self.video}"
    
    def pause(self):
        return f"⏸️ Pausando video: {self.video}"
    
    def stop(self):
        return f"⏹️ Deteniendo video: {self.video}"

class Documento(IGuardable):
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenido = ""
    
    def guardar(self):
        return f"💾 Guardando documento: {self.nombre}"
    
    def cargar(self):
        return f"📂 Cargando documento: {self.nombre}"

# 🔸 CLASE QUE IMPLEMENTA MÚLTIPLES INTERFACES
class EditorVideo(IReproducible, IGuardable):
    def __init__(self, proyecto):
        self.proyecto = proyecto
    
    # Métodos de IReproducible
    def play(self):
        return f"🎬 Reproduciendo proyecto: {self.proyecto}"
    
    def pause(self):
        return f"⏸️ Pausando edición: {self.proyecto}"
    
    def stop(self):
        return f"⏹️ Deteniendo edición: {self.proyecto}"
    
    # Métodos de IGuardable
    def guardar(self):
        return f"💾 Guardando proyecto: {self.proyecto}"
    
    def cargar(self):
        return f"📂 Cargando proyecto: {self.proyecto}"

# 🔸 USANDO LAS INTERFACES
print("=== REPRODUCTORES ===")
musica = ReproductorMusica("Bohemian Rhapsody")
video = ReproductorVideo("Matrix.mp4")

print(musica.play())
print(musica.pause())
print(musica.stop())
print()

print(video.play())
print(video.pause())
print(video.stop())
print()

print("=== DOCUMENTO ===")
doc = Documento("mi_archivo.txt")
print(doc.guardar())
print(doc.cargar())
print()

print("=== EDITOR (MÚLTIPLES INTERFACES) ===")
editor = EditorVideo("Mi_Pelicula.mp4")
print(editor.play())
print(editor.guardar())
print(editor.pause())
print(editor.cargar())
print()

# 🔸 POLIMORFISMO CON INTERFACES
print("=== POLIMORFISMO ===")
print("Todos los reproductores:")
reproductores = [musica, video, editor]
for reproductor in reproductores:
    print(f"- {reproductor.play()}")

print("\nTodos los guardables:")
guardables = [doc, editor]
for guardable in guardables:
    print(f"- {guardable.guardar()}")

print("\n=== RESUMEN SIMPLE ===")
print("🔸 INTERFACE = Lista de métodos obligatorios")
print("🔸 Las clases DEBEN implementar todos los métodos")
print("🔸 Permite polimorfismo: misma función, diferentes objetos")
print("🔸 Una clase puede implementar múltiples interfaces")
print("🔸 Ejemplo: IReproducible, IGuardable, IConectable, etc.")
