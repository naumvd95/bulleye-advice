from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
# TODO delete CORS wrapper for production setup
# TODO set image env var CORS_ENABLED or smth
CORS(app)

# sanity check route
@app.route('/healthcheck', methods=['GET'])
def ping_pong():
    return jsonify('Bullseye server alive')

if __name__ == '__main__':
    app.run()
