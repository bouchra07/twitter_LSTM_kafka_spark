import re
from nltk import PorterStemmer
import string

class CleanText:

    def clean_text(self, txt):
        from nltk.corpus import stopwords
        txt = txt.lower()
        txt = re.sub(r"(?<=\w)nt", "not", txt)  # change don't to do not cna't to cannot
        txt = re.sub(r"(@\S+)", "", txt)  # remove hashtags
        txt = re.sub(r'\W', ' ', str(txt))  # remove all special characters including apastrophie
        txt = txt.translate(str.maketrans('', '', string.punctuation))  # remove punctuations
        txt = re.sub(r'\s+[a-zA-Z]\s+', ' ',
                     txt)  # remove all single characters (it's -> it s then we need to remove s)
        txt = re.sub(r'\s+', ' ', txt, flags=re.I)  # Substituting multiple spaces with single space
        txt = re.sub(r"(http\S+|http)", "", txt)  # remove links
        txt = ' '.join([PorterStemmer().stem(word=word) for word in txt.split(" ") if
                        word not in stopwords.words('english')])  # stem & remove stop words
        txt = ''.join([i for i in txt if not i.isdigit()]).strip()  # remove digits ()
        return txt

    def clean_text_NER(self, txt):

        txt = " ".join([self.camel_case_split(t) for t in txt.split(" ")])
        txt = re.sub(r"(?<=\w)nt", "not", txt)  # change don't to do not cna't to cannot
        txt = re.sub(r'\W', ' ', str(txt))  # remove all special characters including apastrophie
        txt = txt.translate(str.maketrans('', '', string.punctuation))  # remove punctuations
        txt = re.sub(r'\s+[a-zA-Z]\s+', ' ',
                     txt)  # remove all single characters (it's -> it s then we need to remove s)
        txt = re.sub(r'\s+', ' ', txt, flags=re.I)  # Substituting multiple spaces with single space
        txt = re.sub(r"(http\S+|http)", "", txt)  # remove links
        return txt