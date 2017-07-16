from base_test_case import BaseTestCase
import requests

class CreateIssue(BaseTestCase):

    def test_create_issue(self):
        url = self.base_url + '/issue/'
        params = {
            'project' : 'API',
            'summary' : 'test issue',
            'description' : 'test issue by autotest',
        }

        r = requests.put(url, data=params, cookies = self.cookies)
        self.assertEqual(r.status_code, 201)