from datetime import date, datetime
import re

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
