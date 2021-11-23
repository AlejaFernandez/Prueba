
arg1= [{'nombre': "John", 'apellido': "Doe"}, {'nombre': "Jane", 'apellido': None}, {'nombre': "Jose", 'apellido':"Doe"}] 
arg2= {'apellido': "Doe"}

def test (arg1, arg2):
    solucion = []
    for x in arg1:
        if x["apellido"] == arg2["apellido"]:
            solucion.append(x)
    return print(solucion)

test(arg1,arg2);

