from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.phone_book import PhoneBook

"""
1. When two DiaryEntry instances are created and added to a Diary instance,
the Diary instance retrieves and returns these in the same order 
"""
def test_diary_integration_return_all_entries():
    diary = Diary()
    diary_entry_1 = DiaryEntry("First Entry", "Dear Diary, it's Monday again.")
    diary_entry_2 = DiaryEntry("Monday Motivation", "'It does not matter how slowly you go as long as you do not stop.' Confucius")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.all() == [diary_entry_1, diary_entry_2]

"""
2. After adding multiple DiaryEntry instances to a Diary, 
Diary's #count_words should return the total word count of all entries
"""
def test_diary_integration_total_word_count():
    diary = Diary()
    diary_entry_1 = DiaryEntry("First Entry", "Dear Diary, it's Monday.")
    diary_entry_2 = DiaryEntry("Monday Motivation", "'It does not matter how slowly you go as long as you do not stop.' Confucius")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.count_words() == 20

"""
3. Given a Diary with multiple entries, Diary's #reading_time should
return the correct total reading time based on the provided WPM
"""
def test_diary_integration_calculate_reading_time():
    diary = Diary()
    diary.add(DiaryEntry("First Entry", "Dear Diary, it's Monday."))
    diary.add(DiaryEntry("Monday Motivation", "'It does not matter how slowly you go as long as you do not stop.' Confucius"))
    diary.add(DiaryEntry("Tuesday Motivation", "'Quality is not an act. It is a habit.' Aristotle"))
    
    wpm = 10
    expected_reading_time = 3
    assert diary.reading_time(wpm) == expected_reading_time

"""
4. Given a Diary instance with multiple diary entries
Diary finds the best entry to read for a given time frame
"""
def test_diary_integration_find_best_entry_for_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("First Entry", "Dear Diary, it's Monday.")
    diary_entry_2 = DiaryEntry("Monday Motivation", "'It does not matter how slowly you go as long as you do not stop.' Confucius")
    diary.add(diary_entry_1) 
    diary.add(diary_entry_2)

    minutes = 1
    wpm = 10
    best_entry = diary.find_best_entry_for_reading_time(wpm, minutes)
    assert best_entry == diary_entry_1

"""
5. After adding contacts to the PhoneBook, 
#all should return all the contacts correctly
"""
def test_phone_book_integration_add_and_return_contacts():
    phone_book = PhoneBook()
    diary_entry_1 = DiaryEntry("Rang Jo", "Tuesday lunch: Jo rang and left her new number (07000000003).")
    diary_entry_2 = DiaryEntry("Tuesday Entry", "Some content")
    diary_entry_3 = DiaryEntry("Rang Max", "Max is on 07000000004 now.")
    phone_book.add(diary_entry_1.get_phone_number())
    phone_book.add(diary_entry_2.get_phone_number())
    phone_book.add(diary_entry_3.get_phone_number())
    
    assert phone_book.all() == [["Jo", "07000000003"], ["Max", "07000000004"]]

