import re

from nltk.corpus                        import stopwords
from nltk.stem                          import WordNetLemmatizer


def clean_text(text):
    wnl = WordNetLemmatizer()
    text = re.sub("[^a-zA-Z]", " ", text)
    text = text.lower().split()
    text = [wnl.lemmatize(word) for word in text if word not in stopwords.words('english')]
    text = " ".join(text)
    return text
