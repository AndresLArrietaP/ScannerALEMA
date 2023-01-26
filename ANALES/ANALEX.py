import re

file = open("/Users/acer/Pictures/PYTHON/datux/ScannerALEMA/TESTEOS/codigo1.txt")

regex = re.compile(r'[a-z][a-zA-Z0-9_]+')
opl = re.compile(r'(\^|\v|\~)')
opa = re.compile(r'(\+|\-|\/|\@|\$|\-$-|\#)')

oplogicos = {'^':'Lógico “Y”' , 'v':'Lógico “Y”' , '~':'Negaciòn'}
oplogicos_key = oplogicos.keys()

oparitmeticos = {'+':'Suma' , '-':'Resta' , '/':'Division' , '@':'Multiplicacion' ,'$':'Potencia' ,'-$-':'Raiz' ,'#':'Residuo'}
oparitmeticos_key = oparitmeticos.keys()

oprelacion = {'==':'Igual a' , '>':'Mayor que' , '<':'Menor que' , '>=':'Mayor igual que' ,'<=':'Menor igual que'}
oprelacion_key = oprelacion.keys()

tipodato = {'numb' : 'Entero', 'numbdec': 'Decimal' , 'letter' : 'Caracter', 'words' : 'Cadena','clever' : 'Lógico' }
tipodato_key = tipodato.keys()

simbpuntuacion = { '*' : 'Fin de instruccion', ',' : 'coma' }
simbpuntuacion_key = simbpuntuacion.keys()

preservadas = { 'with' : 'De mètodo','of' : 'De clase','craft' : 'Objeto','for' : 'Bucle','work' : 'Repetitivo1','check' : 'Repetitivo1','yes' : 'Condicional1','noty' : 'Condicional2','writing' : 'Escritura','reading' : 'Lectura', 'mucuck' : 'Constante', 'ente' : 'Clase' ,'arqui' : 'Mètodo','ctr' : 'Constructor'}
preservadas_key = preservadas.keys()

identifier = { }
identifier_key = identifier.keys()

dataFlag = False

a=file.read()

count=0
program = a.split("\n")
for line in program:
    count = count + 1
    print("line#" , count, "\n" , line)

    tokens=line.split(' ')
    print("Tokens are " , tokens)
    print("Line#", count, "properties \n")
    for token in tokens:
        if opl.match(token):
            print("Op. lògico ")
        elif opa.match(token):
            print("Op. aritmètico ")
        elif regex.match(token):
            #identifier.update({"ID": token})
            print ("Identificador " )
        else:
            print ("No encontrado " )

        
    
    dataFlag=False
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _") 