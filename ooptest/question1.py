

class Resource:
    def __init__(self, call_id, title,borrowed):
        self.call_id = call_id
        self.title = title
        self.borrowed = False

    def borrow(self):
        self.borrowed = True

    def return_(self):
        self.borrowed = False

class Book(Resource):
    def __init__(self, call_id, title, author,borrowed):
        super().__init__(call_id, title,borrowed)
        self.author = author

class Journal(Resource):
    def __init__(self, call_id, title, issue,borrowed):
        super().__init__(call_id, title,borrowed)
        self.issue = issue



# driver class
class Library:
    def __init__(self):
        self.books = []
        self.journals = []

    def borrow_book(self, call_id):
        for book in self.books:
            if book.call_id == call_id:
                if not book.borrowed:
                    book.borrow()
                    print("Book borrowed successfully.")
                    return
                else:
                    print("Book is already borrowed.")
                    return
        print("Book not found.")

    def return_book(self, call_id):
        for book in self.books:
            if book.call_id == call_id:
                if book.borrowed:
                    book.return_()
                    print("Book returned successfully.")
                    return
                else:
                    print("Book is already returned.")
                    return
        print("Book not found.")

    def borrow_journal(self, call_id):
        for journal in self.journals:
            if journal.call_id == call_id:
                if not journal.borrowed:
                    journal.borrow()
                    print("Journal borrowed successfully.")
                    return
                else:
                    print("Journal is already borrowed.")
                    return
        print("Journal not found.")

    def return_journal(self, call_id):
        for journal in self.journals:
            if journal.call_id == call_id:
                if journal.borrowed:
                    journal.return_()
                    print("Journal returned successfully.")
                    return
                else:
                    print("Journal is already returned.")
                    return
        print("Journal not found.")

# Call the functions
library = Library()

book1 = Book("QA76.1", "Eclid's geometry", "J.R.R. Tolkien","not Library")
book2 = Book("QA73.2", "ACM transactions", "J.R.R. Tolkien","in library")
journal1 = Journal("QA73", "Nature", "march 2006","in lirary")
journal2 = Journal("J4567", "Science", "october 2000","not in library")

print(book1.__dict__)
print(book2.__dict__)
print(journal1.__dict__)
print(journal2.__dict__)


    
