from flask import render_template, request, redirect
from app import app
from models.books_list import books
from models.book import Book


@app.route('/books')
def index():
    return render_template('index.html', title = "Home", books=books)

@app.route('/books/<index>')
def book(index):
    return render_template('book.html', title="Book", books= books, index=int(index))

@app.route('/books', methods=['POST'])
def add_book():
  title = request.form['title']
  author = request.form['author']
  genre = request.form['genre']

  new_book = Book(title=title, author=author, genre=genre)

  books.append(new_book)
  return redirect('/books')

@app.route('/books/delete/<index>', methods=['POST'])
def delete_book(index):
    books.pop(int(index))
    return redirect('/books')



