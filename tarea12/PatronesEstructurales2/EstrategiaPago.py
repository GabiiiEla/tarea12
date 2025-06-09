from abc import ABC, abstractmethod

class EstrategiaPago(ABC):
    @abstractmethod
    def pagar(self, monto: float):
        pass

class PagoTarjetaCredito(EstrategiaPago):
    def pagar(self, monto: float):
        print(f"Pagando ${monto:.2f} con Tarjeta de Crédito. Procesando pago...")
        print("Pago con Tarjeta de Crédito completado.")

class PagoPayPal(EstrategiaPago):
    def pagar(self, monto: float):
        print(f"Pagando ${monto:.2f} con PayPal. Redirigiendo a PayPal...")
        print("Pago con PayPal completado.")

class PagoTransferenciaBancaria(EstrategiaPago):
    def pagar(self, monto: float):
        print(f"Pagando ${monto:.2f} con Transferencia Bancaria. Generando instrucciones...")
        print("Pago con Transferencia Bancaria completado.")

class CarritoCompras:
    def __init__(self, estrategia_pago: EstrategiaPago):
        """
        El carrito de compras se inicializa con una estrategia de pago.
        """
        self._estrategia_pago = estrategia_pago
        self._items = []

    def agregar_item(self, nombre: str, precio: float):
        self._items.append((nombre, precio))
        print(f"Artículo '{nombre}' ( ${precio:.2f}) agregado al carrito.")

    def establecer_estrategia_pago(self, nueva_estrategia: EstrategiaPago):
        """
        Permite cambiar la estrategia de pago en tiempo de ejecución.
        """
        self._estrategia_pago = nueva_estrategia
        print(f"Estrategia de pago cambiada a: {nueva_estrategia.__class__.__name__}")

    def pagar_carrito(self):
        """
        Calcula el total y delega el proceso de pago a la estrategia actual.
        """
        if not self._items:
            print("El carrito está vacío. No hay nada que pagar.")
            return

        total_monto = sum(item[1] for item in self._items)
        print(f"\n--- Resumen del Carrito ---")
        for item_nombre, item_precio in self._items:
            print(f"- {item_nombre}: ${item_precio:.2f}")
        print(f"Total a pagar: ${total_monto:.2f}")
        print(f"Procesando pago con la estrategia: {self._estrategia_pago.__class__.__name__}")

        self._estrategia_pago.pagar(total_monto) 
        self._items = [] 
        print("Transacción completada.")

estrategia_tarjeta = PagoTarjetaCredito()
estrategia_paypal = PagoPayPal()
estrategia_transferencia = PagoTransferenciaBancaria()

print("--- Escenario 1: Pago con Tarjeta de Crédito ---")
carrito1 = CarritoCompras(estrategia_tarjeta)
carrito1.agregar_item("Libro 'Patrones de Diseño'", 45.00)
carrito1.agregar_item("Taza de café", 12.50)
carrito1.pagar_carrito()

print("\n--- Escenario 2: Cambiar la estrategia a PayPal en tiempo de ejecución ---")
carrito2 = CarritoCompras(estrategia_tarjeta) 
carrito2.agregar_item("Auriculares inalámbricos", 99.99)
carrito2.establecer_estrategia_pago(estrategia_paypal) 
carrito2.pagar_carrito()

print("\n--- Escenario 3: Carrito con Pago por Transferencia Bancaria desde el inicio ---")
carrito3 = CarritoCompras(estrategia_transferencia)
carrito3.agregar_item("Monitor 27 pulgadas", 250.00)
carrito3.pagar_carrito()

print("\n--- Escenario 4: Carrito vacío ---")
carrito4 = CarritoCompras(estrategia_tarjeta)
carrito4.pagar_carrito()