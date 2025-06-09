class Computadora:
    def __init__(self):
        self.procesador = None
        self.ram = None
        self.almacenamiento = None
        self.tarjeta_grafica = None
        self.sistema_operativo = None
        self.monitor = None
    def __str__(self):
        partes = [
            f"Procesador: {self.procesador or 'No especificado'}",
            f"RAM: {self.ram or 'No especificada'}",
            f"Almacenamiento: {self.almacenamiento or 'No especificado'}",
            f"Tarjeta Gráfica: {self.tarjeta_grafica or 'No especificada'}",
            f"Sistema Operativo: {self.sistema_operativo or 'No especificado'}",
            f"Monitor: {self.monitor or 'No especificado'}"
        ]
        return "Configuración de la Computadora:\n" + "\n".join(partes)
class ConstructorComputadora:
    def __init__(self):
        self.computadora = Computadora()
    def establecer_procesador(self, procesador):
        pass 
    def establecer_ram(self, ram):
        pass
    def establecer_almacenamiento(self, almacenamiento):
        pass
    def establecer_tarjeta_grafica(self, tarjeta_grafica):
        pass
    def establecer_sistema_operativo(self, so):
        pass
    def establecer_monitor(self, monitor):
        pass
    def obtener_computadora(self) -> Computadora:
        return self.computadora
class ConstructorComputadoraEscritorio(ConstructorComputadora):
    def establecer_procesador(self, procesador):
        self.computadora.procesador = procesador
        return self
    def establecer_ram(self, ram):
        self.computadora.ram = ram
        return self
    def establecer_almacenamiento(self, almacenamiento):
        self.computadora.almacenamiento = almacenamiento
        return self
    def establecer_tarjeta_grafica(self, tarjeta_grafica):
        self.computadora.tarjeta_grafica = tarjeta_grafica
        return self
    def establecer_sistema_operativo(self, so):
        self.computadora.sistema_operativo = so
        return self
    def establecer_monitor(self, monitor):
        self.computadora.monitor = monitor
        return self
class FabricanteComputadoras:
    def __init__(self, constructor: ConstructorComputadora):
        self._constructor = constructor
    def construir_pc_gaming(self):
        return self._constructor \
            .establecer_procesador("Intel Core i9") \
            .establecer_ram("32GB DDR5") \
            .establecer_almacenamiento("1TB NVMe SSD") \
            .establecer_tarjeta_grafica("NVIDIA RTX 4080") \
            .establecer_sistema_operativo("Windows 11 Pro") \
            .establecer_monitor("27-pulgadas 144Hz 4K") \
            .obtener_computadora()
    def construir_pc_oficina(self):
        return self._constructor \
            .establecer_procesador("Intel Core i5") \
            .establecer_ram("16GB DDR4") \
            .establecer_almacenamiento("500GB SSD") \
            .establecer_sistema_operativo("Windows 10 Home") \
            .establecer_monitor("24-pulgadas Full HD") \
            .obtener_computadora()
print("--- Construyendo una PC para Gaming ---")
constructor_gaming = ConstructorComputadoraEscritorio()
fabricante = FabricanteComputadoras(constructor_gaming)
pc_gaming = fabricante.construir_pc_gaming()
print(pc_gaming)
print("\n--- Construyendo una PC para Oficina ---")
constructor_oficina = ConstructorComputadoraEscritorio()
fabricante_oficina = FabricanteComputadoras(constructor_oficina) 
pc_oficina = fabricante_oficina.construir_pc_oficina()
print(pc_oficina)
print("\n--- Construyendo una PC Personalizada (directamente con el Constructor) ---")
pc_personalizada = ConstructorComputadoraEscritorio() \
    .establecer_procesador("AMD Ryzen 7") \
    .establecer_ram("64GB DDR5") \
    .establecer_almacenamiento("2TB NVMe SSD") \
    .establecer_tarjeta_grafica("AMD Radeon RX 7900 XT") \
    .establecer_sistema_operativo("Linux Ubuntu") \
    .obtener_computadora()
print(pc_personalizada)