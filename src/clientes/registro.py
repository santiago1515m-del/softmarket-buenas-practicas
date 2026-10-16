"""Ejemplo de registro de clientes aplicando los principios SOLID."""
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Cliente:
    nombre: str
    correo: str


class ClienteRepository(Protocol):
    def obtener_por_correo(self, correo: str) -> Cliente | None: ...
    def guardar(self, cliente: Cliente) -> None: ...


class NotificadorCliente(Protocol):
    def cliente_registrado(self, cliente: Cliente) -> None: ...


class ErrorValidacion(ValueError):
    pass


class CorreoDuplicado(ValueError):
    pass


class RegistrarCliente:
    """Coordina las reglas de alta sin depender de SQL ni de un proveedor de correo."""

    def __init__(self, repositorio: ClienteRepository, notificador: NotificadorCliente):
        self._repositorio = repositorio
        self._notificador = notificador

    def ejecutar(self, nombre: str, correo: str) -> Cliente:
        nombre = nombre.strip()
        correo = correo.strip().lower()
        if not nombre:
            raise ErrorValidacion("El nombre es obligatorio")
        if "@" not in correo or correo.startswith("@") or correo.endswith("@"):
            raise ErrorValidacion("El correo no tiene un formato válido")
        if self._repositorio.obtener_por_correo(correo) is not None:
            raise CorreoDuplicado("Ya existe un cliente con ese correo")

        cliente = Cliente(nombre=nombre, correo=correo)
        self._repositorio.guardar(cliente)
        self._notificador.cliente_registrado(cliente)
        return cliente


class RepositorioEnMemoria:
    """Adaptador simple para demostración; en producción se usaría una base de datos."""

    def __init__(self):
        self.clientes: dict[str, Cliente] = {}

    def obtener_por_correo(self, correo: str) -> Cliente | None:
        return self.clientes.get(correo)

    def guardar(self, cliente: Cliente) -> None:
        self.clientes[cliente.correo] = cliente


class NotificadorEnConsola:
    """Adaptador de ejemplo; puede sustituirse por correo u otro canal."""

    def cliente_registrado(self, cliente: Cliente) -> None:
        print(f"Cliente registrado: {cliente.correo}")
