class DiaryEntry:
    def __init__(self, title: str, contents: str) -> None:
        self.title = title
        self.contents = contents
    
    def count_words(self) -> int:
        words = self.contents.split()
        return len(words)