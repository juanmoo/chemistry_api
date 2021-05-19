from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from dotenv import load_dotenv
from os import environ
from pathlib import Path
from random import shuffle
import json
import os
from extract import get_ents

# App Setup
app = Flask(__name__)
CORS(app)
api = Api(app)


class Extractor(Resource):
    def post(self):

        if request.is_json:
            data = request.json
        else:
            return {
                'error': "Please format paragraphs to be extracted in a JSON object."
            }

        paragraphs = data.get('paragraphs', [])
        extractions = get_ents(paragraphs)

        return {
            'extractions': extractions
        }


api.add_resource(Extractor, '/extract')


if __name__ == '__main__':

    print('Starting up server ...')

    # Load configuration file
    config_path = os.path.join(os.path.realpath('.'), '.env')

    load_dotenv(dotenv_path=config_path)
    port = environ.get('PORT')

    app.run(debug=True, host='0.0.0.0', port=port)
