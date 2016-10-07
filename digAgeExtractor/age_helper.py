# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-10-05 16:01:52
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-06 20:44:43

import json
import string
import pygtrie as trie
from digDictionaryExtractor.populate_trie import populate_trie
from digDictionaryExtractor.name_dictionary_extractor import get_name_dictionary_extractor
from digExtractor.extractor_processor import ExtractorProcessor
from digCrfTokenizer.crf_tokenizer import CrfTokenizer

def generate_age_dictionary(start=18, end=50):
    dictionary = [str(_) for _ in range(start, end + 1)]
    # dictionary = json.dumps(dictionary, indent=4)
    return dictionary

ages = generate_age_dictionary()
ages_trie = populate_trie(iter(ages))

def tokenize(raw):
    t = CrfTokenizer()
    t.setRecognizeHtmlEntities(True)
    t.setRecognizeHtmlTags(True)
    t.setSkipHtmlTags(True)
    t.setRecognizePunctuation(True)
    tokens = t.tokenize(raw)
    return tokens

def extract(doc, input_fields='text', output_field='names'):
    doc = {input_fields: doc}
    e = get_name_dictionary_extractor(ages_trie).set_pre_filter(lambda x:x)
    ep = ExtractorProcessor().set_input_fields(input_fields).set_output_field(output_field).set_extractor(e)

    if isinstance(input_fields, basestring):
        doc[input_fields] = tokenize(doc[input_fields]) if isinstance(doc[input_fields], basestring) else doc[input_fields]
    elif isinstance(input_fields, list):
        for input_field in input_fields:
            doc[input_field] = tokenize(doc[input_field]) if isinstance(doc[input_field], basestring) else doc[input_field]
    else:
        return None

    updated_doc = ep.extract(doc)
    if output_field not in updated_doc:
        return None
    return updated_doc[output_field][0]['value']

