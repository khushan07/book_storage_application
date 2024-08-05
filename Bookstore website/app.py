from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# In-memory book data (replace with database in production)
books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1', 'year': '2020', 'genre': 'Fiction', 'read_status': 'read', 'photo_url': 'https://via.placeholder.com/80'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2', 'year': '2021', 'genre': 'Non-Fiction', 'read_status': 'unread', 'photo_url': 'https://via.placeholder.com/80'}
]

@app.route('/')
def home():
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        year = request.form.get('year')
        genre = request.form.get('genre')
        read_status = request.form.get('read_status')
        photo_url = request.form.get('photo_url')
        
        new_id = max(book['id'] for book in books) + 1 if books else 1
        new_book = {
            'id': new_id,
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'read_status': read_status,
            'photo_url': photo_url
        }
        books.append(new_book)
        return redirect(url_for('home'))
    
    return render_template('add_book.html')

@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if not book:
        return redirect(url_for('home'))

    if request.method == 'POST':
        book['title'] = request.form.get('title')
        book['author'] = request.form.get('author')
        book['year'] = request.form.get('year')
        book['genre'] = request.form.get('genre')
        book['read_status'] = request.form.get('read_status')
        book['photo_url'] = request.form.get('photo_url')
        return redirect(url_for('home'))
    
    return render_template('edit_book.html', book=book)

@app.route('/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
