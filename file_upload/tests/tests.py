# from django.test import TestCase, Client
# from .models import Tagmodel, Datafile
# import pandas as pd
# from .process_uploaded_files import create_tagmodels_from_csvfile
# from django.conf import settings
# import tempfile


# # Create your tests here.

# class TestCsvFile(TestCase):
#     def test_if_pandas_can_use_csvfile(self):
#         with open('file_upload/testfiles/upload_testfile1.csv') as csvfile:
#             df = pd.read_csv(csvfile, sep=';')

#             self.assertEqual(df.shape, (8760, 7))
#             self.assertEqual(list(df.columns), ["DateTime", "KOELGLEID_MSP_A.MSPChanged", "KOELING_BAK:0310TT110.MEAS", 
#                                             "KOELING_BAK:0310TT120.MEAS", "KOELING_BAK:0310TT121.MEAS", "KrachtMeting_MP1.KrachtMeting", 
#                                             "KrachtMeting_MP1.KrachtMeting.Average"])

#             df = df.set_index(pd.to_datetime(df['DateTime'], dayfirst=True))
#             df = df.drop(columns = 'DateTime')
#             self.assertEqual(df.index.dtype, "datetime64[ns]")
#             self.assertEqual(df.shape[1], 6)
            


# class TestUpload(TestCase):
#     def setUp(self):
#         settings.MEDIA_ROOT = tempfile.mkdtemp()            #create tempfile for uploaded media files to auto-delete after testing


#     def test_upload_form(self):
#         c = Client()
#         response = c.get('/upload/')
#         self.assertEqual(response.status_code, 200)

#     def test_if_file_is_uploaded(self):
#         c = Client()

#         with open('file_upload/testfiles/upload_testfile1.csv') as csvfile:
#             c.post('/upload/', {'csvfile': csvfile})
        
#         self.assertEqual(Datafile.objects.filter(csvfile__icontains="upload_testfile1").exists(), True)


#     def test_upload_multiple_files_at_once(self):

#         file_list = [
#             'file_upload/testfiles/upload_testfile1.csv',
#             'file_upload/testfiles/upload_testfile2.csv'
#         ]
#         data = {}
#         files = []
#         for file in file_list:
#             fp = open(file, 'r')
#             files.append(fp)

#         data['csvfile'] = files

#         c = Client()
#         response = c.post('/upload/', data, follow=True)

#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(Datafile.objects.filter(csvfile__icontains="upload_testfile1").exists(), True)
#         self.assertEqual(Datafile.objects.filter(csvfile__icontains="upload_testfile2").exists(), True)


#         self.assertEqual(Tagmodel.objects.filter(name="KOELGLEID_MSP_A.MSPChanged").exists(), True)
#         self.assertEqual(Tagmodel.objects.filter(name="KOELING_BAK:0310TT110.MEAS").exists(), True)
#         self.assertEqual(Tagmodel.objects.filter(name="KOELING_BAK:0310TT120.MEAS").exists(), True)
#         self.assertEqual(Tagmodel.objects.filter(name="ADDITIEF:0320LT130.PNT").exists(), True)
#         self.assertEqual(Tagmodel.objects.filter(name="ADDITIEF:0320LT230.PNT").exists(), True)
#         self.assertEqual(Tagmodel.objects.filter(name="ADDITIEF:0320LT310.PNT").exists(), True)




#     # def test_non_csv_file_upload(self):
#     #     c = Client()

#     #     with open('file_upload/testfiles/not_a_csv_file') as not_a_csv_file:
#     #         response = c.post('/upload/', {'csvfile': not_a_csv_file}, follow=True)

#     #         self.assertEqual(response.status_code, 200)
#     #         self.assertTemplateUsed(response, 'file_upload/upload_failed.html')

#     #     self.assertEqual(Datafile.objects.filter(csvfile__icontains="not_a_csv_file").exists(), False)



#     def test_if_tagmodels_are_created_from_uploaded_file(self):
#         c = Client()

#         with open('file_upload/testfiles/upload_testfile1.csv', encoding="utf8") as csvfile:
#             c.post('/upload/', {'csvfile': csvfile})
        
#         self.assertEqual(Tagmodel.objects.filter(name="KOELGLEID_MSP_A.MSPChanged").exists(), True)
#         self.assertEqual(Tagmodel.objects.filter(name="KOELING_BAK:0310TT110.MEAS").exists(), True)
#         self.assertEqual(Tagmodel.objects.filter(name="KOELING_BAK:0310TT120.MEAS").exists(), True)
#         self.assertEqual(Tagmodel.objects.filter(name="KOELING_BAK:0310TT121.MEAS").exists(), True)
#         self.assertEqual(Tagmodel.objects.filter(name="KrachtMeting_MP1.KrachtMeting").exists(), True)
#         self.assertEqual(Tagmodel.objects.filter(name="KrachtMeting_MP1.KrachtMeting.Average").exists(), True)





# class TestTagmodelCreation(TestCase):

    
#     def test_manually_create_tagmodels_from_csvfile(self):
#         c = Client()
#         with open('file_upload/testfiles/upload_testfile1.csv') as csvfile:

#             df = pd.read_csv(csvfile, encoding='UTF-8', sep=';')
#             df = df.set_index(pd.to_datetime(df['DateTime'], dayfirst=True))
#             df = df.drop(columns = 'DateTime')

#             for tagname in df.columns:
#                 tag_instance = Tagmodel(name=tagname, csv_filename = "upload_testfile1.csv")
#                 tag_instance.save()

#             self.assertEqual(Tagmodel.objects.filter(name="KOELGLEID_MSP_A.MSPChanged").exists(), True)
#             self.assertEqual(Tagmodel.objects.filter(name="KOELING_BAK:0310TT110.MEAS").exists(), True)
#             self.assertEqual(Tagmodel.objects.filter(name="KOELING_BAK:0310TT120.MEAS").exists(), True)
#             self.assertEqual(Tagmodel.objects.filter(name="KOELING_BAK:0310TT121.MEAS").exists(), True)
#             self.assertEqual(Tagmodel.objects.filter(name="KrachtMeting_MP1.KrachtMeting").exists(), True)
#             self.assertEqual(Tagmodel.objects.filter(name="KrachtMeting_MP1.KrachtMeting.Average").exists(), True)

#     def test_create_tagmodels_from_csvfile_function(self):
#         c = Client()
#         with open('file_upload/testfiles/upload_testfile1.csv') as csvfile:
#             create_tagmodels_from_csvfile(csvfile)
        
#         self.assertEqual(Tagmodel.objects.filter(name="KOELGLEID_MSP_A.MSPChanged").exists(), True)
#         self.assertEqual(Tagmodel.objects.filter(name="KOELING_BAK:0310TT110.MEAS").exists(), True)
#         self.assertEqual(Tagmodel.objects.filter(name="KOELING_BAK:0310TT120.MEAS").exists(), True)
#         self.assertEqual(Tagmodel.objects.filter(name="KOELING_BAK:0310TT121.MEAS").exists(), True)
#         self.assertEqual(Tagmodel.objects.filter(name="KrachtMeting_MP1.KrachtMeting").exists(), True)
#         self.assertEqual(Tagmodel.objects.filter(name="KrachtMeting_MP1.KrachtMeting.Average").exists(), True)


