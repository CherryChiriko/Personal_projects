import pandas as pd
from nltk import word_tokenize,sent_tokenize

path = r"C:\Users\HP\Desktop\Projects\Personal_projects\NLP\document.txt"
raw = pd.read_csv(path)
print(raw.columns[0])
words=[]
for n in range(10):
    try: words.append(word_tokenize(raw.columns[n]))
    except IndexError: break
print(words)
# tokens = sent_tokenize(raw)