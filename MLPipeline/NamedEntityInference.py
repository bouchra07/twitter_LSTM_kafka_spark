import spacy
import en_core_web_sm
from pathlib import Path
from .CleanText import CleanText


class NamedEntitiesInference:

    def __init__(self):

        self.nlp = en_core_web_sm.load()
        output_dir = Path('./models/model_NER/')
        print("Loading from", output_dir)
        self.nlp_updated = spacy.load(output_dir)
        self.clean_text = CleanText()


    def get_Entities(self, text):
        text = self.clean_text.clean_text_NER(text)
        doc = self.nlp_updated(text)
        labels = [(X.text, X.label_) for X in doc.ents]

        doc = self.nlp(text)
        labels_norm = [(X.text, X.label_) for X in doc.ents]
        labels.extend(labels_norm)

        return labels