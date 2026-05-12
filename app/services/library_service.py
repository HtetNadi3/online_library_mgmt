from app.models.book import Book
from app import db

class LibraryService:
    @staticmethod
    def get_all_books():
        return Book.query.all()

    @staticmethod
    def add_book(title, author, isbn, cover_image):
        new_book = Book(title=title, author=author, isbn=isbn, cover_image=cover_image)
        db.session.add(new_book)
        db.session.commit()

    @staticmethod
    def get_book(book_id):
        return Book.query.get(book_id)

    @staticmethod
    def update_book(book_id, title=None, author=None, isbn=None, cover_image=None):
        book = Book.query.get(book_id)
        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            if isbn:
                book.isbn = isbn
            if cover_image:
                book.cover_image = cover_image
            db.session.commit()
            return True
        return False

    @staticmethod
    def delete_book(book_id):
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def update_book(book_id, title, author, isbn, cover_image=None):
        book = Book.query.get(book_id)
        if book:
            book.title = title
            book.author = author
            book.isbn = isbn
            if cover_image:
                book.cover_image = cover_image
            db.session.commit()
            return True
        return False
        
    @staticmethod
    def search_books(query):
        return Book.query.filter(
            (Book.title.ilike(f'%{query}%')) |
            (Book.author.ilike(f'%{query}%')) |
            (Book.isbn.ilike(f'%{query}%'))
        ).all()
    
    @staticmethod
    def borrow_book(book_id):
        book = Book.query.get(book_id)
        if book:
            book.is_available = False
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def return_book(book_id):
        book = Book.query.get(book_id)
        if book:
            book.is_available = True
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_available_books():
        return Book.query.filter_by(is_available=True).all()
    
    @staticmethod
    def get_borrowed_books():
        return Book.query.filter_by(is_available=False).all()
    
