# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-10-05 16:01:52
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-05 16:25:02

import json
import pygtrie as trie
from digDictionaryExtractor.populate_trie import populate_trie
from digDictionaryExtractor.name_dictionary_extractor import get_name_dictionary_extractor
from digExtractor.extractor_processor import ExtractorProcessor

def generate_age_dictionary(start=18, end=50):
    dictionary = [str(_) for _ in range(start, end + 1)]
    # dictionary = json.dumps(dictionary, indent=4)
    return dictionary

ages = generate_age_dictionary()
ages_trie = populate_trie(iter(ages))

def extract(doc, input_fields=None, output_field='names'):
    doc = {"foo": ['18', 'Barbara']}
    e = get_name_dictionary_extractor(ages_trie)
    ep = ExtractorProcessor().set_input_fields('foo').set_output_field(output_field).set_extractor(e)

    updated_doc = ep.extract(doc)
    if output_field not in updated_doc:
        return None

    return updated_doc[output_field][0]['value']

if __name__ == '__main__':
    
    print extract(doc)


