import unittest
import monitor

class TestMonitorMethods(unittest.TestCase):

    def test_get_status_valid_response(self):
        input = {
            "link": "https://apra.me",
            "content": "Apramey Bhat"
        }
        result = monitor.get_status(input)       
        self.assertGreater(result.responseTime, 0)
        self.assertEqual(result.response, '200 OK')
        self.assertEqual(result.isValidContent, True)
        self.assertEqual(result.content, input['content'])
        self.assertEqual(result.link, input['link'])

    def test_get_status_content_mismatch(self):
        input = {
            "link": "https://apra.me",
            "content": "Aprameya"
        }
        result = monitor.get_status(input)       
        self.assertEqual(result.isValidContent, False)

    def test_get_status_HTTP_error(self):
        input = {
            "link": "https://amazon.com",
            "content": "Today's Deals"
        }
        result = monitor.get_status(input)       
        self.assertEqual(result.response, '503 Service Unavailable')

    def test_get_status_exception(self):
        input = {
            "link": 5,
            "content": "Today's Deals"
        }
        result = monitor.get_status(input)       
        self.assertTrue('Invalid URL' in result.response)

if __name__ == '__main__':
    unittest.main()