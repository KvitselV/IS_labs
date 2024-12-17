import tkinter as tk


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
            tk.messagebox.showerror("Ошибка", str(e))

                               from record_controller import RecordController

class MainController:
    def __init__(self):
        # Предыдущий код...

    def add_record(self):
        RecordController(self.repository, self, mode="add")

    def edit_record(self):
        selected_item = self.view.table.selection()
        if selected_item:
            index = self.view.table.index(selected_item[0])
            RecordController(self.repository, self, mode="edit", record_index=index)
