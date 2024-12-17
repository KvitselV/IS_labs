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

    def add_soiskatel(self, soiskatel):
        self.data.append(soiskatel)
        self.notify_observers()
    
    def get_all(self):
        return self.data

    def remove_soiskatel(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]
            self.notify_observers()

    def attach_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def get_count(self):
        """Возвращает общее количество записей."""
        return len(self.data)

    def get_k_n_short_list(self, k, n, field, reverse=False):
        """
        Возвращает n записей, начиная с k, отсортированные по полю.
        :param k: Индекс начальной записи.
        :param n: Количество записей для возврата.
        :param field: Поле для сортировки.
        :param reverse: Направление сортировки (по убыванию).
        :return: Список записей.
        """
        field_map = {
            "Фамилия": "fam",
            "Имя": "imya",
            "Профессия": "professiya",
            "Квалификация": "kvalifikaciya",
            "Дата рождения": "data_rozhdeniya",
            "Телефон": "telefon",
            "Адрес": "adres"
        }
        if field in field_map:
            attribute = field_map[field]
            sorted_data = sorted(self.data, key=lambda x: getattr(x, attribute), reverse=reverse)
            return sorted_data[k:k + n]
        return []

    
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

        # Панель управления
        self.control_frame = tk.Frame(self)
        self.control_frame.pack(fill=tk.X)

        self.add_button = tk.Button(self.control_frame, text="Добавить запись")
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.edit_button = tk.Button(self.control_frame, text="Редактировать запись")
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.control_frame, text="Удалить запись")
        self.delete_button.pack(side=tk.LEFT, padx=5)

# Сортировка
        self.sort_frame = tk.Frame(self)
        self.sort_frame.pack(fill=tk.X)

        self.sort_label = tk.Label(self.sort_frame, text="Сортировать по:")
        self.sort_label.pack(side=tk.LEFT, padx=5)

        self.sort_field = ttk.Combobox(self.sort_frame, values=["Фамилия", "Имя", "Профессия", "Квалификация", "Дата рождения", "Телефон", "Адрес"])
        self.sort_field.set("Фамилия")
        self.sort_field.pack(side=tk.LEFT, padx=5)

        self.sort_asc_button = tk.Button(self.sort_frame, text="По возрастанию")
        self.sort_asc_button.pack(side=tk.LEFT, padx=5)

        self.sort_desc_button = tk.Button(self.sort_frame, text="По убыванию")
        self.sort_desc_button.pack(side=tk.LEFT, padx=5)

class RecordView(tk.Toplevel):
    def __init__(self, master=None, fields=None, data=None, title="Окно записи"):
        super().__init__(master)
        self.title(title)
        self.geometry("400x300")

        self.entries = {}
        for i, field in enumerate(fields):
            label = tk.Label(self, text=field)
            label.grid(row=i, column=0, padx=10, pady=5)

            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[field] = entry

            if data and field in data:
                entry.insert(0, data[field])

        self.save_button = tk.Button(self, text="Сохранить")
        self.save_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

class RecordDetailsView(tk.Toplevel):
    def __init__(self, soiskatel):
        super().__init__()
        self.title("Детали соискателя")
        self.geometry("400x300")

        fields = {
            "Фамилия": soiskatel.fam,
            "Имя": soiskatel.imya,
            "Отчество": soiskatel.otchestvo,
            "Квалификация": soiskatel.kvalifikaciya,
            "Профессия": soiskatel.professiya,
            "Дата рождения": soiskatel.data_rozhdeniya,
            "Телефон": soiskatel.telefon,
            "Адрес": soiskatel.adres,
        }

        for i, (field, value) in enumerate(fields.items()):
            label = tk.Label(self, text=f"{field}:")
            label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

            value_label = tk.Label(self, text=value, anchor="w")
            value_label.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)

        close_button = tk.Button(self, text="Закрыть", command=self.destroy)
        close_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

# Контроллеры
class RecordController:
    def __init__(self, repository, parent_controller, mode="add", record_index=None):
        self.repository = repository
        self.parent_controller = parent_controller
        self.mode = mode
        self.record_index = record_index

        fields = ["Фамилия", "Имя", "Отчество", "Квалификация", "Профессия", "Дата рождения", "Телефон", "Адрес"]
        data = None

        if mode == "edit":
            current_record = repository.get_all()[record_index]
            data = {
                "Фамилия": current_record.fam,
                "Имя": current_record.imya,
                "Отчество": current_record.otchestvo,
                "Квалификация": current_record.kvalifikaciya,
                "Профессия": current_record.professiya,
                "Дата рождения": current_record.data_rozhdeniya,
                "Телефон": current_record.telefon,
                "Адрес": current_record.adres,
            }

        self.view = RecordView(fields=fields, data=data, title="Редактирование записи" if mode == "edit" else "Добавление записи")
        self.view.save_button.config(command=self.save_record)

    def save_record(self):
        try:
            fam = self.view.entries["Фамилия"].get()
            imya = self.view.entries["Имя"].get()
            otchestvo = self.view.entries["Отчество"].get()
            kvalifikaciya = self.view.entries["Квалификация"].get()
            professiya = self.view.entries["Профессия"].get()
            data_rozhdeniya = self.view.entries["Дата рождения"].get()
            telefon = self.view.entries["Телефон"].get()
            adres = self.view.entries["Адрес"].get()

            if not fam or not imya or not professiya:
                raise ValueError("Обязательные поля: Фамилия, Имя, Профессия")

            soiskatel = Soiskatel(fam, imya, otchestvo, kvalifikaciya, professiya, data_rozhdeniya, telefon, adres)

            if self.mode == "add":
                self.repository.add_soiskatel(soiskatel)
            elif self.mode == "edit":
                self.repository.data[self.record_index] = soiskatel
                self.repository.notify_observers()

            self.view.destroy()
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

class RecordDetailsController:
    def __init__(self, repository, soiskatel):
        self.repository = repository
        self.soiskatel = soiskatel
        self.view = RecordDetailsView(self.soiskatel)


class MainController:
    def __init__(self):
        self.repository = Repository()
        self.view = MainWindowView()

        self.repository.attach_observer(self)
        self.update()

    # Привязка кнопок
        self.view.add_button.config(command=self.add_record)
        self.view.edit_button.config(command=self.edit_record)
        self.view.delete_button.config(command=self.delete_record)
        self.view.sort_asc_button.config(command=self.sort_ascending)
        self.view.sort_desc_button.config(command=self.sort_descending)
        
        self.view.table.bind("<Double-1>", self.show_record_details)

    def show_record_details(self, event):
        selected_item = self.view.table.selection()
        if selected_item:
            index = self.view.table.index(selected_item[0])
            soiskatel = self.repository.get_all()[index]
            RecordDetailsController(self.repository, soiskatel)
            
    def add_record(self):
        RecordController(self.repository, self, mode="add")

    def edit_record(self):
        selected_item = self.view.table.selection()
        if selected_item:
            index = self.view.table.index(selected_item[0])
            RecordController(self.repository, self, mode="edit", record_index=index)
    
    def delete_record(self):
        selected_item = self.view.table.selection()
        if selected_item:
            index = self.view.table.index(selected_item[0])
            self.repository.remove_soiskatel(index)
            
    def update_table(self, soiskateli):
        """Обновление данных в таблице."""
        for row in self.view.table.get_children():
            self.view.table.delete(row)
        for soiskatel in soiskateli:
            self.view.table.insert("", "end", values=(soiskatel.fam, soiskatel.imya, soiskatel.professiya))
   
    def update(self):
        for row in self.view.table.get_children():
            self.view.table.delete(row)
        for soiskatel in self.repository.get_all():
            self.view.table.insert("", "end", values=(soiskatel.fam, soiskatel.imya, soiskatel.professiya))

    def sort_and_display(self, reverse=False):
        field = self.view.sort_field.get()
        k = 0  # Начальный индекс
        n = self.repository.get_count()  # Общее количество записей

        sorted_list = self.repository.get_k_n_short_list(k, n, field, reverse)
        self.update_table(sorted_list)

    def sort_ascending(self):
        """Сортировка по возрастанию."""
        self.sort_and_display(reverse=False)

    def sort_descending(self):
        """Сортировка по убыванию."""
        self.sort_and_display(reverse=True)


# Запуск программы
if __name__ == "__main__":
    app = MainController()
    app.view.mainloop()
