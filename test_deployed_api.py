import json
import requests
from numpy.random import randint


def test_text_readability_scoring():
    x_test = pd.read_csv('test.csv')
    rand_text_ind = randint(0, len(x_test))
    rand_text = x_test.excerpt.loc[rand_text_ind]

    url = 'https://lit-taiga-89750.herokuapp.com/get_text_readability'
    params = {'text' : str(rand_text)}
    result = requests.get(url, params=params)
    result = result.json()

    print(f'Provided text : {rand_text}')
    print('-'*110)
    print(f'Readability score = {result["readability_score"]}')


if __name__ == '__main__':
    test_text_readability_scoring()