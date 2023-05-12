from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#======================================
# S3 es hijo de RepositorioDeUsuarios
#======================================
class S3(RepositorioDeUusarios):
    __clientId: str
    __secretKey: str
    __buckey: str

    def __init__(mi, clientId: str, secretKey: str, bucket: str):
        mi.__clientId = clientId
        mi.__secretKey = secretKey
        mi.__bucket = bucket

    def abrir(mi) -> None:
        print(f"EStableciendo conexión a AWS S3 {mi.__clientId}:{mi.__secretKey}")
    
    def guardar(mi, usuario:Usuario) -> None:
        userData = { "nombre": usuario.getNombre(),
                 "apellido": usuario.getApellido(),
                 "edad": usuario.getEdad() }
        print(f"GUardando usuario de la bandeja:{mi.__bucket}: {userData}")


    def cerrar(mi) -> None:
        print("Cerrando conexión AWS S3")

