from datetime import date

class Soiskatel:
    def __init__(self, last_name, first_name, middle_name, qualification, profession, date_of_birth, phone, address):
        # Используем сеттеры для установки значений
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.qualification = qualification
        self.profession = profession
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.address = address

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

