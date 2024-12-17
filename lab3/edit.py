import tkinter as tk


class EditRecordView(tk.Toplevel):
    def __init__(self, master=None, data=None):
        super().__init__(master)
        self.title("Редактировать запись")
        self.geometry("400x300")

        self.entries = {}
        fields = ["Фамилия", "Имя", "Отчество", "Квалификация", "Профессия", "Дата рождения", "Телефон", "Адрес"]

        for i, field in enumerate(fields):
            label = tk.Label(self, text=field)
            label.grid(row=i, column=0, padx=10, pady=5)

            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[field] = entry

            # Заполнение данными
            if data and field in data:
                entry.insert(0, data[field])

        self.save_button = tk.Button(self, text="Сохранить")
        self.save_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

  class EditRecordController:
    def __init__(self, repository, parent_controller, record_index):
        self.repository = repository
        self.parent_controller = parent_controller
        self.record_index = record_index
        self.current_record = repository.get_all()[record_index]

        # Подготовка данных для окна
        data = {
            "Фамилия": self.current_record.fam,
            "Имя": self.current_record.imya,
            "Отчество": self.current_record.otchestvo,
            "Квалификация": self.current_record.kvalifikaciya,
            "Профессия": self.current_record.professiya,
            "Дата рождения": self.current_record.data_rozhdeniya,
            "Телефон": self.current_record.telefon,
            "Адрес": self.current_record.adres,
        }

        self.view = EditRecordView(data=data)

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

            updated_soiskatel = Soiskatel(fam, imya, otchestvo, kvalifikaciya, professiya, data_rozhdeniya, telefon, adres)
            self.repository.data[self.record_index] = updated_soiskatel
            self.repository.notify_observers()

            self.view.destroy()
        except ValueError as e:
            tk.messagebox.showerror("Ошибка", str(e))

      class MainController:
    def __init__(self):
        # Предыдущий код...

    def edit_record(self):
        selected_item = self.view.table.selection()
        if selected_item:
            index = self.view.table.index(selected_item[0])
            EditRecordController(self.repository, self, index)
