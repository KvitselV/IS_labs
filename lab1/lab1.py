import json
import re
from datetime import datetime, date

class Validator:
    @staticmethod
    def validate_last_name(value):
        if not value.strip():
            raise ValueError("Last name cannot be empty.")
        if not value.isalpha():
            raise ValueError("Last name must contain only letters.")
        return value

    @staticmethod
    def validate_first_name(value):
        if not value.strip():
            raise ValueError("First name cannot be empty.")
        if not value.isalpha():
            raise ValueError("First name must contain only letters.")
        return value

    @staticmethod
    def validate_middle_name(value):
        if value.strip() and not value.isalpha():
            raise ValueError("Middle name must contain only letters if provided.")
        return value
    
    @staticmethod
    def validate_qualification(value):
        if not value.strip():
            raise ValueError("Qualification cannot be empty.")
        if not value.replace(' ', '').isalpha():
            raise ValueError("Qualification must contain only letters and spaces.")
        return value
    
    @staticmethod
    def validate_profession(value):
        if not value.strip():
            raise ValueError("Profession cannot be empty.")
        if not value.replace(' ', '').isalpha():
            raise ValueError("Profession must contain only letters and spaces.")
        return value
    
    @staticmethod
    def validate_date_of_birth(value):
        if not value.strip():
            raise ValueError("Date of birth cannot be empty.")
        try:
            datetime.strptime(value, '%Y-%m-%d')  # Формат: YYYY-MM-DD
        except ValueError:
            raise ValueError("Date of birth must be in the format YYYY-MM-DD.")
        return value
    
    @staticmethod
    def validate_phone(value):
        if not value.strip():
            raise ValueError("Phone number cannot be empty.")
        if not re.match(r'^\+\d{1,3}-\d{3}-\d{3}-\d{4}$', value):
            raise ValueError("Phone number must be in the format +XXX-XXX-XXX-XXXX.")
        return value
    
    @staticmethod
    def validate_address(value):
        if not value.strip():
            raise ValueError("Address cannot be empty.")
        return value

class Soiskatel:
    def __init__(self, last_name, first_name, middle_name, qualification, profession, date_of_birth, phone, address):
        self.last_name = Validator.validate_last_name(last_name)
        self.first_name = Validator.validate_first_name(first_name)
        self.middle_name = Validator.validate_middle_name(middle_name)
        self.qualification = Validator.validate_qualification(qualification)
        self.profession = Validator.validate_profession(profession)
        self.date_of_birth = Validator.validate_date_of_birth(date_of_birth)
        self.phone = Validator.validate_phone(phone)
        self.address = Validator.validate_address(address)

    @classmethod
    def from_json(cls, json_str):
        try:
            data = json.loads(json_str)
            return cls(
                data["last_name"], data["first_name"], data.get("middle_name", ""),
                data["qualification"], data["profession"],
                date.fromisoformat(data["date_of_birth"]),
                data["phone"], data["address"]
            )
        except (KeyError, ValueError) as e:
            raise ValueError(f"Ошибка создания Soiskatel из JSON: {e}")

    def short_info(self):
        return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0] if self.middle_name else ''}."

    def __str__(self):
        return (f"Soiskatel: {self.last_name} {self.first_name} {self.middle_name}, "
                f"Квалификация: {self.qualification}, Профессия: {self.profession}, "
                f"Дата рождения: {self.date_of_birth}, Телефон: {self.phone}, Адрес: {self.address}")

    def __eq__(self, other):
        if isinstance(other, Soiskatel):
            # Сравнение полного объекта
            return (self.last_name == other.last_name and
                    self.first_name == other.first_name and
                    self.middle_name == other.middle_name)
        elif isinstance(other, ShortSoiskatel):
            # Сравнение по краткой информации
            return (self.last_name == other.last_name and
                    self.first_name[0] == other.first_name[0] and
                    (self.middle_name[0] if self.middle_name else '') ==
                    (other.middle_name[0] if other.middle_name else ''))
        return False

class ShortSoiskatel(Soiskatel):
    def __init__(self, last_name, first_name, middle_name):
        super().__init__(last_name, first_name, middle_name, qualification="N/A", profession="N/A",
                         date_of_birth=date(1900, 1, 1), phone="0000000000", address="N/A")

    def __str__(self):
        return f"ShortSoiskatel: {self.last_name} {self.first_name[0]}. {self.middle_name[0] if self.middle_name else ''}."

if __name__ == "__main__":
    # Полный объект Soiskatel
    soiskatel1 = Soiskatel(
        last_name = "Иванов",
        first_name = "Иван",
        middle_name = "Иванович",
        qualification="программист",
        profession = "Разработчик",
        date_of_birth = "2000-01-01",
        phone="+7-929-123-4567",
        address="г. Москва, ул. Примерная, д. 1"
    )

    # Краткий объект ShortSoiskatel
    short_soiskatel = ShortSoiskatel("Иванов", "Иван", "Иванович")

    # Сравнение объектов
    print(soiskatel1 == short_soiskatel)  # True

    # Вывод полной и краткой информации
    print(soiskatel1)  # Полная версия объекта
    print(short_soiskatel)  # Краткая версия объекта
