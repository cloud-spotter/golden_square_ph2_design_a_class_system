from typing import List
from lib.diary_entry import DiaryEntry

class PhoneBook:
    def __init__(self) -> None:
        self.contacts = []

    def find_contact_in_entry(self, entry: DiaryEntry) -> List[str]:
        contact = []
        # Identify entry with contact in from DiaryEntry title format
        if "Rang".lower() in entry.title.lower():
            name = entry.title[5:]
            contact.append(name) # TODO: Change to method that adds 1+ items to list later
            # Locate phone number in DiaryEntry content
            phone_number = ""
            split_contents = entry.contents.split()
            for item in split_contents:
                if len(item) == 11 and item[0] == "0" and item[1] == "7":
                    phone_number += item
            contact.append(phone_number)
        
        return contact
    
    # def add(self, contact: List[str]) -> None:
    #     if 
    #     self.contacts += contact