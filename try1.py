class Resource:
    def _init_(self, callId, title): 
        self.callId = callId
        self.title = title
        self.is_borrowed = False   

    def summary(self):
        status = "in library" if not self.is_borrowed else "not in library"  
        return f"Call ID: {self.callId}\n    Title: {self.title}\n    {status}"

    def borrowed(self):
        self.is_borrowed = True     

    def returned(self):
        self.is_borrowed = False 


class Book(Resource):
    def _init_(self, callId, title, author):
        super()._init_(callId, title) 
        self.author = author

    def summary(self):
        status = "in library" if not self.is_borrowed else "not in library"
        return f"Call ID: {self.callId}\n    Title: {self.title}\n    Author: {self.author}\n    {status}"


class Journal(Resource):
    def _init_(self, callId, title, issue):
        super()._init_(callId, title)
        self.issue = issue

    def summary(self):
        status = "in library" if not self.is_borrowed else "not in library"
        return f"Call ID: {self.callId}\n    Title: {self.title}\n    Issue: {self.issue}\n    {status}"


class Library:
    def _init_(self):
        self.resources = []

    def add_resource(self, resource):
        self.resources.append(resource)

    def display_library(self):
        for resource in self.resources:
            print(resource.summary())


library = Library()

book1 = Book("QA76.1", "Euclid's Geometry", "Euclid")
book2 = Journal("QA73.2", "ACM Transactions", "March 2007")
book3 = Book("QA73.3", "Origin of the Species", "Charles Darwin")

library.add_resource(book1)
library.add_resource(book2)
library.add_resource(book3)

book2.borrowed()

library.display_library()