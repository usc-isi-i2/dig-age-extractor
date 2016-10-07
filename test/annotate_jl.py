# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-10-06 20:17:15
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-06 21:02:50

import os
import sys
import json
import codecs

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

from digAgeExtractor.age_helper import *

def annotate(intput_path, output_path=None):
    dataset = []
    i = 0
    for line in codecs.open(intput_path, 'r'):
        try:
            json_obj = json.loads(line)
            # json_obj = yaml.safe_load(line)
        except Exception as e:
            continue
        i += 1

        content = json_obj['content'] if 'content' in json_obj else None
        correct = json_obj['correct'] if 'correct' in json_obj else None
        # annotated = json_obj['annotated'] if 'annotated' in json_obj else None
        annotated = extract(content)
        annotated = annotated if annotated else []

 
        node_text = content if content else ' '

        if not isinstance(node_text, basestring):
            try:
                node_text = ' '.join([_ for _ in node_text if _ and isinstance(_, basestring)])
            except:
                node_text = str(node_text)

        node_text = node_text.encode('ascii', 'ignore')
        dataset.append({
                'content': content, 
                'correct': sorted(correct), 
                'annotated': sorted(annotated)
            })

        # .append((node_text, sorted(list(set(correct))), sorted(list(set(correct)))))

    # dataset = [{'content': content, 'correct': correct, 'annotated': annotated} for (content, correct, _) in dataset]

    if not output_path:
        output_path = intput_path

    with open(output_path, 'wb') as file_handler:
        for data in dataset:
            file_handler.write(json.dumps(data) + '\n')

    return dataset

if __name__ == '__main__':
    annotate(os.path.join(TEST_DATA_DIR, 'age.json'))
