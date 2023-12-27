from typing import List
from lib.diary_entry import DiaryEntry

class PhoneBook:
    def __init__(self) -> None:
        self.contacts = []

    def add(self, contact: List[str]) -> None:
        if contact:   # (contact is from DiaryEntry's #get_phone_number method)
            self.contacts.append(contact)
    
    def all(self) -> List[List[str]]:
        return self.contacts