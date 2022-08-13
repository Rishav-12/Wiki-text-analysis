import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def find_most_frequent_words(text):
    stop_words = set(stopwords.words('english'))
    all_words = [word.lower() for word in word_tokenize(text)]
    meaningful_words = [word for word in all_words if word not in stop_words]
    frequency_distribution = FreqDist(meaningful_words)
    return frequency_distribution.most_common(20)