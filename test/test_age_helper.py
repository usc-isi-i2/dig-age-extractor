import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

from digAgeExtractor.age_helper import *

class TestAgeHelperMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_extract(self):
        doc = "\n \n Age: \n 21 \n \n \n Location: \n Bangalore India \n \n \n Eyes: \n blue \n \n \n Hair color: \n black \n \n \n Hair lenght: \n medium long \n \n \n Bust size: \n B \n \n \n Bust type: \n natural \n \n \n Travel: \n no \n \n \n Weight: \n 128 lb (58 kg) \n \n \n Height: \n 5.5 ft (166 cm) \n \n \n Ethnicity: \n Asian \n \n \n Orientation: \n bisexual \n \n \n Smoker: \n no \n \n \n Nationality: \n Indian \n \n \n Languages: \n \n                                English, \n                                Hindi\n                             \n \n \n Provides: \n Outcall + Incall \n \n \n Meeting with: \n man \n \n \n A-level: \n yes \n \n \n"
        
        self.assertEquals(extract(doc, input_fields='foo'), list(['21']))

    

if __name__ == '__main__':
    unittest.main()



