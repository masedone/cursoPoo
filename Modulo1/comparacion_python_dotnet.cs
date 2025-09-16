/* 
 * COMPARACIÓN: Python intro.py vs C# (.NET)
 * Traducción de todos los ejemplos de programación
 */

using System;
using System.Collections.Generic;
using System.Linq;

namespace ComparacionPythonDotNet
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== COMPARACIÓN PYTHON vs C# (.NET) ===\n");
            
            // 🔹 PROGRAMACIÓN IMPERATIVA
            Console.WriteLine("### 🔹 Programación Imperativa");
            Console.WriteLine("// Basada en dar instrucciones paso a paso.");
            Console.WriteLine("// El foco está en **cómo** se hace la tarea.");
            Console.WriteLine("// Ejemplos: C, C#, Java, Python (en estilo imperativo).\n");
            
            // Calcular la suma de una lista (imperativo)
            int[] numeros = {1, 2, 3, 4};
            int suma = 0;
            for (int i = 0; i < numeros.Length; i++)
            {
                suma += numeros[i];
            }
            Console.WriteLine($"Suma imperativa: {suma}");
            
            // 🔹 PROGRAMACIÓN DECLARATIVA
            Console.WriteLine("\n### 🔹 Programación Declarativa");
            Console.WriteLine("// Se centra en QUÉ queremos lograr, no en los pasos.");
            Console.WriteLine("// Ejemplos: SQL, LINQ, XAML");
            
            // En C#, equivalente declarativo con LINQ
            int[] numerosDeclarativos = {1, 2, 3, 4};
            int sumaDeclarativa = numerosDeclarativos.Sum(); // LINQ - declarativo
            Console.WriteLine($"Suma declarativa (LINQ): {sumaDeclarativa}");
            
            // 🔹 PROGRAMACIÓN FUNCIONAL
            Console.WriteLine("\n### 🔹 Programación Funcional");
            Console.WriteLine("// C# soporta programación funcional con LINQ y delegates");
            
            // Calcular suma (funcional con LINQ)
            int[] numerosFuncional = {1, 2, 3, 4};
            int sumaFuncional = numerosFuncional.Aggregate((a, b) => a + b);
            Console.WriteLine($"Suma funcional: {sumaFuncional}");
            
            // 🔹 PROGRAMACIÓN ORIENTADA A OBJETOS
            Console.WriteLine("\n### 🔹 Programación Orientada a Objetos");
            Console.WriteLine("// C# es fuertemente orientado a objetos");
            
            // Crear y usar objetos
            Coche miCoche = new Coche("Toyota", "Rojo");
            miCoche.Arrancar();
            
            Coche coche1 = new Coche("Toyota", "Rojo");
            Coche coche2 = new Coche("Ford", "Azul");
            
            coche1.Arrancar();
            coche2.Arrancar();
            
            // 🔹 ENCAPSULAMIENTO
            Console.WriteLine("\n### 🔹 Encapsulamiento");
            Console.WriteLine("// C# tiene verdadero encapsulamiento con private/public");
            
            CuentaBancaria cuenta = new CuentaBancaria("Ana", 1000);
            Console.WriteLine(cuenta.Titular); // Público
            // Console.WriteLine(cuenta.saldo); // ❌ Error de compilación - es private
            cuenta.Depositar(500);
            Console.WriteLine(cuenta.MostrarSaldo());
            
            // 🔹 GETTERS Y SETTERS (PROPERTIES)
            Console.WriteLine("\n### 🔹 Properties (Getters y Setters)");
            
            // Método tradicional
            CuentaConGetSet cuenta1 = new CuentaConGetSet("María", 500);
            Console.WriteLine($"Saldo inicial: {cuenta1.GetSaldo()}");
            cuenta1.SetSaldo(1000);
            Console.WriteLine($"Saldo después del setter: {cuenta1.GetSaldo()}");
            cuenta1.SetSaldo(-100); // Validación
            
            // Método con Properties (más elegante en C#)
            Console.WriteLine("\n=== EJEMPLO CON PROPERTIES (equivalente a @property) ===");
            CuentaConProperty cuenta2 = new CuentaConProperty("Juan", 800);
            Console.WriteLine($"Saldo inicial: {cuenta2.Saldo}"); // Property getter
            cuenta2.Saldo = 1200; // Property setter
            Console.WriteLine($"Saldo después de modificar: {cuenta2.Saldo}");
            cuenta2.Saldo = -50; // Validación automática
            
            Console.WriteLine("\n=== RESUMEN DE DIFERENCIAS ===");
            Console.WriteLine("Python: Dinámico, interpretado, duck typing");
            Console.WriteLine("C#:     Estático, compilado, strong typing");
            Console.WriteLine("Python: Encapsulamiento por convención (_ y __)");
            Console.WriteLine("C#:     Encapsulamiento real (private, protected, public)");
            Console.WriteLine("Python: @property para getters/setters");
            Console.WriteLine("C#:     Properties nativas del lenguaje");
        }
    }
    
    // 🔸 CLASE COCHE (equivalente a Python)
    public class Coche
    {
        // Campos privados (equivalente a self.marca, self.color en Python)
        private string marca;
        private string color;
        
        // Constructor (equivalente a __init__ en Python)
        public Coche(string marca, string color)
        {
            this.marca = marca;
            this.color = color;
        }
        
        // Método público (equivalente a def arrancar(self) en Python)
        public void Arrancar()
        {
            Console.WriteLine($"El {marca} arranca!");
        }
    }
    
    // 🔸 CLASE CUENTA BANCARIA CON ENCAPSULAMIENTO REAL
    public class CuentaBancaria
    {
        public string Titular { get; private set; } // Property de solo lectura
        private decimal saldo; // Campo privado REAL
        
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
    
    // 🔸 CLASE CON GET/SET TRADICIONAL
    public class CuentaConGetSet
    {
        private string titular;
        private decimal saldo;
        
        public CuentaConGetSet(string titular, decimal saldo)
        {
            this.titular = titular;
            this.saldo = saldo;
        }
        
        // GETTER tradicional
        public decimal GetSaldo()
        {
            return saldo;
        }
        
        // SETTER tradicional con validación
        public void SetSaldo(decimal nuevoSaldo)
        {
            if (nuevoSaldo >= 0)
            {
                saldo = nuevoSaldo;
            }
            else
            {
                Console.WriteLine("❌ El saldo no puede ser negativo");
            }
        }
        
        public void Depositar(decimal cantidad)
        {
            saldo += cantidad;
        }
    }
    
    // 🔸 CLASE CON PROPERTIES (equivalente a @property de Python)
    public class CuentaConProperty
    {
        private string titular;
        private decimal saldo;
        
        public CuentaConProperty(string titular, decimal saldo)
        {
            this.titular = titular;
            this.saldo = saldo;
        }
        
        // PROPERTY con getter y setter (equivalente a @property en Python)
        public decimal Saldo
        {
            get { return saldo; }                    // GETTER
            set                                      // SETTER
            {
                if (value >= 0)
                {
                    saldo = value;
                }
                else
                {
                    Console.WriteLine("❌ El saldo no puede ser negativo");
                }
            }
        }
        
        public void Depositar(decimal cantidad)
        {
            saldo += cantidad;
        }
    }
}

/*
 * TABLA COMPARATIVA DETALLADA:
 * 
 * | Aspecto              | Python                    | C# (.NET)                |
 * |----------------------|---------------------------|--------------------------|
 * | Tipado               | Dinámico                  | Estático                 |
 * | Compilación          | Interpretado              | Compilado                |
 * | Constructor          | __init__(self, ...)      | public Class(...)        |
 * | Métodos              | def metodo(self):         | public void Metodo()     |
 * | Atributos públicos   | self.atributo             | public string Atributo   |
 * | Atributos privados   | self.__atributo           | private string atributo  |
 * | Getters/Setters      | @property / @setter       | Properties { get; set; } |
 * | Herencia             | class Hijo(Padre):        | class Hijo : Padre       |
 * | Múltiple herencia    | ✅ Sí                     | ❌ No (interfaces sí)    |
 * | Duck typing          | ✅ Sí                     | ❌ No                    |
 * | Sobrecarga métodos   | ❌ No                     | ✅ Sí                    |
 * | Namespaces           | import modulo             | using Namespace;         |
 * | Manejo de memoria    | Garbage Collector         | Garbage Collector        |
 * | Performance          | Más lento                 | Más rápido               |
 * | Curva aprendizaje    | Más fácil                 | Más complejo             |
 * | Ecosistema           | Amplio (PyPI)             | Muy amplio (NuGet)       |
 * 
 */
