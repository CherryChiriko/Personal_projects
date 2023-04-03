from tokenize import String
import pandas as pd
import nltk
from nltk import word_tokenize,sent_tokenize

article = pd.read_csv('C:\\Users\\HP\\Desktop\\Projects\\Personal_projects\\NLP\\TedTalk.txt', sep="&")
print(article)
tokens = word_tokenize(article)
print(tokens[:10])
# sentences = nltk.sent_tokenize(article.columns)
# token_sentences = [nltk.word_tokenize(sent) for sent in sentences]
# pos_sentences = [nltk.pos_tag(sent) for sent in token_sentences] 
# print(sentences)