class Book:
    def __init__(self,name, author, price, publish_year):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_publish_year = publish_year
        
    def add_book(self):
        print("Name: " + self.book_name)
        print("Author: " + str(self.book_author))
        print("Price: " + self.book_price)
        print("Publish Year: " + self.book_publish_year)
        print("Book Added")


book1 = Book("Harry Potter and The Philosopher's Stone","J.K. Rowling","$19.28", "1997")
book1.add_book()

book2 = Book("Diary of A Wimpy Kid","Jeff Kinney","$7.00", "2017")
book2.add_book()