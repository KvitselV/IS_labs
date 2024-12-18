from datetime import date, datetime
import re

class Soiskatel:
    def __init__(self, last_name, first_name, middle_name, qualification, profession, date_of_birth, phone, address):
        # Используем сеттеры для установки значений
        self.last_name = self.validate_last_name(last_name)
        self.first_name = self.validate_first_name(first_name)
        self.middle_name = self.validate_middle_name(middle_name)
        self.qualification = self.validate_qualification(qualification)
        self.profession = self.validate_profession(profession)
        self.date_of_birth = self.validate_date_of_birth(date_of_birth)
        self.phone = self.validate_phone(phone)
        self.address = self.validate_address(address)

    # Валидация фамилии
    @staticmethod
    def validate_last_name(value):
        if not value.strip():
            raise ValueError("Last name cannot be empty.")
        if not value.isalpha():
            raise ValueError("Last name must contain only letters.")
        return value

    # Валидация имени
    @staticmethod
    def validate_first_name(value):
        if not value.strip():
            raise ValueError("First name cannot be empty.")
        if not value.isalpha():
            raise ValueError("First name must contain only letters.")
        return value

    # Валидация отчества
    @staticmethod
    def validate_middle_name(value):
        if value.strip() and not value.isalpha():
            raise ValueError("Middle name must contain only letters if provided.")
        return value
    
    # Валидация квалификации
    @staticmethod
    def validate_qualification(value):
        if not value.strip():
            raise ValueError("Qualification cannot be empty.")
        if not value.replace(' ', '').isalpha():
            raise ValueError("Qualification must contain only letters and spaces.")
        return value
    
    # Валидация профессии
    @staticmethod
    def validate_profession(value):
        if not value.strip():
            raise ValueError("Profession cannot be empty.")
        if not value.replace(' ', '').isalpha():
            raise ValueError("Profession must contain only letters and spaces.")
        return value
    
    # Валидация даты рождения
    @staticmethod
    def validate_date_of_birth(value):
        if not value.strip():
            raise ValueError("Date of birth cannot be empty.")
        try:
            datetime.strptime(value, '%Y-%m-%d')  # Формат: YYYY-MM-DD
        except ValueError:
            raise ValueError("Date of birth must be in the format YYYY-MM-DD.")
        return value
    
    # Валидация номера телефона
    @staticmethod
    def validate_phone(value):
        if not value.strip():
            raise ValueError("Phone number cannot be empty.")
        if not re.match(r'^\+\d{1,3}-\d{3}-\d{3}-\d{4}$', value):
            raise ValueError("Phone number must be in the format +XXX-XXX-XXX-XXXX.")
        return value
    
    # Валидация адреса
    @staticmethod
    def validate_address(value):
        if not value.strip():
            raise ValueError("Address cannot be empty.")
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
