# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-10-05 16:01:52
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-06 20:11:28

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
        print 'sss'
        for input_field in input_fields:
            doc[input_field] = tokenize(doc[input_field]) if isinstance(doc[input_field], basestring) else doc[input_field]
    else:
        return None

    updated_doc = ep.extract(doc)
    # print updated_doc
    if output_field not in updated_doc:
        return None
    return updated_doc[output_field][0]['value']

if __name__ == '__main__':
    doc = "\r\n    Posted:\r\n    Saturday, June 25, 2016 1:04 AM\r\n   \n \n \n \n \r\n      \r\n\r\n      \r\n\r\n      \r\n        \r\n        \r\n          Are you A pretty thick & curvy female READY to make CHANGES with your LIFE??? TIRED of being STUCK.Well now you have the chance to earn fast money now. Im Looking for a few attractive ladies to start TODAY. First time ladies are welcome. \n \nSafety is my #1 concern!! Your safety comes First \n \n \n**Must be Reliable, Honest, Open-minded & Attractive** \nThis is for FULL or PART time work. \nWE OFFER DAY SHIFTS AND NIGHT SHIFTS. SAFETY IS OUR MAIN PRIORITY. WE ARE LOOKING FOR NON FLAKY GIRLS THAT ARE ABLE TO PROVIDE A 1 ON 1 ADULT CEXPERIENCE \n \nWE HAVE A LARGE DATA BASE OF REGULAR CLIENTS ALSO WE USE THE BEST WEBSITES OUT THERE NOT JUST CRAIGSLIST OR BP TO ADVERTISE YOU ON. EXPERIENCE IS NOT NECESSARY Just have the desire to make a lot of $$money$$ \nBUT IF YOU DO HAVE EXPERIENCE THAT IS OK. \n \nWE ARE ALSO HIRING STRIPPERS FOR BACHELOR PARTIES AND DO ADULT FILM WORK \nOPPORTUNITIES \n305-479-9468\r\n        \r\n      \r\n     \n Poster's age: 26 \n \r\n         Location:\r\n        Orlando\r\n       \n  Post ID: 12295358 orlando \n \n \n \n \n Are you A pretty thick & curvy female READY to make CHANGES with your LIFE??? TIRED of being STUCK.Well now you have the chance to earn fast money now. Im Looking for a few attractive ladies to start TODAY. First time ladies are welcome. Safety is my #1 concern!! Your safety comes First **Must be Reliable, Honest, Open-minded & Attractive** This is for FULL or PART time work. WE OFFER DAY SHIFTS AND NIGHT SHIFTS. SAFETY IS OUR MAIN PRIORITY. WE ARE LOOKING FOR NON FLAKY GIRLS THAT ARE ABLE TO PROVIDE A 1 ON 1 ADULT CEXPERIENCE WE HAVE A LARGE DATA BASE OF REGULAR CLIENTS ALSO WE USE THE BEST WEBSITES OUT THERE NOT JUST CRAIGSLIST OR BP TO ADVERTISE YOU ON. EXPERIENCE IS NOT NECESSARY Just have the desire to make a lot of $$money$$ BUT IF YOU DO HAVE EXPERIENCE THAT IS OK. WE ARE ALSO HIRING STRIPPERS FOR BACHELOR PARTIES AND DO ADULT FILM WORK OPPORTUNITIES 305-479-9468 _________ ________ _______ ___ESCORTS & STRIPPERS WANTED___ _________ _______ _______ - 26 _________ ________ _______ ___ESCORTS & STRIPPERS WANTED___ _________ _______ _______ - Orlando adult jobs - backpage.com"
    print extract(doc)


