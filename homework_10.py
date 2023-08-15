from collections import UserDict

class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name_value, *phones):
        self.name = Name(name_value)
        self.phones = [Phone(phone) for phone in phones]

    def add_phone(self, phone_value):
        phone = Phone(phone_value)
        self.phones.append(phone)

    def remove_phone(self, phone_value):
        self.phones = [phone for phone in self.phones if phone.value != phone_value]

    def edit_phone(self, old_value, new_value):
        for phone in self.phones:
            if phone.value == old_value:
                phone.value = new_value

    def __str__(self):
        phones_str = ', '.join(str(phone.value) for phone in self.phones)
        return f"Name: {self.name.value}, Phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

    def __getitem__(self, key):
        return self.data[key]

if __name__ == "__main__":
    name = 'Bill'
    phone = '1234567890'
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    for key, value in ab.items():
        print(f"{key}: {value}")
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')