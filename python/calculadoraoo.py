class Calculadora:
    primer_nro = None
    segundo_nro = None
    resultado = 0.0
    historial = None

    def __init__(self,p,s):
        self.primer_nro = p
        self.segundo_nro = s
        self.resultado = 0.0
        self.historial = []

    def set_numeros(self,p,s):
        self.primer_nro= p
        self.segundo_nro=s

    def get_suma(self):
        self.resultado= self.primer_nro + self.segundo_nro
        texto = str(self.primer_nro) + "+" + str(self.segundo_nro) + "=" + str(self.resultado)
        self.historial.append(texto)
        return self.resultado
    
    def get_resta(self):
        self.resultado = self.primer_nro - self.segundo_nro
        texto = str(self.primer_nro) + "-" + str(self.segundo_nro) + "=" + str(self.resultado)
        self.historial.append(texto)
        return self.resultado
    
    def get_mult(self):
        self.resultado = self.primer_nro * self.segundo_nro
        texto = str(self.primer_nro) + "*" + str(self.segundo_nro) + "=" + str(self.resultado)
        self.historial.append(texto)
        return self.resultado
    
    def get_div(self):
        if (self.segundo_nro != 0):
            self.resultado = self.primer_nro / self.segundo_nro
            texto = str(self.primer_nro) + "/" + str(self.segundo_nro) + "=" + str(self.resultado)
            self.historial.append(texto)
            return self.resultado  
        else:
            print("No se puede dividir entre 0")

    def get_exponente(self):
        self.resultado = self.primer_nro ** self.segundo_nro
        texto = str(self.primer_nro) + "^" + str(self.segundo_nro) + "=" + str(self.resultado)
        self.historial.append(texto)
        return self.resultado

    def get_historial(self):
        return self.historial
    
if __name__ == "__main__":
    calc= Calculadora (30,30)
    print(calc.get_suma())
    calc.set_numeros(15,30)
    print(calc.get_suma())
    calc.set_numeros(2,2)
    print(calc.get_suma())
    calc.set_numeros(10,5)
    print(calc.get_resta())
    calc.set_numeros(3,5)
    print(calc.get_mult())
    calc.set_numeros(2,3)
    print(calc.get_exponente())
    calc.set_numeros(30,5)
    print(calc.get_div())
    print(calc.get_historial())