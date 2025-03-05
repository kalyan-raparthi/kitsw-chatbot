# import urllib.request
# data_url = 'https://www.gutenberg.org/cache/epub/2554/pg2554.txt'
# t = urllib.request.urlopen(data_url).read().decode('utf-8')

import re
import spacy
nlp = spacy.load("en_core_web_sm")

t = '''
Though neither by temperament nor conviction a revolutionist, Dostoevsky
was one of a little group of young men who met together to read Fourier
and Proudhon. He was accused of “taking part in conversations against
the censorship, of reading a letter from Byelinsky to Gogol, and of
knowing of the intention to set up a printing press.” Under Nicholas
I. (that “stern and just man,” as Maurice Baring calls him) this was
enough, and he was condemned to death. After eight months’ imprisonment
he was with twenty-one others taken out to the Semyonovsky Square to
be shot. Writing to his brother Mihail, Dostoevsky says: “They snapped
words over our heads, and they made us put on the white shirts worn by
persons condemned to death. Thereupon we were bound in threes to stakes,
to suffer execution. Being the third in the row, I concluded I had only
a few minutes of life before me. I thought of you and your dear ones and
I contrived to kiss Plestcheiev and Dourov, who were next to me, and to
bid them farewell. Suddenly the troops beat a tattoo, we were unbound,
brought back upon the scaffold, and informed that his Majesty had spared
us our lives.” The sentence was commuted to hard labour.

One of the prisoners, Grigoryev, went mad as soon as he was untied, and
never regained his sanity.

The intense suffering of this experience left a lasting stamp on
Dostoevsky’s mind. Though his religious temper led him in the end to
accept every suffering with resignation and to regard it as a blessing
in his own case, he constantly recurs to the subject in his writings.
He describes the awful agony of the condemned man and insists on the
cruelty of inflicting such torture. Then followed four years of penal
servitude, spent in the company of common criminals in Siberia, where
he began the “Dead House,” and some years of service in a disciplinary
battalion.

He had shown signs of some obscure nervous disease before his arrest
and this now developed into violent attacks of epilepsy, from which he
suffered for the rest of his life. The fits occurred three or four times
a year and were more frequent in periods of great strain. In 1859 he was
allowed to return to Russia. He started a journal--“Vremya,” which was
forbidden by the Censorship through a misunderstanding. In 1864 he lost
his first wife and his brother Mihail. He was in terrible poverty, yet
he took upon himself the payment of his brother’s debts. He started
another journal--“The Epoch,” which within a few months was also
prohibited. He was weighed down by debt, his brother’s family was
dependent on him, he was forced to write at heart-breaking speed, and is
said never to have corrected his work. The later years of his life were
much softened by the tenderness and devotion of his second wife.

In June 1880 he made his famous speech at the unveiling of the
monument to Pushkin in Moscow and he was received with extraordinary
demonstrations of love and honour.'''
# print(t)


def clean_text(text):
    text = text.lower()
    text = text.replace("\n", " ")
    text = re.sub(r"[^a-z ]", "", text) # remove all characters that are not a-z
    text = re.sub(r"\s+", " ", text) # remove extra spaces
    return text

def lemmatize(text):
    doc = nlp(text)
    for token in doc:
        text = text.replace(token.text, (token.lemma_).lower())
    return text
# print(lemmatize(clean_text(t)))
filel = open("clean.txt", "w").write(lemmatize(clean_text(t)))