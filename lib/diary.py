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
    
    def count_words(self) -> int:
        '''Returns an integer representing the number of words in all diary entries'''
        word_count = 0
        for entry in self.entries:
            word_count += entry.count_words()
        return word_count