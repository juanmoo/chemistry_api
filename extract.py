'''
Extraction Module
'''

import os
from os import environ
from dotenv import load_dotenv
import re
from spacy.lang.en import English
from chemrxnextractor import RxnExtractor
import warnings
from chemdataextractor.doc import Paragraph

warnings.filterwarnings("ignore")

nlp = English()
tokenizer = nlp.tokenizer
extractor = None


def tokenize(text):
    text = ' '.join([t.text for t in tokenizer(text)])
    text = re.sub('\n+', '\n', text)
    text = re.sub('[ ]{2,}', ' ', text)
    text = '\n'.join([s.strip() for s in text.split('\n') if s.strip()])
    return text


def get_ents(paragraphs):

    # get extractor
    global extractor

    config_path = os.path.join(os.path.realpath('.'), '.env')
    load_dotenv(dotenv_path=config_path)
    models_dir = environ.get('MODELS_DIR')
    model_name = environ.get('ACTIVE_MODEL')
    model_dir = os.path.join(models_dir, model_name)
    
    if extractor is None:
        extractor = RxnExtractor(model_dir=model_dir)

    # Get sentences
    paragraphs = [Paragraph(p).sentences for p in paragraphs]
    sentences = []

    for par in paragraphs:
        for sent in par:
            sentences.append(str(sent))

    reactions = extractor.get_reactions(sentences)

    # Re-combine sentences into paragraphs
    extractions = []
    off = 0
    for par in paragraphs:
        tokens = []
        recs = []
        for j in range(off, off + len(par)):
            sent_react = reactions[j]
            for r in sent_react["reactions"]:
                r_offset = {}
                for k in r:
                    r_offset[k] = []
                    for e in r[k]:
                        if isinstance(e, (list, tuple)):
                            r_offset[k].append([j + len(tokens) for j in e])
                        else:
                            r_offset[k].append(e + len(tokens))

                recs.append(r_offset)
                
            tokens.extend(sent_react['tokens'])

        extractions.append({'tokens': tokens, 'reactions':recs})
        off += len(par)

    return extractions
