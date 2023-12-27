from typing import List

class DiaryEntry:
    def __init__(self, title: str, contents: str) -> None:
        self.title = title
        self.contents = contents
    
    def count_words(self) -> int:
        words = self.contents.split()
        return len(words)
    
    def get_phone_number(self) -> List[str]:
        contact = []
        # Identify entry with contact in from DiaryEntry title format
        if "Rang".lower() in self.title.lower():
            name = self.title[5:]
            contact.append(name) # TODO: Change to method that adds 1+ items to list later
            # Locate phone number in DiaryEntry content
            phone_number = ""
            split_contents = self.contents.split()
            for item in split_contents:
                if len(item) == 11 and item[0] == "0" and item[1] == "7":
                    phone_number += item
            contact.append(phone_number)
        
        return contact