import unittest

from src.clientes.registro import (
    CorreoDuplicado,
    ErrorValidacion,
    RegistrarCliente,
    RepositorioEnMemoria,
)


class NotificadorFalso:
    def __init__(self):
        self.notificados = []

    def cliente_registrado(self, cliente):
        self.notificados.append(cliente)


class RegistrarClienteTests(unittest.TestCase):
    def setUp(self):
        self.repo = RepositorioEnMemoria()
        self.notificador = NotificadorFalso()
        self.servicio = RegistrarCliente(self.repo, self.notificador)

    def test_registra_y_normaliza_correo(self):
        cliente = self.servicio.ejecutar("Santiago", "  SANTIAGO@example.com ")
        self.assertEqual(cliente.correo, "santiago@example.com")
        self.assertEqual(self.notificador.notificados, [cliente])

    def test_rechaza_nombre_vacio(self):
        with self.assertRaises(ErrorValidacion):
            self.servicio.ejecutar(" ", "santiago@example.com")

    def test_rechaza_correo_duplicado(self):
        self.servicio.ejecutar("Santiago", "santiago@example.com")
        with self.assertRaises(CorreoDuplicado):
            self.servicio.ejecutar("Santiago", "santiago@example.com")


if __name__ == "__main__":
    unittest.main()
