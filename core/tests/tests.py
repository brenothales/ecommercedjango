from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class IndexViewTestCase(TestCase):

    def setup(self):
        self.client = Client()
        self.url = reverse('index')


    def tearDown(self):
        pass


    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.test_status_code, 200)


    def test_template_used(selft):
        response = selft.client.get(self.url)
        selft.assertTemplateUsed(response, 'index.html')

