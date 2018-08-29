data = []

class Prestamo:
    valorPrestamo = 0
    numeroCuotaPrestamo = 0

    def __init__(self, valorPrestamo, numeroCuotaPrestamo):
        self.valorPrestamo = valorPrestamo
        self.numeroCuotaPrestamo = numeroCuotaPrestamo

    def crearPrestamo(self, posicion):
        prestamo = {
            'valorPrestamo': self.valorPrestamo,
            'numeroCuotaPrestamo': self.numeroCuotaPrestamo
        }

        lista = list(data[posicion]['prestamos'])
        lista.append(prestamo)
        data[posicion]['prestamos'] = lista

        listaSegunda = int(len(lista) - 1)

        valorCuota = int(self.valorPrestamo) / int(self.numeroCuotaPrestamo)

        cuota = Cuotas(valorCuota, listaSegunda, False)
        cuota.crearCuota(posicion, int(self.numeroCuotaPrestamo))



class Cuotas:
    valorCuota = 0
    idPrestamo = 0
    estado = False

    def __init__(self, valorCuota, idPrestamo, estado):
        self.valorCuota = valorCuota
        self.idPrestamo = idPrestamo
        self.estado = False

    def crearCuota(self, posicion, numeroCuota):
        cuota = {
            'valorCuota': self.valorCuota,
            'idPrestamo': self.idPrestamo,
            'estado': self.estado
        }

        lista = list(data[posicion]['cuotas'])

        for c in range(1, (numeroCuota+1):
            lista.append(cuota)

        data[posicion]['cuotas']= lista

class Usuario(Prestamo, Cuotas):
    cedula = 0
    nombre = ""
    edad = 0
    correo = ""

    def __init__(self, cedula, nombre, edad, correo, valorPrestamo, numeroCuotaPrestamo, valorCuota, idPrestamo, estado):
        Prestamo.__init__(self, valorPrestamo, numeroCuotaPrestamo)
        Cuotas.__init__(self, valorCuota, idPrestamo, estado)
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def crearUsuario(self):
        usuario = {
            'cedula': self.cedula,
            'nombre': self.nombre,
            'edad': self.edad,
            'correo': self.correo
        }
        data.append({'usuarios':[usuario],'prestamos':[],'cuotas':[]})

def pagarCuota(posicion):
    posp = 0
    for p in list(data[posicion]['prestamos']):
        print("(ced: {}) El valor del prestamo es: {}".format(posp,p['valor']))
        posp = posp + 1

    idp = input('digite el id del prestamo')

    lista =  list(data[posicion]['cuotas'])
    for c in lista:
        if c['idPrestamo'] == int(idp):
            c['estado'] = True
            break
    data[posicion]['cuotas'] = lista

def crearPrestamo(posicion):
    valorPrestamo = input('Digite valor del prestamo: ')
    numeroCuotasPrestamo = input('Digite numero de cuotas: ')

    prestamo = Prestamo(int(valorPrestamo), int(numeroCuotasPrestamo))
    prestamo.crearPrestamo(posicion)

    print(data)
    print('')
    menu()


def buscarUsuario(opcion):
    usuario = int(input('Digite cedula de usuario: '))
    posicion = 0
    for u in data:
        if u['usuarios'][0]['cedula'] == usuario:
            if opcion == 2:
                crearPrestamo(posicion)
            elif opcion == 3:
                pagarCuota(posicion)
            crearPrestamo(posicion)
            break
        posicion = posicion + 1


def crearUsuario():
    cedula = input('Digite cedula')
    nombre = input('Digite nombre')
    edad = input('Digite edad')
    correo = input('Digite correo')
    print('')
    usuario = Usuario(cedula, nombre, edad, correo, 0, 0, 0, 0, False)
    usuario.crearUsuario()
    print(data)
    print('')
    menu()


def procesarOpciones(opcion):
     if opcion == 1:
         crearUsuario()
     elif opcion == 2:
         crearPrestamo(2)
     elif opcion == 3:
         crearUsuario(3)
     elif opcion == 4:
         crearUsuario()


def menu():
     print('***MI BANCO**')
     print('1- Registrar usuarios')
     print('2- Realizar prestamo')
     print('3- Pagos de cuotas')
     print('4- Reportes')
     print('')
     opcion = int(input('Seleccione opcion: '))
     procesarOpciones(opcion)

menu()