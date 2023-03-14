print("CALCULADORA DE DOS ENTEROS: ")
 
class calculadora:
    def __init__(self, num1, num2):
        self.num1 = int(num1)
        self.num2 = int(num2)

    def sumar(self):
        suma = self.num1 + self.num2
        print("La suma de los valores es: ", suma)

    def restar(self):
        resta = self.num1 - self.num2
        print("La resta de los valores es: ", resta)

    def multiplicar(self):
        multiplicacion = self.num1 * self.num2
        print("La multiplicación de los valores es: ", multiplicacion)

    def dividir(self):
        division = self.num1 / self.num2
        print("La división de los valores es ", division)


num1 = input("Introduzca un primer número: ")
num2 = input("Introduzca un segundo número: ")

calculadora = calculadora(num1, num2)
calculadora.sumar()
calculadora.multiplicar()
calculadora.restar()
calculadora.dividir()