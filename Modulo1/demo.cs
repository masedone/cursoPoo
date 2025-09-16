#!/usr/bin/env dotnet-script
#r "nuget: System.Linq, 4.3.0"

using System;
using System.Linq;

Console.WriteLine("=== COMPARACIÓN PYTHON vs C# (.NET) ===\n");

// 🔹 PROGRAMACIÓN IMPERATIVA
Console.WriteLine("### 🔹 Programación Imperativa");
int[] numeros = {1, 2, 3, 4};
int suma = 0;
for (int i = 0; i < numeros.Length; i++)
{
    suma += numeros[i];
}
Console.WriteLine($"Suma imperativa: {suma}");

// 🔹 PROGRAMACIÓN DECLARATIVA
Console.WriteLine("\n### 🔹 Programación Declarativa");
int sumaDeclarativa = numeros.Sum(); // LINQ - declarativo
Console.WriteLine($"Suma declarativa (LINQ): {sumaDeclarativa}");

// 🔹 PROGRAMACIÓN FUNCIONAL
Console.WriteLine("\n### 🔹 Programación Funcional");
int sumaFuncional = numeros.Aggregate((a, b) => a + b);
Console.WriteLine($"Suma funcional: {sumaFuncional}");

// 🔹 PROGRAMACIÓN ORIENTADA A OBJETOS
Console.WriteLine("\n### 🔹 Programación Orientada a Objetos");

var miCoche = new Coche("Toyota", "Rojo");
miCoche.Arrancar();

var coche1 = new Coche("Toyota", "Rojo");
var coche2 = new Coche("Ford", "Azul");

coche1.Arrancar();
coche2.Arrancar();

// 🔹 ENCAPSULAMIENTO
Console.WriteLine("\n### 🔹 Encapsulamiento");
var cuenta = new CuentaBancaria("Ana", 1000);
Console.WriteLine(cuenta.Titular); // Público
cuenta.Depositar(500);
Console.WriteLine(cuenta.MostrarSaldo());

// 🔹 PROPERTIES
Console.WriteLine("\n### 🔹 Properties (Getters y Setters)");
var cuenta2 = new CuentaConProperty("Juan", 800);
Console.WriteLine($"Saldo inicial: {cuenta2.Saldo}");
cuenta2.Saldo = 1200;
Console.WriteLine($"Saldo después de modificar: {cuenta2.Saldo}");
cuenta2.Saldo = -50; // Validación automática

Console.WriteLine("\n=== RESUMEN DE DIFERENCIAS ===");
Console.WriteLine("Python: Dinámico, interpretado, duck typing");
Console.WriteLine("C#:     Estático, compilado, strong typing");
Console.WriteLine("Python: Encapsulamiento por convención (_ y __)");
Console.WriteLine("C#:     Encapsulamiento real (private, protected, public)");

// CLASES
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

public class CuentaBancaria
{
    public string Titular { get; private set; }
    private decimal saldo;
    
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

public class CuentaConProperty
{
    private string titular;
    private decimal saldo;
    
    public CuentaConProperty(string titular, decimal saldo)
    {
        this.titular = titular;
        this.saldo = saldo;
    }
    
    public decimal Saldo
    {
        get { return saldo; }
        set 
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
}
