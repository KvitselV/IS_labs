import tkinter as tk
from tkinter import ttk, messagebox


# Модель
class Soiskatel:
    def __init__(self, fam, imya, otchestvo, kvalifikaciya, professiya, data_rozhdeniya, telefon, adres):
        self.fam = fam
        self.imya = imya
        self.otchestvo = otchestvo
        self.kvalifikaciya = kvalifikaciya
        self.professiya = professiya
        self.data_rozhdeniya = data_rozhdeniya
        self.telefon = telefon
        self.adres = adres


class Repository:
    def __init__(self):
        self.data = []
        self.observers = []

    def get_all(self):
        return self.data



    def attach_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    
# Виды
class MainWindowView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Список соискателей")
        self.geometry("800x400")

        # Таблица
        self.table = ttk.Treeview(self, columns=("fam", "imya", "professiya"), show="headings")
        self.table.heading("fam", text="Фамилия")
        self.table.heading("imya", text="Имя")
        self.table.heading("professiya", text="Профессия")
        self.table.pack(fill=tk.BOTH, expand=True)




# Контроллеры


class MainController:
    def __init__(self):
        self.repository = Repository()
        self.view = MainWindowView()

        self.repository.attach_observer(self)
        self.update()

        
    def update(self):
        for row in self.view.table.get_children():
            self.view.table.delete(row)
        for soiskatel in self.repository.get_all():
            self.view.table.insert("", "end", values=(soiskatel.fam, soiskatel.imya, soiskatel.professiya))


# Запуск программы
if __name__ == "__main__":
    app = MainController()
    app.view.mainloop()
