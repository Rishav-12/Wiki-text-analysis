import wikipedia
import matplotlib.pyplot as plt

from make_wordcloud import make_wordcloud
from most_frequent_words import find_most_frequent_words

term = input("Enter a term to look up: ")
result = wikipedia.search(term, results=1)[0]
page = wikipedia.page(result)
print(f"Wordcloud for the Wikipedia page {page.title}")
content = page.content

frequent_words = find_most_frequent_words(content)

for i in frequent_words:
    if i[0].isalnum():
        print(f"{i[0]}: {i[1]}")

wordcloud = make_wordcloud(content)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
