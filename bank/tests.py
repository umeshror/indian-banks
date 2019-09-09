from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from bank import Bank, Branch


class TestBranchIFSCView(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Test user', password='admin123')
        self.client.force_authenticate(user=self.user)
        self.bank = Bank.objects.create(id=1234, name="TEST BANK")
        self.branch = Branch.objects.create(bank=self.bank,
                                            ifsc="TESTIFSC",
                                            branch="TEST BRANCH",
                                            city="TEST CITY",
                                            district="TEST DISTRICT",
                                            state="TEST STATE",
                                            address="TEST address")

    def test_get_api_200_status(self):
        response = self.client.get(reverse('branch-ifsc', kwargs={'ifsc_code': "TESTIFSC"}))
        self.assertEqual(response.status_code, 200)

        actual_output = response.data

        expected_output = {'city': 'TEST CITY',
                           'district': 'TEST DISTRICT',
                           'ifsc': 'TESTIFSC',
                           'state': 'TEST STATE',
                           'branch': 'TEST BRANCH',
                           'address': 'TEST address',
                           'bank': 'TEST BANK'}

        self.assertDictEqual(actual_output, expected_output)

    def test_get_api_404_not_found(self):
        response = self.client.get(reverse('branch-ifsc', kwargs={'ifsc_code': "IncorrectIFSC"}))
        self.assertEqual(response.status_code, 404)

        actual_output = response.data
        expected_output = {
            "detail": "Branch not found for given IFSC code"
        }

        self.assertDictEqual(actual_output, expected_output)


class TestBankBranchView(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Test user', password='admin123')
        self.client.force_authenticate(user=self.user)
        self.bank_1 = Bank.objects.create(id=1234, name="TEST BANK 1")
        self.bank_2 = Bank.objects.create(id=1235, name="TEST BANK 2")
        self.bank_3 = Bank.objects.create(id=1236, name="TEST BANK 3")
        self.branch_1 = Branch.objects.create(bank=self.bank_1,
                                              ifsc="TESTIFSC",
                                              branch="TEST BRANCH 1",
                                              city="TEST CITY 1",
                                              district="TEST DISTRICT",
                                              state="TEST STATE",
                                              address="Test address")

        self.branch_2 = Branch.objects.create(bank=self.bank_1,
                                              ifsc="TESTIFSC 2",
                                              branch="TEST BRANCH",
                                              city="TEST CITY 2",
                                              district="TEST DISTRICT",
                                              state="TEST STATE",
                                              address="Test address")

        self.branch_3 = Branch.objects.create(bank=self.bank_2,
                                              ifsc="TESTIFSC 3",
                                              branch="TEST BRANCH",
                                              city="TEST CITY",
                                              district="TEST DISTRICT",
                                              state="TEST STATE",
                                              address="Test address")

    def test_get_api_200_status(self):
        response = self.client.get(reverse('bank-branch'), {'city': "Test city 1", "bank": "TEST BANK 1"})

        actual_output = response.data

        expected_output = [{'address': 'Test address',
                            'bank': 'TEST BANK 1',
                            'branch': 'TEST BRANCH 1',
                            'city': 'TEST CITY 1',
                            'district': 'TEST DISTRICT',
                            'ifsc': 'TESTIFSC',
                            'state': 'TEST STATE'}]

        self.assertEqual(response.status_code, 200)

        self.assertListEqual(actual_output, expected_output)

    def test_get_api_422_status(self):
        response = self.client.get(reverse('bank-branch'), {"bank": "TEST BANK 3"})

        actual_output = response.data

        expected_output = {"detail": "Both City and Bank names are required "
                                     "to get all the branches of the Bank in the City."}

        self.assertEqual(response.status_code, 422)

        self.assertDictEqual(actual_output, expected_output)

    def test_get_api_404_status(self):
        response = self.client.get(reverse('bank-branch'), {'city': "Test city 1", "bank": "TEST BANK 3"})

        actual_output = response.data

        expected_output = {"detail": "No branch found for provided Bank and City."}

        self.assertEqual(response.status_code, 404)

        self.assertDictEqual(actual_output, expected_output)
