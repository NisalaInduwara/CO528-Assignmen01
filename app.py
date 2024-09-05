from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database
books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]

# Retrieve all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Retrieve a book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book is None:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify(book)

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.json
    books.append(new_book)
    return jsonify(new_book), 201

# Update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book is None:
        return jsonify({'message': 'Book not found'}), 404
    book.update(request.json)
    return jsonify(book)

# Delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({'message': 'Book deleted'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

