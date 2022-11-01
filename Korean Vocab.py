from konlpy.tag import Okt
from konlpy.utils import pprint
import numpy as np


#text = open('vocab/Merged.txt', encoding="utf8")
#text = text.read()
okt = Okt()


text = "이명함은디자인이인상적이서좋다."
text2 = '이명함은디자인에더신경을써야한다.'

trans = np.array(okt.pos(text, norm=True, stem=True, join=False))
uTrans = np.unique(trans, axis=0)

trans2 = np.array(okt.pos(text, norm=True, stem=True, join=False))
uTrans2 = np.unique(trans2, axis=0)

0
rows = np.where(uTrans[:,1] == 'Noun')
Nouns = uTrans[rows]

rows2 = np.where(uTrans[:,1] == 'Verb')
Verbs = uTrans[rows2]

rows3 = np.where(uTrans[:,1] == 'Adjective')
Adjective = uTrans[rows3]

rows4 = np.where(uTrans[:,1] == 'Adverb')
Adverb = uTrans[rows4]

#second text

Nrows = np.where(uTrans2[:,1] == 'Noun')
nNouns = uTrans2[Nrows]

nrows2 = np.where(uTrans2[:,1] == 'Verb')
nVerbs = uTrans2[nrows2]

nrows3 = np.where(uTrans2[:,1] == 'Adjective')
nAdjective = uTrans2[nrows3]

nrows4 = np.where(uTrans2[:,1] == 'Adverb')
nAdverb = uTrans2[nrows4]


if np.all(nNouns) == np.all(Nouns):
  np.delete(nNouns)


print(Nouns)
print('---')
print(nNouns)


