import unittest
import yaml
import requests


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        settings = yaml.load(open('settings.yml').read())
        self.settings = settings

        self.base_url = settings['base_url']
        login = settings['credentials']['login']
        pwd = settings['credentials']['password']
        self.creds = (login, pwd)

        self.login(login, pwd)

    def login(self, login, pwd):
        url = self.base_url + '/user/login'
        params = {
            'login': login,
            'password': pwd,
        }

        r = requests.post(url, data=params)
        self.cookies = r.cookies

    def create_issue(self):
        url = self.base_url + '/issue/'

        params = {
            'project': 'API',
            'summary': '[Test issue] summary',
            'description': 'Test - created by autotests'
        }

        r = requests.put(url, data=params, cookies=self.cookies)
        self.assertEqual(r.status_code, 201)

        issue_id = r.headers['Location'].split('/')[-1]

        return issue_id