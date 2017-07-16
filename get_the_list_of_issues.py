from base_test_case import BaseTestCase

class GetTheListOfIssues(BaseTestCase):
    def get_the_list_of_issues(self):
        url = self.base_url +'/issue/'
