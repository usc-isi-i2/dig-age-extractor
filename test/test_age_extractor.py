import unittest
from digExtractor.extractor_processor import ExtractorProcessor
from digAgeExtractor.age_helper import get_age_dictionary_extractor


class TestAgeExtractorMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_age_extractor(self):
        doc = {'content': ["Poster's", "age", "26", "Location",
                           "Orlando", "Post", "ID", "12295358",
                           "Date", "June", "25", "2015"],
               'b': 'world'}

        extractor = get_age_dictionary_extractor()
        extractor_processor = ExtractorProcessor().set_input_fields(
            'content').set_output_field('extracted').set_extractor(extractor)
        updated_doc = extractor_processor.extract(doc)

        result1 = updated_doc['extracted'][0]['result'][0]
        result2 = updated_doc['extracted'][0]['result'][1]
        self.assertEqual(result1['value'], '26')
        self.assertEqual(result2['value'], '25')

    def test_age_extractor_with_context(self):
        doc = {'content': ["Poster's", "age", "26", "Location",
                           "Orlando", "Post", "ID", "12295358",
                           "Date", "June", "25", "2015"],
               'b': 'world'}

        extractor = get_age_dictionary_extractor()
        extractor.set_include_context(True)
        extractor_processor = ExtractorProcessor().set_input_fields(
            'content').set_output_field('extracted').set_extractor(extractor)
        updated_doc = extractor_processor.extract(doc)

        result1 = updated_doc['extracted'][0]['result'][0]
        result2 = updated_doc['extracted'][0]['result'][1]
        self.assertEqual(result1['value'], '26')
        self.assertEqual(result1['context']['start'], 2)
        self.assertEqual(result1['context']['end'], 3)
        self.assertEqual(result2['value'], '25')
        self.assertEqual(result2['context']['start'], 10)
        self.assertEqual(result2['context']['end'], 11)


if __name__ == '__main__':
    unittest.main()
