# 🔥 COMPARACIÓN: Python vs C# (.NET)

Comparación detallada de todos los ejemplos del archivo `intro.py` traducidos a C# (.NET)

## 🔹 **1. PROGRAMACIÓN IMPERATIVA**

### 🐍 Python
```python
# Calcular la suma de una lista (imperativo)
numeros = [1, 2, 3, 4]
suma = 0
for n in numeros:
    suma += n
print(suma)
```

### 🔷 C# (.NET)
```csharp
// Calcular la suma de una lista (imperativo)
int[] numeros = {1, 2, 3, 4};
int suma = 0;
for (int i = 0; i < numeros.Length; i++)
{
    suma += numeros[i];
}
Console.WriteLine(suma);
```

---

## 🔹 **2. PROGRAMACIÓN DECLARATIVA**

### 🐍 Python
```python
# Declarativo con función built-in
numeros = [1, 2, 3, 4]
suma_declarativa = sum(numeros)  # QUÉ queremos: la suma
print(f"Suma declarativa: {suma_declarativa}")
```

### 🔷 C# (.NET)
```csharp
// Declarativo con LINQ
int[] numeros = {1, 2, 3, 4};
int sumaDeclarativa = numeros.Sum(); // LINQ - declarativo
Console.WriteLine($"Suma declarativa: {sumaDeclarativa}");
```

---

## 🔹 **3. PROGRAMACIÓN FUNCIONAL**

### 🐍 Python
```python
# Funcional con función built-in
numeros = [1, 2, 3, 4]
print(sum(numeros))
```

### 🔷 C# (.NET)
```csharp
// Funcional con LINQ y lambda
int[] numeros = {1, 2, 3, 4};
int sumaFuncional = numeros.Aggregate((a, b) => a + b);
Console.WriteLine(sumaFuncional);
```

---

## 🔹 **4. PROGRAMACIÓN ORIENTADA A OBJETOS**

### 🐍 Python - Clase Coche
```python
class Coche:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def arrancar(self):
        print(f"El {self.marca} arranca!")

mi_coche = Coche("Toyota", "Rojo")
mi_coche.arrancar()
```

### 🔷 C# (.NET) - Clase Coche
```csharp
public class Coche
{
    private string marca;
    private string color;
    
    public Coche(string marca, string color)
    {
        this.marca = marca;
        this.color = color;
    }
    
    public void Arrancar()
    {
        Console.WriteLine($"El {marca} arranca!");
    }
}

Coche miCoche = new Coche("Toyota", "Rojo");
miCoche.Arrancar();
```

---

## 🔹 **5. ENCAPSULAMIENTO**

### 🐍 Python - "Privado" por convención
```python
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo   # "privado" (name mangling)

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def mostrar_saldo(self):
        return f"Saldo de {self.titular}: {self.__saldo}€"

cuenta = CuentaBancaria("Ana", 1000)
print(cuenta.titular)  # ✅ Público
# print(cuenta.__saldo)  # ❌ AttributeError (pero no real)
print(cuenta._CuentaBancaria__saldo)  # ✅ Accesible con name mangling
```

### 🔷 C# (.NET) - Privado REAL
```csharp
public class CuentaBancaria
{
    public string Titular { get; private set; }  // Público para lectura
    private decimal saldo;                        // PRIVADO REAL

    public CuentaBancaria(string titular, decimal saldo)
    {
        Titular = titular;
        this.saldo = saldo;
    }

    public void Depositar(decimal cantidad)
    {
        saldo += cantidad;
    }

    public string MostrarSaldo()
    {
        return $"Saldo de {Titular}: {saldo}€";
    }
}

CuentaBancaria cuenta = new CuentaBancaria("Ana", 1000);
Console.WriteLine(cuenta.Titular);  // ✅ Público
// Console.WriteLine(cuenta.saldo);  // ❌ ERROR DE COMPILACIÓN - es private
```

---

## 🔹 **6. GETTERS Y SETTERS**

### 🐍 Python - Método tradicional
```python
class CuentaConGetSet:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    
    def get_saldo(self):        # GETTER
        return self.__saldo
    
    def set_saldo(self, nuevo_saldo):  # SETTER
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            print("❌ El saldo no puede ser negativo")

cuenta = CuentaConGetSet("María", 500)
print(cuenta.get_saldo())  # Usar getter
cuenta.set_saldo(1000)     # Usar setter
```

### 🔷 C# (.NET) - Método tradicional
```csharp
public class CuentaConGetSet
{
    private string titular;
    private decimal saldo;
    
    public CuentaConGetSet(string titular, decimal saldo)
    {
        this.titular = titular;
        this.saldo = saldo;
    }
    
    public decimal GetSaldo()  // GETTER
    {
        return saldo;
    }
    
    public void SetSaldo(decimal nuevoSaldo)  // SETTER
    {
        if (nuevoSaldo >= 0)
            saldo = nuevoSaldo;
        else
            Console.WriteLine("❌ El saldo no puede ser negativo");
    }
}

CuentaConGetSet cuenta = new CuentaConGetSet("María", 500);
Console.WriteLine(cuenta.GetSaldo());  // Usar getter
cuenta.SetSaldo(1000);                 // Usar setter
```

---

## 🔹 **7. PROPERTIES (Equivalente a @property)**

### 🐍 Python - @property
```python
class CuentaConProperty:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    
    @property
    def saldo(self):  # GETTER
        return self.__saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):  # SETTER
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            print("❌ El saldo no puede ser negativo")

cuenta = CuentaConProperty("Juan", 800)
print(cuenta.saldo)    # Como atributo público (usa getter)
cuenta.saldo = 1200    # Como atributo público (usa setter)
```

### 🔷 C# (.NET) - Properties nativas
```csharp
public class CuentaConProperty
{
    private string titular;
    private decimal saldo;
    
    public CuentaConProperty(string titular, decimal saldo)
    {
        this.titular = titular;
        this.saldo = saldo;
    }
    
    public decimal Saldo  // PROPERTY
    {
        get { return saldo; }         // GETTER
        set                           // SETTER
        {
            if (value >= 0)
                saldo = value;
            else
                Console.WriteLine("❌ El saldo no puede ser negativo");
        }
    }
}

CuentaConProperty cuenta = new CuentaConProperty("Juan", 800);
Console.WriteLine(cuenta.Saldo);  // Como atributo público (usa getter)
cuenta.Saldo = 1200;              // Como atributo público (usa setter)
```

---

## 📊 **TABLA COMPARATIVA COMPLETA**

| **Aspecto** | **🐍 Python** | **🔷 C# (.NET)** |
|-------------|---------------|------------------|
| **Tipado** | Dinámico | Estático |
| **Compilación** | Interpretado | Compilado |
| **Performance** | Más lento | Más rápido |
| **Constructor** | `__init__(self, ...)` | `public Class(...)` |
| **Métodos** | `def metodo(self):` | `public void Metodo()` |
| **Atributos públicos** | `self.atributo` | `public string Atributo` |
| **Atributos privados** | `self.__atributo` (convención) | `private string atributo` (real) |
| **Getters/Setters** | `@property` / `@setter` | `Properties { get; set; }` |
| **Herencia** | `class Hijo(Padre):` | `class Hijo : Padre` |
| **Múltiple herencia** | ✅ Sí | ❌ No (interfaces sí) |
| **Duck typing** | ✅ Sí | ❌ No |
| **Sobrecarga métodos** | ❌ No | ✅ Sí |
| **Namespaces** | `import modulo` | `using Namespace;` |
| **Manejo memoria** | Garbage Collector | Garbage Collector |
| **Curva aprendizaje** | 🟢 Más fácil | 🟡 Más complejo |
| **Ecosistema** | 🟢 Amplio (PyPI) | 🟢 Muy amplio (NuGet) |

---

## 🎯 **CONCLUSIONES**

### **🐍 Python es mejor para:**
- ✅ Prototipado rápido
- ✅ Data Science y ML
- ✅ Scripting y automatización
- ✅ Aprendizaje de programación
- ✅ Desarrollo web rápido

### **🔷 C# (.NET) es mejor para:**
- ✅ Aplicaciones empresariales
- ✅ Aplicaciones de alto rendimiento
- ✅ Aplicaciones web escalables
- ✅ Aplicaciones de escritorio
- ✅ Juegos (Unity)

### **🤝 Ambos son excelentes para:**
- ✅ Programación orientada a objetos
- ✅ Desarrollo web
- ✅ APIs y microservicios
- ✅ Aplicaciones multiplataforma

---

## 🚀 **PRÓXIMOS PASOS**

1. **Practica ambos lenguajes** con los mismos ejercicios
2. **Elige según el proyecto:** Python para rapidez, C# para robustez
3. **Aprende los patrones** comunes en ambos ecosistemas
4. **Experimenta** con frameworks: Django/Flask vs ASP.NET Core

**¡La POO es universal, los lenguajes son solo herramientas!** 🛠️
