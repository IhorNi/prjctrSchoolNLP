import nltk
import pickle
import pandas as pd
import numpy as np

from flask                              import Flask
from flask_restful                      import Resource, Api, reqparse
from helper.text_helpers                import clean_text

VECTORIZER = 'nlp_models/text_vectorizer.sav'
MODEL = 'nlp_models/any_model_nlp_model.sav'

app = Flask(__name__)
api = Api(app)

get_parser = reqparse.RequestParser()
get_parser.add_argument('text')


class Base(Resource):

    def get(self):
        return 'Hello World!'


class TextReadability(Resource):

    def __init__(self):
        # nltk.download('stopwords')
        # nltk.download('wordnet')
        self.loaded_vectorizer = pickle.load(open(VECTORIZER, 'rb'))
        self.loaded_model = pickle.load(open(MODEL, 'rb'))

    def get_readability_score(self, text):
        # make text a super simple dataframe to utilize existing flow
        text = pd.DataFrame([text], columns=['excerpt'])
        # text preprocessing
        text['excerpt'] = text['excerpt'].apply(lambda x: clean_text(x))
        # text vectorization
        text = self.loaded_vectorizer.transform(text['excerpt'])
        # return forecast
        return np.round(self.loaded_model.predict(text)[0], 3)

    def get(self):
        args = get_parser.parse_args()
        if args['text']:
            read_score = self.get_readability_score(args['text'])
            return {'readability_score': read_score}
        else:
            return {'error': 'No text for readability scoring provided'}


api.add_resource(Base, '/')
api.add_resource(TextReadability, '/get_text_readability')


if __name__ == '__main__':
    app.run()