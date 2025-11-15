from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# Windows реализации
class WindowsButton(Button):
    def render(self):
        print("кнопка Windows")

class WindowsCheckbox(Checkbox):
    def render(self):
        print("чекбокс Windows")

# MacOS реализации
class MacOSButton(Button):
    def render(self):
        print("кнопка MacOS")

class MacOSCheckbox(Checkbox):
    def render(self):
        print("чекбокс MacOS")