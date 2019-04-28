from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, jsonify, request, abort
import logging


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
# TODO delete CORS wrapper for production setup
# TODO set image env var CORS_ENABLED or smth
CORS(app)

def validate_advice(advice, tags = []):
    assert 0 < len(advice) < 100, 'Incorrect Advice title length (symbol amount should be between 1 and 100)'
    assert len(tags) < 4, 'Advice tags should be no more than 3'

# Fake advice list
ADVICES = [
    {
        'title': 'Green beer its just marketing',
        'author': 'vnaumov',
        'verified': True,
        'tags': ['Prague', 'Europe']
    },
    {
        'title': 'Lidl have more alcohol discounts that Albert, Billa have more interesting products, but prices shit',
        'author': 'vnaumov',
        'verified': False,
        'tags': ['Prague', 'Europe', 'Germany']
    },
    {
        'title': 'Do not smoke weed and drink simultaneously',
        'author': 'vnaumov',
        'verified': True,
        'tags': ['Europe', 'Weed']
    }
]

# sanity check route
@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify('Bullseye watching your advice')

@app.route('/advices', methods=['GET', 'POST'])
def all_advices():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()

        adv = post_data.get('title','')
        adv_tags = post_data.get('tags',[])
        try:
            validate_advice(adv, adv_tags)
        except AssertionError as e:
            logging.error(e)
            abort(400, e)

        ADVICES.append({
            'title': adv,
            'author': post_data.get('author', 'Anonymous'),
            'tags': adv_tags,
            'read': post_data.get('verified', False)
        })
        response_object['message'] = 'Advice added!'
    else:
        response_object['advices'] = ADVICES

    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
