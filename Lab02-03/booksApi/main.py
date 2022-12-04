from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

client = MongoClient('localhost', 27017)
db = client['library']
books_collection = db['books']


@app.route('/api/books', methods=['POST'])
def new_book():
    raw_book = request.get_json()
    status = books_collection.insert_one(raw_book)
    if status:
        return jsonify({
            "success": True
        })
    return jsonify({
        "error": "database error"
    })


@app.route('/api/book/<string:_id>', methods=['GET'])
def get_book_by_id(_id):
    book = books_collection.find_one({"_id": ObjectId(_id)})
    if book:
        book['_id'] = str(_id)
        return jsonify(book)
    return jsonify({
        "error": "book not found"
    })


@app.route('/api/books', methods=['GET'])
def get_books():
    books = books_collection.find()
    json_books = []
    for book in books:
        book['_id'] = str(book['_id'])
        json_books.append(book)

    return json_books


@app.route('/api/books', methods=['DELETE'])
def delete_all_books():
    status = books_collection.delete_many({})
    if status:
        return jsonify({
            "success": True
        })
    return jsonify({
        "success": False
    })


@app.route('/api/book/<string:_id>', methods=['DELETE'])
def delete_book_by_id(_id):
    status = books_collection.delete_one({"_id": ObjectId(_id)})
    if status:
        return jsonify({
            "success": True
        })
    return jsonify({
        "success": False
    })


@app.route('/api/book/<string:_id>', methods=['PUT'])
def update_book_by_id(_id):
    book = request.get_json()
    status = books_collection.find_one_and_update({"_id": ObjectId(_id)}, {"$set": book})

    if status:
        return jsonify({
            "success": True
        })
    return jsonify({
        "error": "book not found"
    })


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0'
    )
