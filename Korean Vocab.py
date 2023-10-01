from konlpy.tag import Okt
import numpy as np

text = open('Merged.txt', encoding="utf8")
text = text.read()
okt = Okt()

#text = "이명함은 디자인이인 상적이서좋다."

trans = np.array(okt.pos(text, norm=True, stem=True, join=False))
trans = np.unique(trans, axis=0)

# Define a dictionary to map English speech categories to Korean
english_to_korean_mapping = {
    'Noun': '명사',
    'Verb': '동사',
    'Adjective': '형용사',
    'Adverb': '부사'
}

# Get the English speech categories
english_speech_categories = set(english_to_korean_mapping.keys())

# Get the Korean speech categories
korean_speech_categories = set(english_to_korean_mapping.values())

# Filter words based on English speech categories
wordList = [word for word, speech in trans if speech in english_speech_categories]

# Connecting to SQL database
import pyodbc
server = "LAPTOP-N520711M\SQLEXPRESS"
database = "KoreanDict"
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; '
                      'SERVER=' + server + '; '
                      'DATABASE=' + database + '; '
                      'Trusted_Connection=yes;')

cursor = cnxn.cursor()

# Function that translates words
def translate(pos):
    unique_entries = set()
    for i in pos:
        cursor.execute("SELECT [Entry], [품사], " 
               "STRING_AGG([DistinctEnglish], '; ') AS [English], "
               "STRING_AGG([English Meaning], '; ') AS [English Meaning] "
               "FROM ( "
               "SELECT [Entry], [품사], [DistinctEnglish], [English Meaning] "
               "FROM ( "
               "SELECT [Entry], [품사], [English] AS [DistinctEnglish], [English Meaning] "
               "FROM [KDPT1] "
               "WHERE [Entry] LIKE ? AND [English] IS NOT NULL AND [English] <> '' "
               "UNION ALL "
               "SELECT [Entry], [품사], [English] AS [DistinctEnglish], [English Meaning] "
               "FROM [KDPT2] "
               "WHERE [Entry] LIKE ? AND [English] IS NOT NULL AND [English] <> '' "
               ") AS mergedSubquery "
               "GROUP BY [Entry], [품사], [DistinctEnglish], [English Meaning] "
               ") AS merged "
               "GROUP BY [Entry], [품사]",
               (i, i))
        
    
        for row in cursor:
                print(row)
                

translate(wordList)
