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
    
    def reading_time(self, wpm: int) -> int:
        '''Returns an integer representing an estimate of the reading
        time in minutes, if the user were to read all diary entries'''
        return self.count_words() / wpm
    
    def find_best_entry_for_reading_time(self, wpm: int, minutes: int):
        '''Returns an instance of DiaryEntry representing the entry that
        is closest to, but not over, the length that the user could read
        in the minutes they have available given their reading speed.'''
        word_limit = wpm * minutes
        sorted_entries = sorted(self.entries, key=lambda entry: entry.count_words(), reverse=True)
        # Include reverse=True in sorted method to catch any entry equal to word_limit first
        for entry in sorted_entries:
            if entry.count_words() <= word_limit:
                return entry
        