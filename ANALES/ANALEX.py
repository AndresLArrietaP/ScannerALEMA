import re

#Cabro el que lo lea

file = open("/Users/acer/Pictures/PYTHON/datux/ScannerALEMA/TESTEOS/codigo1.txt")

oplogicos = {'^':'Lógico “Y”' , 'v':'Lógico “Y”' , '~':'Negaciòn'}
oplogicos_key = oplogicos.keys()

oparitmeticos = {'+':'Suma' , '-':'Resta' , '/':'Division' , '@':'Multiplicacion' ,'$':'Potencia' ,'-$-':'Raiz' ,'#':'Residuo'}
oparitmeticos_key = oparitmeticos.keys()

oprelacion = {'==':'Igual a' , '>':'Mayor que' , '<':'Menor que' , '>=':'Mayor igual que' ,'<=':'Menor igual que'}
oprelacion_key = oprelacion.keys()

tipodato = {'numb' : 'Entero', 'numbdec': 'Decimal' , 'letter' : 'caracter', 'words' : 'cadena','clever' : 'lógico' }
tipodato_key = tipodato.keys()

simbpuntuacion = { '*' : 'Fin de instruccion', ',' : 'coma' }
simbpuntuacion_key = simbpuntuacion.keys()

preservadas = { 'mucuck' : 'Constante', 'ente' : 'Clase' ,'arqui' : 'Mètodo','ctr' : 'Constructor'}
preservadas_key = preservadas.keys()

identifier = { 'a' : 'id', 'b' : 'id', 'c' : 'id' , 'd' : 'id' }
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
        if token in operators_key:
            print("operator is ", operators[token])
        if token in data_type_key:
            print("datatype is", data_type[token])
        if token in punctuation_symbol_key:
            print (token, "Punctuation symbol is" , punctuation_symbol[token])
        if token in identifier_key:
            print (token, "Identifier is" , identifier[token])

           
    dataFlag=False
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _") 