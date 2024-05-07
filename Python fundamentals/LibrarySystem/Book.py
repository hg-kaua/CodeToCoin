class Book:
    def __init__(self, title, author, publication_year, status):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.status = status

    def UptadeStatus(self):
        situation = self.status.upper()
        
        if situation == 'AVAIBLE':
            self.status = 'Borroed'
        else:
            self.status = 'Avaible'

if __name__ == '__main__':
    
    book1 = Book('The amazing Spider-Man', 'stan lee', 1990, 'Avaible')
    
    print(f'Book title: {book1.title}')
    print(f'Current book situation: {book1.status}')
    
    book1.UptadeStatus()
    
    print(f'Current book situation: {book1.status}')
    
    book1.UptadeStatus()
    

    print(f'Current book situation: {book1.status}')