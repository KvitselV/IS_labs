from datetime import date, datetime
import re
import json

class Soiskatel:
    def __init__(self, last_name, first_name, middle_name, qualification, profession, date_of_birth, phone, address):
        # Используем сеттеры для установки значений
        self.last_name = self.validate_value(last_name, "Last name", is_required=True, only_letters=True)
        self.first_name = self.validate_value(first_name, "First name", is_required=True, only_letters=True)
        self.middle_name = self.validate_value(middle_name, "Middle name", is_required=False, only_letters=True)
        self.qualification = self.validate_value(qualification, "Qualification", is_required=True, only_letters_and_spaces=True)
        self.profession = self.validate_value(profession, "Profession", is_required=True, only_letters_and_spaces=True)
        self.date_of_birth = self.validate_value(date_of_birth, "Date of birth", is_required=True, date_format='%Y-%m-%d')
        self.phone = self.validate_value(phone, "Phone", is_required=True, regex=r'^\+\d{1,3}-\d{3}-\d{3}-\d{4}$')
        self.address = self.validate_value(address, "Address", is_required=True)

    @staticmethod
    def validate_value(value, field_name, is_required=True, only_letters=False, only_letters_and_spaces=False, date_format=None, regex=None):
        """
        Универсальный метод валидации.
        """
        if is_required and not value.strip():
            raise ValueError(f"{field_name} cannot be empty.")
        
        if only_letters and not value.replace(' ', '').isalpha():
            raise ValueError(f"{field_name} must contain only letters.")
        
        if only_letters_and_spaces and not all(char.isalpha() or char.isspace() for char in value):
            raise ValueError(f"{field_name} must contain only letters and spaces.")
        
        if date_format:
            try:
                datetime.strptime(value, date_format)
            except ValueError:
                raise ValueError(f"{field_name} must be in the format {date_format}.")
        
        if regex and not re.match(regex, value):
            raise ValueError(f"{field_name} is invalid. Expected format: {regex}")
        
        return value


    @classmethod
    def from_string(cls, data_string, delimiter=","):
        """
        Создает экземпляр из строки, где значения разделены заданным разделителем.
        """
        fields = data_string.split(delimiter)
        if len(fields) != 8:
            raise ValueError("Data string must contain exactly 8 fields separated by the delimiter.")
        
        validated_fields = [
            cls.validate_value(field.strip(), field_name, **validation_rules)
            for field, (field_name, validation_rules) in zip(fields, [
                ("Last name", {"is_required": True, "only_letters": True}),
                ("First name", {"is_required": True, "only_letters": True}),
                ("Middle name", {"is_required": False, "only_letters": True}),
                ("Qualification", {"is_required": True, "only_letters_and_spaces": True}),
                ("Profession", {"is_required": True, "only_letters_and_spaces": True}),
                ("Date of birth", {"is_required": True, "date_format": "%Y-%m-%d"}),
                ("Phone", {"is_required": True, "regex": r'^\+\d{1,3}-\d{3}-\d{3}-\d{4}$'}),
                ("Address", {"is_required": True}),
            ])
        ]
        
        return cls(*validated_fields)

    @classmethod
    def from_json(cls, json_string):
        """
        Создает экземпляр из JSON-строки.
        """
        try:
            data = json.loads(json_string)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}")
        
        required_keys = [
            ("last_name", "Last name", {"is_required": True, "only_letters": True}),
            ("first_name", "First name", {"is_required": True, "only_letters": True}),
            ("middle_name", "Middle name", {"is_required": False, "only_letters": True}),
            ("qualification", "Qualification", {"is_required": True, "only_letters_and_spaces": True}),
            ("profession", "Profession", {"is_required": True, "only_letters_and_spaces": True}),
            ("date_of_birth", "Date of birth", {"is_required": True, "date_format": "%Y-%m-%d"}),
            ("phone", "Phone", {"is_required": True, "regex": r'^\+\d{1,3}-\d{3}-\d{3}-\d{4}$'}),
            ("address", "Address", {"is_required": True}),
        ]
        
        validated_data = {
            key: cls.validate_value(data.get(key, "").strip(), field_name, **validation_rules)
            for key, field_name, validation_rules in required_keys
        }
        
        return cls(
            last_name=validated_data["last_name"],
            first_name=validated_data["first_name"],
            middle_name=validated_data["middle_name"],
            qualification=validated_data["qualification"],
            profession=validated_data["profession"],
            date_of_birth=validated_data["date_of_birth"],
            phone=validated_data["phone"],
            address=validated_data["address"]
        )

    # Геттеры
    @property
    def last_name(self):
        return self.__last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def middle_name(self):
        return self.__middle_name

    @property
    def qualification(self):
        return self.__qualification

    @property
    def profession(self):
        return self.__profession

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @property
    def phone(self):
        return self.__phone

    @property
    def address(self):
        return self.__address

    # Сеттеры
    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @middle_name.setter
    def middle_name(self, value):
        self.__middle_name = value

    @qualification.setter
    def qualification(self, value):
        self.__qualification = value

    @profession.setter
    def profession(self, value):
        self.__profession = value

    @date_of_birth.setter
    def date_of_birth(self, value):
        self.__date_of_birth = value

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @address.setter
    def address(self, value):
        self.__address = value

