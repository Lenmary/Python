#suma, restar, multiplicar, dividir, raíz cuadrada y exponente

def sumar(x, y):
    return x + y

def sumador(*args):
    resul=0
    for x in args:
        resul+=x
    return resul

def restar(x, y):
    return x - y

def multiplicar (x, y):
    return x * y

def dividir(x, y):
    if (y != 0): 
        return x/y
    else:
        return "No se puede dividir entre cero"
    
def raíz (x, y=2):
    return ((x)**0.5)

def exponente (x,y):
    return x**y
    
print(sumar(20,40))
print 
print (restar(40,20))
print (multiplicar(2,2))
print (dividir(4,0))
print (raíz(4))
print (exponente(3,2))

print(sumador(12,45,78,98,65,32))

