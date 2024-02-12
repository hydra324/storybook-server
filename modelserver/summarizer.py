import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import spacy
import logging


class Summarizer:
    def __init__(self) -> None:
        # self.nlp = spacy.load("en_core_web_sm")
        logging.info('initialized summarizer')

    
    def summarize(self,text) -> list[list[str]]:
        # Tokenize the text
        tokens = word_tokenize(text)
        # Part-of-speech tagging using NLTK
        pos_tags = pos_tag(tokens)
        logging.info(f'pos tags : {pos_tags}')
        # Perform named entity recognition (NER) using spaCy
        # doc = self.nlp(text)
        # ner_tags = [(ent.text, ent.label_) for ent in doc.ents]

        # logging.info(f'ner tags: {ner_tags}')

        # Extracting keywords and actions
        keywords = []
        # actions = []

        for word, tag in pos_tags:
            if tag.startswith('N') or tag.startswith('V'):  # Nouns or verbs are considered keywords
                keywords.append(word)
            # elif word.lower() in ["submit", "available", "consider"]:  # Specific verbs considered as actions
            #     actions.append(word)

        # for entity, label in ner_tags:
        #     if label == "DATE" or label == "ORG":  # Date or organization entities considered as keywords
        #         keywords.append(entity)

        # Remove duplicates
        keywords = list(set(keywords))
        # actions = list(set(actions))

        print("Keywords:", keywords)
        # print("Actions:", actions)

        # return [keywords,actions]
        return keywords