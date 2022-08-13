from wordcloud import WordCloud, STOPWORDS

def make_wordcloud(text):
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width=400, height=400, background_color='white', stopwords=stopwords, min_font_size=10).generate(text)
    return wordcloud
