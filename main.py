from singleton.database_connection import DatabaseConnection
from factory.notification_factory import NotificationFactory
from abstract_factory.gui_factories import WindowsFactory, MacOSFactory
from builder.computer import ComputerBuilder

def demonstrate_singleton():
    print("=== 1. SINGLETON PATTERN ===")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    print(f"db1 is db2: {db1 is db2}")
    db1.execute_query("SELECT * FROM users")
    print()

def demonstrate_factory():
    print("=== 2. FACTORY METHOD PATTERN ===")
    factory = NotificationFactory()
    
    email = factory.create_notification("email")
    sms = factory.create_notification("sms")
    push = factory.create_notification("push")
    
    email.send("Добро пожаловать в наше приложение!")
    sms.send("Ваш код подтверждения: 123456")
    push.send("У вас новое сообщение")
    print()

def demonstrate_abstract_factory():
    print("=== 3. ABSTRACT FACTORY PATTERN ===")
    
    # Windows UI
    windows_factory = WindowsFactory()
    windows_button = windows_factory.create_button()
    windows_checkbox = windows_factory.create_checkbox()
    
    print("Windows UI:")
    windows_button.render()
    windows_checkbox.render()
    
    # MacOS UI
    mac_factory = MacOSFactory()
    mac_button = mac_factory.create_button()
    mac_checkbox = mac_factory.create_checkbox()
    
    print("MacOS UI:")
    mac_button.render()
    mac_checkbox.render()
    print()

def demonstrate_builder():
    print("=== 4. BUILDER PATTERN ===")
    
    # Простой компьютер
    basic_computer = (ComputerBuilder()
                     .set_cpu("Intel i3")
                     .set_ram("8GB")
                     .build())
    print(f"Базовый компьютер: {basic_computer}")
    
    # Игровой компьютер
    gaming_computer = (ComputerBuilder()
                      .set_cpu("Intel i9")
                      .set_ram("32GB")
                      .set_storage("1TB NVMe SSD")
                      .set_graphics_card("NVIDIA RTX 4080")
                      .set_bluetooth(True)
                      .set_wifi(True)
                      .build())
    print(f"Игровой компьютер: {gaming_computer}")
    
    # Офисный компьютер
    office_computer = (ComputerBuilder()
                      .set_cpu("AMD Ryzen 5")
                      .set_ram("16GB")
                      .set_storage("512GB SSD")
                      .set_wifi(True)
                      .build())
    print(f"Офисный компьютер: {office_computer}")

if __name__ == "__main__":
    demonstrate_singleton()
    demonstrate_factory()
    demonstrate_abstract_factory()
    demonstrate_builder()