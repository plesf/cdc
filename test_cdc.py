import unittest
import cdc


class TestCdc(unittest.TestCase):

    def test_query_depression(self):
        expected = [{'mediatype': u'Video', 'language': u'English', 'title': u'Creating a Healthier Future through Prevention of Child Maltreatment'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Rest Easy'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Sleep On It'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Defeating Depression'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Defeating Depression'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Breastfeed for Better Health'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Don&#39;t be a Night Owl'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Coping With Depression and Thoughts of Suicide After a Disaster PSA (:30)'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Diabetes and Depression in Older Women'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Have a Happy Birthday'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Have a Happy Birthday'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'No Rest for the Weary'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'No Rest for the Weary'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Coping With Depression and Thoughts of Suicide After a Disaster'}]
        actual = cdc.search(query='depression')
        self.assertEqual(expected, actual)

    def test_query_params(self):
        expected = [{'mediatype': u'Podcast', 'language': u'English', 'title': u'Rest Easy'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Sleep On It'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Defeating Depression'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Defeating Depression'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Breastfeed for Better Health'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Don&#39;t be a Night Owl'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Coping With Depression and Thoughts of Suicide After a Disaster PSA (:30)'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Diabetes and Depression in Older Women'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Have a Happy Birthday'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Have a Happy Birthday'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'No Rest for the Weary'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'No Rest for the Weary'},
                    {'mediatype': u'Podcast', 'language': u'English', 'title': u'Coping With Depression and Thoughts of Suicide After a Disaster'}]
        actual = cdc.search(query='depression', language='English', media_type='Podcast')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
