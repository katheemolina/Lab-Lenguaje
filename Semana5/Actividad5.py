# __init__: Constructor que inicializa los atributos de un contacto
# if __name__ == "__main__":: Actua como metodo main, se ejecuta directamente.

class Correo:
    def __init__(self, asunto, mensaje, remitente, destinatario, leido=False):
        self.asunto = asunto
        self.mensaje = mensaje
        self.remitente = remitente
        self.destinatario = destinatario if isinstance(destinatario, list) else [destinatario]
        self.leido = leido

    def marcar_como_leido(self):
        self.leido = True

class Contacto:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

class Cuenta:
    def __init__(self, nombre_usuario, direccion_mail, servidor_entrada, servidor_salida):
        self.nombre_usuario = nombre_usuario
        self.direccion_mail = direccion_mail
        self.servidor_entrada = servidor_entrada
        self.servidor_salida = servidor_salida
        self.correos_recibidos = []
        self.correos_enviados = []
        self.contactos = []

    def cantidad_correos(self):
        return len(self.correos_recibidos) + len(self.correos_enviados)

    def cantidad_correos_recibidos(self):
        return len(self.correos_recibidos)

    def cantidad_correos_enviados(self):
        return len(self.correos_enviados)

    def cantidad_correos_no_leidos(self):
        return sum(1 for correo in self.correos_recibidos if not correo.leido)

    def cantidad_contactos(self):
        return len(self.contactos)

    def agregar_correo_recibido(self, correo):
        self.correos_recibidos.append(correo)

    def enviar_correo(self, correo):
        self.correos_enviados.append(correo)

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una cuenta
    cuenta = Cuenta("usuario", "usuario@gmail.com", "imap.gmail.com", "smtp.gmail.com")

    # Crear algunos contactos
    contacto1 = Contacto("Juan", "Perez", "jperez@gmail.com")
    contacto2 = Contacto("Paco", "Rodrigez", "arodrigez@gmail.com")
    contacto3 = Contacto("Juliana", "Gonzales", "jgonzales@gmail.com")

    # Agregar contactos a la cuenta
    cuenta.agregar_contacto(contacto1)
    cuenta.agregar_contacto(contacto2)
    cuenta.agregar_contacto(contacto3)

    # Crear algunos correos
    correo1 = Correo("Hola", "Este es un mensaje de prueba.", contacto1.email, contacto2.email)
    correo2 = Correo("Re: Hola", "Gracias por tu mensaje.", contacto2.email, contacto1.email, leido=True)

    # Agregar correos a las carpetas correspondientes
    cuenta.agregar_correo_recibido(correo1)
    cuenta.enviar_correo(correo2)

    # Consultar información
    print("Cantidad total de correos:", cuenta.cantidad_correos())
    print("Cantidad de correos recibidos:", cuenta.cantidad_correos_recibidos())
    print("Cantidad de correos enviados:", cuenta.cantidad_correos_enviados())
    print("Cantidad de correos no leidos:", cuenta.cantidad_correos_no_leidos())
    print("Cantidad de contactos:", cuenta.cantidad_contactos())
