'''
Extraction Module
'''

import os
from os import environ
from dotenv import load_dotenv
import re
from spacy.lang.en import English
from medtrialextractor import RxnExtractor
import warnings
from seqeval.metrics.sequence_labeling import get_entities
warnings.filterwarnings("ignore")

nlp = English()

tokenizer = nlp.tokenizer


def tokenize(text):
    text = ' '.join([t.text for t in tokenizer(text)])
    text = re.sub('\n+', '\n', text)
    text = re.sub('[ ]{2,}', ' ', text)
    text = '\n'.join([s.strip() for s in text.split('\n') if s.strip()])
    return text


def get_bio(paragraphs, extractor):

    # tokenize paragraphs
    tok_pars = [tokenize(p) for p in paragraphs]

    toks, labels = extractor.get_entities(tok_pars)

    return toks, labels


def get_ents(paragraphs):

    # get extractor
    config_path = os.path.join(os.path.realpath('.'), '.env')
    load_dotenv(dotenv_path=config_path)
    models_dir = environ.get('MODELS_DIR')
    model_dir = os.path.join(models_dir, 'model_v1')
    extractor = RxnExtractor(model_dir=model_dir)

    toks, labs = get_bio(paragraphs, extractor)

    res = []
    for t, l in zip(toks, labs):

        spans = get_entities(l)

        res.append({
            'text':  ' '.join(t),
            'spans': spans,
            'links': []
        })
    return res
