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
        doc = {"foo": "\r\n    Posted:\r\n    Saturday, June 25, 2016 1:04 AM\r\n   \n \n \n \n \r\n      \r\n\r\n      \r\n\r\n      \r\n        \r\n        \r\n          Are you A pretty thick & curvy female READY to make CHANGES with your LIFE??? TIRED of being STUCK.Well now you have the chance to earn fast money now. Im Looking for a few attractive ladies to start TODAY. First time ladies are welcome. \n \nSafety is my #1 concern!! Your safety comes First \n \n \n**Must be Reliable, Honest, Open-minded & Attractive** \nThis is for FULL or PART time work. \nWE OFFER DAY SHIFTS AND NIGHT SHIFTS. SAFETY IS OUR MAIN PRIORITY. WE ARE LOOKING FOR NON FLAKY GIRLS THAT ARE ABLE TO PROVIDE A 1 ON 1 ADULT CEXPERIENCE \n \nWE HAVE A LARGE DATA BASE OF REGULAR CLIENTS ALSO WE USE THE BEST WEBSITES OUT THERE NOT JUST CRAIGSLIST OR BP TO ADVERTISE YOU ON. EXPERIENCE IS NOT NECESSARY Just have the desire to make a lot of $$money$$ \nBUT IF YOU DO HAVE EXPERIENCE THAT IS OK. \n \nWE ARE ALSO HIRING STRIPPERS FOR BACHELOR PARTIES AND DO ADULT FILM WORK \nOPPORTUNITIES \n305-479-9468\r\n        \r\n      \r\n     \n Poster's age: 26 \n \r\n         Location:\r\n        Orlando\r\n       \n  Post ID: 12295358 orlando \n \n \n \n \n Are you A pretty thick & curvy female READY to make CHANGES with your LIFE??? TIRED of being STUCK.Well now you have the chance to earn fast money now. Im Looking for a few attractive ladies to start TODAY. First time ladies are welcome. Safety is my #1 concern!! Your safety comes First **Must be Reliable, Honest, Open-minded & Attractive** This is for FULL or PART time work. WE OFFER DAY SHIFTS AND NIGHT SHIFTS. SAFETY IS OUR MAIN PRIORITY. WE ARE LOOKING FOR NON FLAKY GIRLS THAT ARE ABLE TO PROVIDE A 1 ON 1 ADULT CEXPERIENCE WE HAVE A LARGE DATA BASE OF REGULAR CLIENTS ALSO WE USE THE BEST WEBSITES OUT THERE NOT JUST CRAIGSLIST OR BP TO ADVERTISE YOU ON. EXPERIENCE IS NOT NECESSARY Just have the desire to make a lot of $$money$$ BUT IF YOU DO HAVE EXPERIENCE THAT IS OK. WE ARE ALSO HIRING STRIPPERS FOR BACHELOR PARTIES AND DO ADULT FILM WORK OPPORTUNITIES 305-479-9468 _________ ________ _______ ___ESCORTS & STRIPPERS WANTED___ _________ _______ _______ - 26 _________ ________ _______ ___ESCORTS & STRIPPERS WANTED___ _________ _______ _______ - Orlando adult jobs - backpage.com"}
    
        self.assertEquals(extract(doc, input_fields='foo'), list(['25', '26']))

    

if __name__ == '__main__':
    unittest.main()



