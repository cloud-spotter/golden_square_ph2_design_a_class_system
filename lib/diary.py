from typing import List
from lib.diary_entry import DiaryEntry

class Diary:
    def __init__(self) -> None:
        self.entries = []

    def add(self, entry: DiaryEntry) -> None:
        '''Adds an instance of DiaryEntry to the list of entries'''
        self.entries.append(entry)

    def all(self) -> List[str]:
        '''Returns a list of instances of DiaryEntry'''
        return self.entries