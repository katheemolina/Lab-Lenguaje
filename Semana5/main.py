class Correo:
    def __init__(self, asunto, mensaje, remitente, destinatario, leido=False):
        self.asunto = asunto
        self.mensaje = mensaje
        self.remitente = remitente
        self.destinatario = destinatario
        self.leido = leido

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

    def cantidad_correos_no_leidos(self):
        return len([correo for correo in self.correos_recibidos if not correo.leido])

    def enviar_correo(self, correo):
        self.correos_enviados.append(correo)

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

def mostrar_menu():
    print("\n--- Menú Cliente de Correo ---")
    print("1. Ver cantidad total de correos")
    print("2. Ver correos recibidos")
    print("3. Ver correos enviados")
    print("4. Ver cantidad de correos no leídos")
    print("5. Ver contactos")
    print("6. Enviar correo")
    print("7. Agregar contacto")
    print("8. Salir")
    return input("Elige una opción: ")

def consola_interactiva(cuenta):
    while True:
        opcion = mostrar_menu()

        match opcion:
            case "1":
                print(f"Cantidad total de correos: {cuenta.cantidad_correos()}")
            case "2":
                if cuenta.correos_recibidos:
                    print("\n--- Correos Recibidos ---")
                    for i, correo in enumerate(cuenta.correos_recibidos):
                        estado = "Leído" if correo.leido else "No leído"
                        print(f"{i + 1}. Asunto: {correo.asunto}, Remitente: {correo.remitente}, Estado: {estado}")
                else:
                    print("No tienes correos recibidos.")
            case "3":
                if cuenta.correos_enviados:
                    print("\n--- Correos Enviados ---")
                    for i, correo in enumerate(cuenta.correos_enviados):
                        print(f"{i + 1}. Asunto: {correo.asunto}, Destinatario: {correo.destinatario}")
                else:
                    print("No tienes correos enviados.")
            case "4":
                print(f"Cantidad de correos no leídos: {cuenta.cantidad_correos_no_leidos()}")
            case "5":
                if cuenta.contactos:
                    print("\n--- Contactos ---")
                    for contacto in cuenta.contactos:
                        print(f"Nombre: {contacto.nombre}, Apellido: {contacto.apellido}, Email: {contacto.email}")
                else:
                    print("No tienes contactos registrados.")
            case "6":
                asunto = input("Asunto: ")
                mensaje = input("Mensaje: ")
                remitente = cuenta.direccion_mail
                destinatario = input("Destinatario (email): ")
                correo = Correo(asunto, mensaje, remitente, destinatario)
                cuenta.enviar_correo(correo)
                print("Correo enviado.")
            case "7":
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                email = input("Email: ")
                contacto = Contacto(nombre, apellido, email)
                cuenta.agregar_contacto(contacto)
                print("Contacto agregado.")
            case "8":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Inténtalo de nuevo.")

# Ejemplo de uso
if __name__ == "__main__":
    cuenta = Cuenta("usuario", "usuario@gmail.com", "imap.gmail.com", "smtp.gmail.com")
    consola_interactiva(cuenta)
