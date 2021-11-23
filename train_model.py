import os
import re
import pickle
import pandas as pd
import numpy as np

from nltk.corpus                        import stopwords
from nltk.stem                          import WordNetLemmatizer
from helper.text_helpers                import clean_text

from sklearn.linear_model               import Ridge
from sklearn.model_selection            import train_test_split
from sklearn.feature_extraction.text    import TfidfVectorizer
from sklearn.metrics                    import mean_squared_error

# nltk==3.6.1
# import nltk
# nltk.download('stopwords')
# nltk.download('wordnet')


def train_model():

    # Load data
    x_train = pd.read_csv('data/train.csv')
    print('Data has been loaded')
    # Basic text preprocessing before building model
    x_train['excerpt'] = x_train['excerpt'].apply(lambda x : clean_text(x))
    print('Data has been cleaned')
    X_train, X_test, y_train, y_test = train_test_split(x_train.excerpt, x_train.target, test_size=0.3,
                                                        random_state=42, shuffle=True)

    tfidf = TfidfVectorizer(binary=True)
    vect = tfidf.fit(X_train)
    X_train = vect.transform(X_train)
    X_test = vect.transform(X_test)
    print('Data has been vectorized')

    model_rr = Ridge().fit(X_train, y_train)
    y_pred = model_rr.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model Name: Ridge Regression ====>>> RMSE:{np.round(np.sqrt(mse), 3)}")

    filename = 'nlp_models/text_vectorizer.sav'
    pickle.dump(tfidf, open(filename, 'wb'))

    filename = 'nlp_models/any_model_nlp_model.sav'
    pickle.dump(model_rr, open(filename, 'wb'))


if __name__ == '__main__':
    train_model()


