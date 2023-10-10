import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {
        'id': 0,
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'first_sentence': 'The coldsleep itself was dreamless.',
        'year_published': '1992'
    },
    {
        'id': 1,
        'title': 'The Ones Who Walk Away From Omelas',
        'author': 'Ursula K. Le Guin',
        'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
        'published': '1973'
    },
    {
        'id': 2,
        'title': 'Dhalgren',
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the autumnal city.',
        'published': '1975'
    }
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello World!</h1>"


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    id = request.args.get('id')
    print(id)
    if id:
        id = int(id)
    else:
        return "Error: No id field provided. Please specify an id."
    results = []
    for book in books:
        if book['id'] == id:
            results.append(book)
    return jsonify(results)


@app.route('/api/v1/resources/books/new', methods=['POST'])
def api_new():
    print(request.json)
    if request.json:
        books.append(request.json)
        return jsonify(books)
    else:
        return "Error: No json provided. Please specify a json."


if __name__ == '__main__':
    app.run()
