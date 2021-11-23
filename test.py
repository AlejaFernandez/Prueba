arg1= [{'nombre': "John", 'apellido': "Doe"}, {'nombre': "Jane", 'apellido': None}, {'nombre': "Jose", 'apellido':"Doe"}] 
arg2= {'apellido': "Doe"}

propArg2 = list(arg2.keys())

def test (arg1, arg2):
    solucion = []
    for x in arg1:
        if x[propArg2[0]] == arg2[propArg2[0]]:
            solucion.append(x)
    return print(solucion)

test(arg1,arg2);

