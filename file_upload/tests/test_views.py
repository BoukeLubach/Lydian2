from django.test import TestCase, Client
from django.conf import settings
import tempfile



class TestUploadviews(TestCase):
    def setUp(self):
        settings.MEDIA_ROOT = tempfile.mkdtemp()            #create tempfile for uploaded media files to auto-delete after testing


    def test_csvupload_form(self):
        c = Client()
        response = c.get('/upload_csv/')
        self.assertEqual(response.status_code, 200)