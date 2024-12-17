class AddRecordView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Добавить запись")
        self.geometry("400x300")

        self.entries = {}
        fields = ["Фамилия", "Имя", "Отчество", "Квалификация", "Профессия", "Дата рождения", "Телефон", "Адрес"]

        for i, field in enumerate(fields):
            label = tk.Label(self, text=field)
            label.grid(row=i, column=0, padx=10, pady=5)

            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[field] = entry

        self.save_button = tk.Button(self, text="Сохранить")
        self.save_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

  
class AddRecordController:
    def __init__(self, repository, parent_controller):
        self.repository = repository
        self.parent_controller = parent_controller
        self.view = AddRecordView()

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
            self.repository.add_soiskatel(soiskatel)

            self.view.destroy()
        except ValueError as e:
            tk.messagebox.showerror("Ошибка", str(e))

      class MainController:
    def __init__(self):
        # Предыдущий код...

    def add_record(self):
        AddRecordController(self.repository, self)
