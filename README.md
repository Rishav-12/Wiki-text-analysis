# Wiki-text-analysis

Analysing the text of Wikipedia articles

Created at the Wikimania 2022 Hackathon

## Install and Run locally

```bash
git clone https://github.com/Rishav-12/Wiki-text-analysis.git
cd Wiki-text-analysis
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

streamlit run main.py
```

## Description

Pulls the text of a Wikipedia article and does some analysis with the text
- displays the most common words
- generates and displays a wordcloud

## License
[MIT](https://choosealicense.com/licenses/mit/)
