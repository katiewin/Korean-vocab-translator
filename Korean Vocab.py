from konlpy.tag import Okt
import numpy as np


text = open('Merged.txt', encoding="utf8")
text = text.read()
okt = Okt()

#text = "이명함은 디자인이인 상적이서좋다."
text = text.strip().replace(' ','')

trans = np.array(okt.pos(text, norm=True, stem=True, join=False))
trans = np.unique(trans, axis=0)


#only using words in compareSpeech list
compareSpeech = ['Noun', 'Verb', 'Adjective', 'Adverb']
wordList = []

for speech in compareSpeech:
  for compare in trans:
    if speech == compare[1]:
      wordList.append(compare[0])


#Connecting to SQL database
import pyodbc
server = "LAPTOP-N520711M\SQLEXPRESS"
database = "KoreanDict"
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                        SERVER=' + server + '; \
                        DATABASE=' + database +';\
                        Trusted_Connection=yes;')

cursor = cnxn.cursor()

#function that translates words

def translate(pos):
  for i in pos:
    cursor.execute("SELECT KDPT1.Entry, KDPT1.English, KDPT1.English Meaning FROM KDPT1 WHERE KDPT1.Entry LIKE (?) \
          UNION ALL \
            SELECT KDPT2.Entry, KDPT2.English, KDPT2.English Meaning FROM KDPT2 WHERE KDPT2.Entry LIKE (?)", (i, i))     
    for row in cursor:
      print(row)
      
translate(wordList)    
