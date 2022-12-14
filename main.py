import streamlit as st
import wikipedia
import matplotlib.pyplot as plt

from make_wordcloud import make_wordcloud
from most_frequent_words import find_most_frequent_words

st.write("""
# Wikipedia article text analysis
""")

term = st.text_input("Enter a term to look up: ")
if term == "":
    st.info("Please enter a valid search term!")
else:
    result = wikipedia.search(term, results=1)[0]
    page = wikipedia.page(result)

    freq_words_subheading = f"Most common words in the Wikipedia article {page.title}"
    st.write(freq_words_subheading)
    content = page.content

    frequent_words = find_most_frequent_words(content)

    words_to_display = ""

    for i in frequent_words:
        if i[0].isalnum():
            words_to_display += f"- {i[0]}: {i[1]}\n"

    st.markdown(words_to_display)

    wordcloud_subheading = f"Wordcloud for the Wikipedia article {page.title}"
    st.write(wordcloud_subheading)
    wordcloud = make_wordcloud(content)
    fig = plt.figure(figsize=(30, 30))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.tight_layout(pad=0)

    st.pyplot(fig)
