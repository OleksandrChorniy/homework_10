from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name_value):
        self.name = Name(name_value)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if str(phone) != phone_number]

    def edit_phone(self, old_phone_number, new_phone_number):
        for phone in self.phones:
            if str(phone) == old_phone_number:
                phone.value = new_phone_number
                break

    def __str__(self):
        phones_str = ", ".join(str(phone) for phone in self.phones)
        return f"Name: {self.name}, Phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[str(record.name)] = record

    def find_records_by_name(self, name):
        return [record for record in self.data.values() if str(record.name) == name]

    def find_records_by_phone(self, phone):
        return [record for record in self.data.values() if phone in [str(p) for p in record.phones]]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())