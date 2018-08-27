class Prestamo:
    cedulaPrestamo = 0
    valorPrestamo = 0
    numeroCuotaPrestamo = 0
    prestamos = []
    prestamo = {}

    def __init__(self, cedulaPrestamo, valorPrestamo, numeroCuotaPrestamo):
        self.cedulaPrestamo = cedulaPrestamo
        self.valorPrestamo = valorPrestamo
        self.numeroCuotaPrestamo = numeroCuotaPrestamo

    def crear_prestamo(self):
         self.prestamo = {
             'cedulaPrestamo': self.cedulaPrestamo,
             'valorPrestamo': self.valorPrestamo,
             'numeroCuotaPrestamo': self.numeroCuotaPrestamo,
         }
         self.prestamos.append(self.prestamo)


class Cuotas:
    cedulaCuota = 0
    numeroCuota = 0
    valorCuota = 0
    estado = bool
    cuotas = []
    cuota = {}

    def __init__(self, cedulaCuota, numeroCuota, valorCuota):
        self.cedulaCuota = cedulaCuota
        self.numeroCuota = numeroCuota
        self.valorCuota = valorCuota
        self.estado = bool

    def pagar_cuota(self):
         self.cuota = {
             'cedulaCuota': self.cedulaCuota,
             'numeroCuota': self.numeroCuota,
             'valorCuota': self.valorCuota,
             'estado': self.estado
         }
         self.cuotas.append(self.cuota)

class Usuario(Prestamo,Cuotas):
    cedula = 0
    nombre = ""
    edad = 0
    correo = ""
    usuarios = []
    usuario = {}

    def __init__(self, cedula, nombre, edad, correo, cedulaPrestamo, valorPrestamo, numeroCuotaPrestamo, cedulaCuota, numeroCuota, valorCuota, estado ):
        Prestamo.__init__(self, cedulaPrestamo, valorPrestamo, numeroCuotaPrestamo)
        Cuotas.__init__(self, cedulaCuota, numeroCuota, valorCuota, estado)
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def crear_usuario(self):
            self.usuario = {
                'cedula': self.cedula,
                'nombre': self.nombre,
                'edad': self.edad,
                'correo': self.correo
            }
            self.usuarios.append(self.usuario)


def menu():
    salir = 0
    while salir != 1:
        print('---MENU DE OPCIONES---')
        print('1) Registrar usuarios')
        print('2) Registrar Prestamo')
        print('3) Pagar Cuota')
        print('4) Reportes')
        print('5) salir')
        seleccion = int(input('digite una opcion:'))

        if seleccion == 1:

            print('---crear usuarios--')
            cedula = int(input('Digite el cedula de usuario: '))
            nombre = input('Digite nombre de usuario: ')
            edad = int(input('Digite edad de usuario: '))
            correo = input('Digite  correo de usuario: ')
            usuario = Usuario(cedula, nombre, edad, correo)
            usuario.crear_usuario()

        elif seleccion == 2:
            print('---crear prestamo--')
            cedulaPrestamo = int(input('digite el cedula del usuario: '))
            valorPrestamo = int(input('Digite el valor del prestamo: '))
            numeroCuotaPrestamo = int(input('Digite numero de cuotas a pagar del prestamo: '))
            valorCuota = valorPrestamo/numeroCuotaPrestamo
            prestamo = Prestamo(cedulaPrestamo, valorPrestamo, numeroCuotaPrestamo)
            prestamo.crear_prestamo()
            cuota = Cuotas(cedulaPrestamo, numeroCuotaPrestamo, valorCuota, 'false')
            cuota.pagar_cuota()

        elif seleccion == 3:
            print('---pagar cuota---')
            cedulaCuota = int(input('digite cedula de usuario: '))
          
        elif seleccion == 4:
            print('buscar usuarios')

        elif seleccion == 5:
            print('salir')
            salir = 1

menu()

