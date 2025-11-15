class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.graphics_card = None
        self.has_bluetooth = False
        self.has_wifi = False
    
    def __str__(self):
        return (f"Computer(CPU={self.cpu}, RAM={self.ram}, "
                f"Storage={self.storage}, Graphics={self.graphics_card}, "
                f"Bluetooth={self.has_bluetooth}, WiFi={self.has_wifi})")

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()
    
    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self
    
    def set_ram(self, ram):
        self.computer.ram = ram
        return self
    
    def set_storage(self, storage):
        self.computer.storage = storage
        return self
    
    def set_graphics_card(self, graphics_card):
        self.computer.graphics_card = graphics_card
        return self
    
    def set_bluetooth(self, has_bluetooth):
        self.computer.has_bluetooth = has_bluetooth
        return self
    
    def set_wifi(self, has_wifi):
        self.computer.has_wifi = has_wifi
        return self
    
    def build(self):
        return self.computer