class Contact:

    def __init__(self, number, last_name, first_name):
        self.__number = number
        self.__first_name = first_name
        self.__last_name = last_name

    def get_number(self):
        return self.__number

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

class UnknownContact(Contact):

    def __init__(self, number):
        super().__init__(number, "unknown", "unknown")

class Event:

    def __init__(self, contact, time, event_type):
        self.__contact = contact
        self.__time = time
        self.__type = event_type

    def get_info(self):
        return self.__contact, self.__time, self.__type

class PhoneBook:

    def __init__(self):
        self.__repo = {}

    # def add_contact(self, number, first_name, last_name):
    #     self.__repo[number] = Contact(number, first_name, last_name)

    # def update_contact(self, number, first_name, last_name):
    #     if number in self.__repo:
    #         self.add_contact(number, first_name, last_name)

    def add_or_update_contact(self, number, first_name, last_name):
        self.__repo[number] = Contact(number, first_name, last_name)

    def find_contact(self, number):
        if number in self.__repo:
            return self.__repo[number]
        
        return False

    def remove_contact(self, number):
        if number in self.__repo:
            del self.__repo[number]
            return True
        
        return False


class Journal:

    def __init__(self):
        self.__repo = []

    def add_event(self, contact, time, event_type):
        self.__repo.append(Event(contact, time, event_type))

    def read_events_by_number(self, number):
        current_events = []
        
        for i in self.__repo:
            if i.get_info()[0] == number:
                current_events.append(i)

        return current_events

    def read_events_by_time(self, time):
        current_events = []
        
        for i in self.__repo:
            if i.get_info()[1] == time:
                current_events.append(i)

        return current_events


# book = PhoneBook()
# book.add_or_update_contact(786478684, "first", "last")

e = Event(UnknownContact(254676576), '13:44', "call")
info = e.get_info()
print(info[1])