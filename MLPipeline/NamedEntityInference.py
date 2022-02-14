import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
import re
import string
from pathlib import Path
from .CleanText import CleanText


class NameEntities:

    def __init__(self):

        self.nlp = en_core_web_sm.load()
        output_dir = Path('../model_NER/')
        print("Loading from", output_dir)
        self.nlp_updated = spacy.load(output_dir)
        self.clean_text = CleanText()


    def camel_case_split(self, str):
        words = [[str[0]]]

        for c in str[1:]:
            if words[-1][-1].islower() and c.isupper():
                words.append(list(c))
            else:
                words[-1].append(c)

        return " ".join([''.join(word) for word in words])

    def get_Entities(self, text):
        text = self.clean_text.clean_text_NER(text)
        doc = self.nlp_updated(text)
        labels = [(X.text, X.label_) for X in doc.ents]

        doc = self.nlp(text)
        labels_norm = [(X.text, X.label_) for X in doc.ents]
        labels.extend(labels_norm)

        return labels
