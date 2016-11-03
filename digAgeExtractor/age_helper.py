# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-10-05 16:01:52
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-10 15:43:22


from digDictionaryExtractor.populate_trie import populate_trie
from digDictionaryExtractor.dictionary_extractor import DictionaryExtractor


def generate_age_dictionary(start=18, end=50):
    dictionary = [str(_) for _ in range(start, end + 1)]
    return dictionary


default_ages = generate_age_dictionary()


default_ages_trie = populate_trie(iter(default_ages))


def get_age_dictionary_extractor(ages_trie=default_ages_trie):
    """Method for creating default name dictionary extractor"""
    return DictionaryExtractor()\
        .set_trie(ages_trie)\
        .set_metadata({'extractor': 'dig_age_dictionary_extractor'})
