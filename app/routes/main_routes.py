from flask import Blueprint, abort, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.services.library_service import LibraryService

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    search_query = request.args.get('search', '')
    books = LibraryService.search_books(search_query)
    return render_template('user_cards.html', books=books, search_query=search_query)

@main_bp.route('/admin')
@login_required
def index():
    books = LibraryService.get_all_books()
    return render_template('index.html', books=books)

@main_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        cover_image = request.files['cover_image']
        LibraryService.add_book(title, author, isbn, cover_image)
        return redirect(url_for('main.index'))
    return render_template('add_book.html')

@main_bp.route('/delete/<int:book_id>')
@login_required
def delete_book(book_id):
    
    if current_user.role != 'admin': abort(403)  # Only admins can delete books
    LibraryService.delete_book(book_id)
    return redirect(url_for('main.index'))

@main_bp.route('/update/<int:book_id>', methods=['GET', 'POST'])
@login_required
def update_book(book_id):
    book = LibraryService.get_book(book_id)
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        cover_image = request.files['cover_image']
        LibraryService.update_book(book_id, title, author, isbn, cover_image)
        return redirect(url_for('main.index'))
    return render_template('update_book.html', book=book)

