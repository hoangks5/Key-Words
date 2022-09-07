import yake


with open('text.txt','r',encoding='utf-8') as file:
    doc = file.read()
kw = yake.KeywordExtractor(top = 10, stopwords=None)
keys = kw.extract_keywords(doc)

print(doc)